import streamlit as st
import os

import pandas as pd,numpy as np,matplotlib.pyplot as plt
import time
import glob
import altair as alt
import pydeck as pdk



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
   
if 'tags' not in st.session_state:
    st.session_state.tags = {}
if 'count2' not in st.session_state:
    st.session_state.count2 = 0

if 'index_random' not in st.session_state:
    st.session_state.index_random = np.random.randint(0, n_imgs)
st.session_state.random_index = np.random.randint(0, n_imgs)


#login 

if 'utenti' not in st.session_state:
        st.session_state.utenti = {
            'abdel': {'eta': 25, 'citta': 'torino'}
        }
if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None
if 'fase' not in st.session_state:
    st.session_state.fase = 'login'

    
#logica likes
def cambia_valore(n):       
        tag_corrente = imgs_2[st.session_state.random_index]["tag"]
        if tag_corrente not in st.session_state.tags:
            st.session_state.tags[tag_corrente] = {"like": 0,"dislike":0}
        if n ==1:
            st.session_state.tags[tag_corrente]["like"] += 1
        else:
            st.session_state.tags[tag_corrente]["dislike"] -= 1
        st.session_state.random_index = np.random.randint(0, n_imgs)

tab_home,tab_prova,tab_prova2,tab_prova3,tab_server = st.tabs(["home","prova","prova_2","prova_3","Server"])


with tab_home:
    st.write("hello word")
    
    st.title("text elements:")
    st.divider()

    st.title("titolo")
    st.header("header")
    st.subheader("sub header")
    st.markdown("questo è _markdown_")
    code_example = """
    def greet(name):
        printf('hello', name)
    """
    st.code(code_example,language = "python")

    st.divider()
    st.image(os.path.join(os.getcwd(),"static","montagna_1.jpg"),width=200)

    st.title("Chart demo")

    chart_data = pd.DataFrame(
        np.random.randn(10,3),columns=["A","B","C"]
    )

    st.subheader("Area Chart")
    st.area_chart(chart_data)

    st.subheader("Bar Chart")
    st.bar_chart(chart_data)

    st.subheader("Line Chart")
    st.line_chart(chart_data)

    st.subheader("Scatter Chart")
    scatter_data = pd.DataFrame({
        'x':np.random.randn(100),
        'y':np.random.randn(100),
        'z':np.random.randn(100)
    })

    st.scatter_chart(scatter_data)

    st.title("Prova Chart")
    #prova_chart_data =pd.DataFrame([1,2,3,4],columns=["A","B","C","D"])
    prova_chart_data =pd.DataFrame([1,2,3,4])
    st.bar_chart(prova_chart_data)

    st.subheader("Map")
    map_data = pd.DataFrame(
        np.random.randn(100,2)/[50,50]+[37.76,-122.4],
        columns=["lat","lon"]
    )

    st.map(map_data)


with tab_prova:
    imgs = sorted(glob.glob("static/*.jp*g"))
    st.title("prova")
    if 'count' not in st.session_state:
        st.session_state.count = 0
    #incremento = st.write(st.session_state.incremento)
    
    @st.fragment()
    def fun_incremento():
        col1,col2 = st.columns(2)
        with col1:
            decremento = st.button("decremento")
        with col2:
            incremento = st.button("incremento")
        if incremento and st.session_state.count<6:
            st.session_state.count += 1
            if st.session_state.count == 6:
                st.session_state.count=0
        if decremento and st.session_state.count>-1:
            st.session_state.count -= 1
            if st.session_state.count <= -1:
                st.session_state.count=5
        st.write("count: ",st.session_state.count)
        st.image(os.path.join(os.getcwd(),"",imgs[st.session_state.count]),width=200)
    fun_incremento()


with tab_prova2:
    st.title("prova2")



