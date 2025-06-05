import streamlit as st
import os

import pandas as pd,numpy as np
#import matplotlib.pyplot as plt
import time
import glob
import altair as alt
import pydeck as pdk
import urllib.parse
from streamlit_image_select import image_select

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
   

province_coords = {
    'agrigento': [37.3000, 13.6000],
    'alessandria': [44.9167, 8.6167],
    'ancona': [43.6167, 13.5167],
    'aosta': [45.7333, 7.3167],
    'arezzo': [43.4667, 11.8833],
    'ascoli piceno': [42.8500, 13.5667],
    'asti': [44.8833, 8.2000],
    'avellino': [40.9167, 14.7833],
    'bari': [41.1167, 16.8667],
    'barletta-andria-trani': [41.3167, 16.2833],
    'belluno': [46.1333, 12.2167],
    'benevento': [41.1333, 14.7833],
    'bergamo': [45.7000, 9.6667],
    'biella': [45.5667, 8.0500],
    'bologna': [44.5000, 11.3333],
    'bolzano': [46.5000, 11.3500],
    'brescia': [45.5333, 10.2167],
    'brindisi': [40.6333, 17.9333],
    'cagliari': [39.2167, 9.1167],
    'caltanissetta': [37.4833, 14.0667],
    'campobasso': [41.5667, 14.6667],
    'caserta': [41.0667, 14.3333],
    'catania': [37.5000, 15.0833],
    'catanzaro': [38.9167, 16.6000],
    'chieti': [42.3500, 14.1667],
    'como': [45.8000, 9.0833],
    'cosenza': [39.3000, 16.2500],
    'cremona': [45.1333, 10.0167],
    'crotone': [39.0833, 17.1167],
    'cuneo': [44.3833, 7.5500],
    'enna': [37.5667, 14.2833],
    'ferrara': [44.8333, 11.6167],
    'firenze': [43.7667, 11.2500],
    'foggia': [41.4667, 15.5500],
    'forlì-cesena': [44.2167, 12.0500],
    'frosinone': [41.6333, 13.3500],
    'genova': [44.4167, 8.9333],
    'gorizia': [45.9500, 13.6167],
    'grosseto': [42.7667, 11.1167],
    'imperia': [43.8833, 8.0333],
    'isernia': [41.6000, 14.2333],
    'la spezia': [44.1167, 9.8167],
    'l\'aquila': [42.3500, 13.4000],
    'latina': [41.4667, 12.9000],
    'lecce': [40.3500, 18.1667],
    'lecco': [45.8500, 9.4000],
    'livorno': [43.5500, 10.3167],
    'lodi': [45.3167, 9.5000],
    'lucca': [43.8333, 10.5000],
    'macerata': [43.3000, 13.4500],
    'mantova': [45.1500, 10.7833],
    'massa-carrara': [44.0333, 10.1333],
    'matera': [40.6667, 16.6000],
    'messina': [38.2000, 15.5500],
    'milano': [45.4667, 9.1833],
    'modena': [44.6500, 10.9167],
    'monza e della brianza': [45.5833, 9.2667],
    'napoli': [40.8500, 14.2500],
    'novara': [45.4500, 8.6167],
    'nuoro': [40.3167, 9.3333],
    'oristano': [39.9000, 8.5833],
    'padova': [45.4000, 11.8833],
    'palermo': [38.1167, 13.3667],
    'parma': [44.8000, 10.3333],
    'pavia': [45.1833, 9.1500],
    'perugia': [43.1000, 12.3833],
    'pesaro e urbino': [43.9000, 12.9167],
    'pescara': [42.4667, 14.2167],
    'piacenza': [45.0500, 9.7000],
    'pisa': [43.7167, 10.4000],
    'pistoia': [43.9333, 10.9167],
    'pordenone': [45.9500, 12.6667],
    'potenza': [40.6333, 15.8000],
    'prato': [43.8833, 11.1000],
    'ragusa': [36.9333, 14.7167],
    'ravenna': [44.4167, 12.2000],
    'reggio calabria': [38.1167, 15.6500],
    'reggio emilia': [44.7000, 10.6333],
    'rieti': [42.4167, 12.8667],
    'rimini': [44.0500, 12.5667],
    'roma': [41.9000, 12.5000],
    'rovigo': [45.0667, 11.7833],
    'salerno': [40.6833, 14.7667],
    'sassari': [40.7333, 8.5667],
    'savona': [44.3000, 8.4833],
    'siena': [43.3167, 11.3333],
    'siracusa': [37.0667, 15.2833],
    'sondrio': [46.1667, 9.8667],
    'taranto': [40.4667, 17.2333],
    'teramo': [42.6667, 13.7000],
    'terni': [42.5667, 12.6500],
    'torino': [45.0667, 7.7000],
    'trapani': [38.0167, 12.5167],
    'trento': [46.0667, 11.1167],
    'treviso': [45.6667, 12.2500],
    'trieste': [45.6500, 13.7667],
    'udine': [46.0667, 13.2333],
    'varese': [45.8167, 8.8333],
    'venezia': [45.4333, 12.3333],
    'verbano-cusio-ossola': [45.9333, 8.5500],
    'vercelli': [45.3167, 8.4167],
    'verona': [45.4333, 10.9833],
    'vibo valentia': [38.6667, 16.1000],
    'vicenza': [45.5500, 11.5500],
    'viterbo': [42.4167, 12.1000],
    'rabat': [34.0209, -6.8416],
    'gela': [37.0736, 14.2406]
}

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
tab_home,tab_server = st.tabs(["home","Server"])


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
        #corr = st.session_state.utente_corrente
        #salvo i dati nell'diz
        #if corr not in st.session_state.likes_utenti:
        #    st.session_state.likes_utenti[corr] = {}
        #st.session_state.likes_utenti[corr]["eta"]=st.session_state.utenti[corr]["eta"]
        #st.session_state.likes_utenti[corr]["citta"]=st.session_state.utenti[corr]["citta"]
        #st.session_state.likes_utenti[corr]["tags"]=st.session_state.utenti[corr]["tags"]
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
                    # df_long = df.reset_index().melt(id_vars='index', var_name='Tipo', value_name='Valore')
                    # df_long.rename(columns={'index': 'Categoria'}, inplace=True)
                    # colori_personalizzati = alt.Scale(domain=['like', 'dislike'], range=["#3CA045", "#9B3244"])
                    # chart = alt.Chart(df_long).mark_bar().encode(
                    #     x=alt.X('Categoria:N', title=None),
                    #     y=alt.Y('Valore:Q', stack='zero', title=None),
                    #     color=alt.Color('Tipo:N', scale=colori_personalizzati, title=None)
                    # ).configure_legend(
                    #     orient='bottom',         
                    #     direction='horizontal',
                    #     title=None              
                    # )
                    # st.altair_chart(chart, use_container_width=True)
                st.divider()
                st.write(st.session_state.utente_corrente)
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

        if True:
            fun_gellery()


       
