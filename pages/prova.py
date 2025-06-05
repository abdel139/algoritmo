#if not st.session_state["handle_click"]:
#    st.session_state["handle_click"] = 0

import streamlit as st
import os
import pandas as pd,numpy as np
import altair as alt
import pydeck as pdk
import urllib.parse
from streamlit_image_select import image_select


st.set_page_config(page_title="Simulatore di Algoritmo", layout="centered")
#if "likes_utenti" not in st.session_state:
#    st.session_state.likes_utenti = {}
imgs_2 = []
tags = set()
for nome_file in os.listdir("static"):
    if nome_file.endswith((".jpg", ".png", ".jpeg")):
        tag = nome_file.split("_")[0]
        tags.add(tag)
        imgs_2.append({
            "url":nome_file,
            "tag": tag
            })
n_imgs = len(imgs_2)
   


if 'index_random' not in st.session_state:
    st.session_state.index_random = np.random.randint(0, n_imgs)
st.session_state.random_index = np.random.randint(0, n_imgs)


#if 'tags' not in st.session_state:
#    st.session_state.tags = {}

#login 
if 'utenti' not in st.session_state:
        st.session_state.utenti = {
            'abdel': {'eta': 25, 'citta': 'rabat','tags':{}},
            'davide': {'eta': 22, 'citta': 'gela','tags':{}},
            'marco': {'eta': 20, 'citta': 'torino','tags':{}}
        }
if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None
if 'fase' not in st.session_state:
    st.session_state.fase = 'login'


#logica likes
def cambia_valore(n):       
        tag_corrente = imgs_2[st.session_state.random_index]["tag"]
        corr =st.session_state.utente_corrente 
        if tag_corrente not in st.session_state.utenti[corr]["tags"]:
            st.session_state.utenti[corr]["tags"][tag_corrente] = {"like": 0,"dislike":0}
        if n ==1:
            st.session_state.utenti[corr]["tags"][tag_corrente]["like"] += 1
        else:
            st.session_state.utenti[corr]["tags"][tag_corrente]["dislike"] -= 1
        st.session_state.random_index = np.random.randint(0, n_imgs)

def grafico(df):
    #df_long.rename(columns={'index': 'Categoria'}, inplace=True)
    df_long = df.reset_index().melt(id_vars="index", var_name="Tipo", value_name="Valore")
    df_long.rename(columns={"index": "Tag"}, inplace=True)
    colori = alt.Scale(domain=['like', 'dislike'], range=["#3CA045", "#9B3244"])
    chart = alt.Chart(df_long).mark_bar().encode(
        x=alt.X('Tag:N', title=None),
        y=alt.Y('Valore:Q', stack='zero',title=None),
        color=alt.Color('Tipo:N', scale=colori, title=None),
        tooltip=['Tag', 'Tipo', 'Valore']
    ).configure_legend(
        orient='bottom',         
        direction='horizontal',
        title=None              
    )
    st.altair_chart(chart, use_container_width=True)
tab_home,tab_prova,tab_osservazioni = st.tabs(["home","Server","osservazioni"])