with tab_prova3:
    
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

    # CALLBACK: login
    def esegui_login():
        nome = st.session_state.temp_nome.strip()
        if nome:
            if nome in st.session_state.utenti:
                st.session_state.utente_corrente = nome
                st.session_state.fase = 'home'
            else:
                st.session_state.utente_corrente = nome
                st.session_state.fase = 'registrazione'

    # CALLBACK: registrazione
    def esegui_registrazione():
        nome = st.session_state.utente_corrente
        if nome:
            st.session_state.utenti[nome] = {
                'eta': st.session_state.temp_eta,
                'citta': st.session_state.temp_citta
            }
            st.session_state.fase = 'home'

    def esegui_logout():
        st.session_state.fase = 'login'
        st.session_state.utente_corrente = None
        st.session_state.temp_nome = ""
        st.session_state.temp_eta = 0
        st.session_state.temp_citta = ""

    # LOGIN
    if st.session_state.fase == 'login':
        st.text_input("Inserisci il tuo nome:", key="temp_nome")
        st.button("Login", on_click=esegui_login)

    # REGISTRAZIONE
    elif st.session_state.fase == 'registrazione':
        st.write(f"Benvenuto **{st.session_state.utente_corrente}**, completa la registrazione:")
        st.number_input("Età:", min_value=0, key="temp_eta")
        st.text_input("Città:", key="temp_citta")
        st.button("Registrati", on_click=esegui_registrazione)

    # HOME
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
            # Centrare l'immagine
            col1, col2, col3 = st.columns([1, 2, 1])  # colonne laterali più strette
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
                chart_data = pd.DataFrame.from_dict(st.session_state.tags, orient='index')
                chart_data.rename(columns={'index': 'Tag'}, inplace=True)
                st.subheader("Like/Dislike")

                if len(chart_data)==0:
                    st.subheader("nessun data, metti Like/Dislike per vedere il grafico")
                else:
                    #st.bar_chart(chart_data)
                    df = chart_data
                    df_long = df.reset_index().melt(id_vars='index', var_name='Tipo', value_name='Valore')
                    df_long.rename(columns={'index': 'Categoria'}, inplace=True)
                    colori_personalizzati = alt.Scale(domain=['like', 'dislike'], range=["#3CA045", "#9B3244"])
                    chart = alt.Chart(df_long).mark_bar().encode(
                        x=alt.X('Categoria:N', title=None),
                        y=alt.Y('Valore:Q', stack='zero', title=None),
                        color=alt.Color('Tipo:N', scale=colori_personalizzati, title=None)
                    ).configure_legend(
                        orient='bottom',         
                        direction='horizontal',
                        title=None              
                    )
                    st.altair_chart(chart, use_container_width=True)

        fun_incremento_2()  

       
with tab_server:
    dati_utenti = st.session_state.utenti
    citta_coords = {
        'milano': [45.4642, 9.19],
        'torino': [45.0703, 7.6869],
        'roma': [41.9028, 12.4964],
        'napoli': [40.8518, 14.2681],
        }
        
    data = []
    for nome, info in dati_utenti.items():
        lat, lon = citta_coords.get(info["citta"].lower(), [0, 0])
        data.append({
            "nome": nome,
            "eta": info["eta"],
            "citta": info["citta"].capitalize(),
            "lat": lat,
            "lon": lon
        })
    df = pd.DataFrame(data)
    st.title("Analisi Utenti Registrati")
        # 📊 Grafico distribuzione età
    st.subheader("Distribuzione età")
    st.bar_chart(df["eta"].value_counts().sort_index())

    # 🌍 Mappa utenti
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
                get_radius=50000,
                get_color='[200, 30, 0, 160]',
                pickable=True
            )
        ]
    ))

    # 🧑‍🤝‍🧑 Elenco utenti
    st.subheader("Utenti registrati")
    for _, row in df.iterrows():
        st.markdown(f"- **{row['nome']}** – {row['citta']}, {row['eta']} anni")



print(st.session_state.utenti)
print(st.session_state.utente_corrente)
print(st.session_state.fase)