with tab_server:
    possibili_interessi = {
        "montagna":["Natura","Animale"],
        "mare":["Acqua","Lago","Pesce"],
        "citta":["Strada","Edificio"],
        "car":["Tecnologia"],
        #"bici":["Tecnologia"]
    }
    dati_utenti = st.session_state.utenti
    data = []
    for nome, info in dati_utenti.items():
        lat, lon = province_coords.get(info["citta"].lower(), [0, 0])
        data.append({
            "nome": nome,
            "eta": info["eta"],
            "citta": info["citta"].capitalize(),
            "lat": lat,
            "lon": lon
        })
    st.write("dati utenti: ")
    st.write(dati_utenti)
    df = pd.DataFrame(data)
    st.title("Analisi Utenti Registrati")
    st.subheader("Distribuzione età")
    st.bar_chart(df["eta"].value_counts().sort_index())

    #Mappa utenti
    st.subheader("Mappa utenti per città")
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=df["lat"].mean(),
            longitude=df["lon"].mean(),
            zoom=5
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position='[lon, lat]',
                get_radius=30000,
                get_color='[200, 30, 0, 160]',
                pickable=True
            )
        ]
    ))

    #Elenco utenti
    st.subheader("Utenti registrati")
    for _, row in df.iterrows():
        st.markdown(f"- **{row['nome']}** – {row['citta']}, {row['eta']} anni")
    st.subheader("Grafici Like/Dislike per ogni utente")
    st.write("i dati vengono aggiornati solo dopo il logout dell'utente")
    
    for utente, dati in st.session_state.utenti.items():
        tags = dati.get("tags", {})
        count_max = -100
        count_min = 100
        tag_max = ''
        tag_min = ''
        for tag in tags:
            count = tags[tag]["like"] + tags[tag]["dislike"]
            if count > count_max:
                count_max = count
                tag_max = tag
            elif count < count_min:
                count_min = count
                tag_min = tag
        if tags:
            st.write(f"Utente: {utente} ({dati['citta']}, {dati['eta']} anni)")
            df = pd.DataFrame.from_dict(tags, orient="index")
            #print("df2: ",df)
            grafico(df)
            st.success(f"Interesse principale: {(tag_max).capitalize()}")
            if tag_max in possibili_interessi:
                st.write(f"Possibili interessi: \n"+" | | ".join(possibili_interessi[tag_max]))
            st.error(f"Disinteresse principale: {(tag_min).capitalize()}")
            if tag_min in possibili_interessi:
                st.write(f"Possibili disinteressi: \n"+" | | ".join(possibili_interessi[tag_min]))
        else:
            st.info(f"L'utente {utente} non ha ancora nessun tag.")
        st.divider()
            

#print(st.session_state.utenti)
#print(st.session_state.utente_corrente)
#print(st.session_state.fase)