with tab_home:
    
    #@st.fragment()
    #def fun_incremento_3():  
    #fun_incremento_3()

    
    # Stato iniziale
    if 'temp_nome' not in st.session_state:
        st.session_state.temp_nome = ""
    if 'temp_eta' not in st.session_state:
        st.session_state.temp_eta = 0
    if 'temp_citta' not in st.session_state:
        st.session_state.temp_citta = ""

    if st.session_state.fase == 'login':
        st.title("Login")
    elif st.session_state.fase == 'registrazione':
        st.title("Registrazione")
    else:
        st.title("Home")

    #CALLBACK: login
    def esegui_login():
        nome = st.session_state.temp_nome.strip()
        if nome:
            if nome in st.session_state.utenti:
                st.session_state.utente_corrente = nome
                st.session_state.fase = 'home'
            else:
                st.session_state.utente_corrente = nome
                st.session_state.fase = 'registrazione'

    #CALLBACK: registrazione
    def esegui_registrazione():
        nome = st.session_state.utente_corrente
        if nome:
            st.session_state.utenti[nome] = {
                'eta': st.session_state.temp_eta,
                'citta': st.session_state.temp_citta,
                'tags':{}
            }
            st.session_state.fase = 'home'

    def esegui_logout():
        #logica logout 
        st.session_state.fase = 'login'
        st.session_state.utente_corrente = None
        st.session_state.temp_nome = ""
        st.session_state.temp_eta = 0
        st.session_state.temp_citta = ""

    #LOGIN
    if st.session_state.fase == 'login':
        st.text_input("Inserisci il tuo nome:", key="temp_nome")
        st.button("Login", on_click=esegui_login)

    #REGISTRAZIONE
    elif st.session_state.fase == 'registrazione':
        st.write(f"Benvenuto **{st.session_state.utente_corrente}**, completa la registrazione:")
        st.number_input("Età:", min_value=0, key="temp_eta")
        st.text_input("Città:", key="temp_citta")
        st.button("Registrati", on_click=esegui_registrazione)

    #HOME
    elif st.session_state.fase == 'home':
        nome = st.session_state.utente_corrente
        utente = st.session_state.utenti.get(nome, {})
        col1,col2,col3 = st.columns([1,2,1])
        with col1:
            st.success(f"Benvenuto {nome} !")
        with col3:
            logout = st.button("Logout",on_click=esegui_logout)
        #st.write(f"Età: {utente.get('eta')}")
        #st.write(f"Città: {utente.get('citta')}")

        @st.fragment()
        def fun_incremento_2():
            col1, col2, col3 = st.columns([1, 2, 1])  
            with col2:
                st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
            #st.write(imgs_2[st.session_state.random_index]["tag"])
            col1,col2,col3 = st.columns([3,1,4])
            with col2:
                decremento2 = st.button("👎",on_click= cambia_valore,args=(-1,))
            with col3:
                incremento2 = st.button("👍",on_click=  cambia_valore,args=(1,))
            st.divider()
            # clonne imagini 
            col1,col2,col3 = st.columns([2,1,2])
            with col1:
                st.image(os.path.join(os.getcwd(),"static","bici_6.jpg"))
                st.image(os.path.join(os.getcwd(),"static","bici_6.jpg"))
            with col2:
                st.write(1)
            with col3:
                st.image(os.path.join(os.getcwd(),"static","bici_6.jpg"))
                st.image(os.path.join(os.getcwd(),"static","bici_6.jpg"))

            #grafico
            col1,col2,col3 = st.columns([1,4,1])
            with col2:
                chart_data = pd.DataFrame.from_dict(st.session_state.utenti[st.session_state.utente_corrente]["tags"], orient='index')
                chart_data.rename(columns={'index': 'Tag'}, inplace=True)
                st.subheader("Like/Dislike")

                if len(chart_data)==0:
                    st.subheader("Inizia a mettere Like/Dislike per vedere il grafico")
                else:
                    #st.bar_chart(chart_data)
                    df = chart_data
                    #print("df1: ",df)
                    grafico(df)
                    
                st.divider()
                dati = st.session_state.utenti[st.session_state.utente_corrente]
                ordinati = sorted(
                            dati['tags'].items(),
                            key=lambda item: (-(item[1]['like'] - item[1]['dislike']), item[1]['like'])
                        )
                st.write(ordinati)
                st.divider()
        fun_incremento_2() 

        @st.fragment()
        def fun_gellery():
            col1,col2,col3 = st.columns([1,1,1])
            with col1:
                selected_image = image_select(
                    label="Clicca su un'immagine",
                    images=[
                        "static/citta_1.jpg",
                        "static/citta_2.jpg",
                        "static/citta_3.jpg",
                    ],
                    #captions=["Città 1", "Città 2", "Città 3"],
                )
                if selected_image:
                    st.write("Hai selezionato:", selected_image)
                    
               
                #st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
                st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
            with col2:
                st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
                st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
            with col3:
                st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
                st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))

        if False:
            fun_gellery()

with tab_prova:
    #import random
    st.title("🧠 Il Feed Non È Tuo")
    st.subheader("Simula come un algoritmo decide cosa vedrai")

    st.markdown("""
    Ogni scelta che fai insegna qualcosa all’algoritmo. Più interagisci, più il tuo feed si trasforma — non sempre per il meglio.
    """)

    # Stato iniziale
    if "bias" not in st.session_state:
        st.session_state.bias = None
        st.session_state.counter = 0

    st.markdown("### Cosa ti interessa oggi?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌱 Ambiente"):
            st.session_state.bias = "ambiente"
            st.session_state.counter += 1
    with col2:
        if st.button("💣 Politica"):
            st.session_state.bias = "politica"
            st.session_state.counter += 1

    # Feed simulato
    if st.session_state.bias:
        st.markdown("---")
        st.markdown("### 🔁 Contenuti consigliati")

        base_content = {
            "ambiente": [
                "🐢 'Le tartarughe stanno scomparendo: è colpa tua?'",
                "🌍 'Il cambiamento climatico non aspetta: guarda questi dati'",
                "🚨 'Scienziati in allarme: soglia di CO₂ superata!'"
            ],
            "politica": [
                "🔥 'Questo politico sta distruggendo il paese – video shock!'",
                "🔊 'La verità che nessuno ti dice sulla riforma fiscale'",
                "📉 'Democrazia in pericolo? Ecco cosa sta succedendo'"
            ]
        }

        # Aumenta la radicalizzazione in base al numero di click
        intensity = min(st.session_state.counter, 3)
        content = base_content[st.session_state.bias][:intensity]

        for c in content:
            st.markdown(f"- {c}")

        st.markdown(f"> *Hai cliccato `{st.session_state.counter}` volte. Il tuo feed sta cambiando.*")

        if st.session_state.counter >= 3:
            st.warning("🔄 L’algoritmo ha imparato cosa ti prende… e ti mostra solo quello.")

    st.markdown("---")
    st.caption("Questo è un esempio semplificato. Nella realtà, ogni tocco, pausa e reazione modifica il tuo mondo digitale.")


       

#print(st.session_state.utenti)
#print(st.session_state.utente_corrente)
#print(st.session_state.fase)