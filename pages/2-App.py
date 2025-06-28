import streamlit as st
import os
import pandas as pd,numpy as np
import time
import glob
import altair as alt
import pydeck as pdk
import urllib.parse
#from streamlit_image_select import image_select
import random
from itertools import chain
from collections import defaultdict
import matplotlib.pyplot as plt
from collections import Counter
# !imp da fare -----------------------------
# todo: 
#sife bar app 
st.set_page_config(
    page_title="App",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "### per il progetto di *:blue[internet e social media]*, semplice dimostrazione su come gli algoritmi funzionano fornendo esempi iterativi",
        }
)
@st.cache_data
def carica_immagini_e_tag():
    immagini = []
    tag_set = set()
    for nome_file in os.listdir("static"):
        if nome_file.endswith((".jpg", ".png", ".jpeg")):
            tag = nome_file.split("_")[0]
            tag_set.add(tag)
            immagini.append({"url": nome_file, "tag": tag})
    return immagini, tag_set

iterazioni_per_apprendere=10
#imgs_2 = []
#tags = set()
#for nome_file in os.listdir("static"):
#    if nome_file.endswith((".jpg", ".png", ".jpeg")):
#        tag = nome_file.split("_")[0]
#        tags.add(tag)
#        imgs_2.append({
#            "url":nome_file,
#            "tag": tag
#            })
#n_imgs = len(imgs_2)
imgs_2, tags = carica_immagini_e_tag()
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
#st.session_state.random_index = np.random.randint(0, n_imgs)

def genera_indice_ponderato(immagini, punteggi):
    # 1. Mappa tag → lista indici
    mappa_tag_indici = defaultdict(list)
    for idx, elemento  in enumerate(immagini):
        tag = elemento['tag']
        mappa_tag_indici[tag].append(idx)

    # 2. Costruisci lista tag e pesi positivi
    tag_con_pesi = [(tag, max(score, 0)) for tag, score in punteggi.items()]
    tag_con_pesi = [item for item in tag_con_pesi if item[1] > 0]

    if not tag_con_pesi:
        #raise ValueError("Tutti i punteggi sono zero o negativi.")
        tag_scelto = random.choices(["auto","bici","citta","mare","montagna"], weights=[1,1,1,1,1], k=1)[0]

    else:
        tags, pesi = zip(*tag_con_pesi)
        # 3. Scegli un tag in base al peso
        tag_scelto = random.choices(tags, weights=pesi, k=1)[0]
    
    #print(tag_con_pesi)

    # 4. Scegli un indice casuale tra quelli associati a quel tag
    return random.choice(mappa_tag_indici[tag_scelto])


#genero dati random per i grafici
def random_data_graf():
    tag_interesse = random.choice(list(tags))
    tag_disinteresse = random.choice(list(tags))
    obj = {}
    for tag in tags:
        if(tag == tag_interesse):
            obj[tag] = {
                "like":random.randint(7,15),
                "dislike":-(random.randint(1,3)),}
        elif tag == tag_disinteresse:
            obj[tag] = {
                "like":random.randint(1,3),
                "dislike":-(random.randint(7,15)),}
        else:
            obj[tag] = {
                "like":random.randint(1,10),
                "dislike":-(random.randint(1,10)),
            }
    return obj
#login 
if 'utenti' not in st.session_state:
        st.session_state.utenti = {
            'abdel': {'eta': 25, 'citta': 'pescara','tags':random_data_graf(),'max':None,'min':None},
            'davide': {'eta': 21, 'citta': 'gela','tags':random_data_graf(),'max':None,'min':None},
            'filippo': {'eta': 20, 'citta': 'torino','tags':random_data_graf(),'max':None,'min':None},
            'aurora': {'eta': 20, 'citta': 'torino','tags':random_data_graf(),'max':None,'min':None},
            'angela': {'eta': 20, 'citta': 'torino','tags':random_data_graf(),'max':None,'min':None},
            'mattia': {'eta': 21, 'citta': 'taranto','tags':random_data_graf(),'max':None,'min':None},
            'saverio': {'eta': 23, 'citta': 'salerno','tags':random_data_graf(),'max':None,'min':None},
            'danny': {'eta': 23, 'citta': 'torino','tags':random_data_graf(),'max':None,'min':None},
            'gianmaria': {'eta': 20, 'citta': 'ancona','tags':random_data_graf(),'max':None,'min':None},
            'jacopo': {'eta': 20, 'citta': 'ancona','tags':random_data_graf(),'max':None,'min':None},
            'ettore': {'eta': 20, 'citta': 'sassari','tags':random_data_graf(),'max':None,'min':None},
        }
if 'utente_corrente' not in st.session_state:
    st.session_state.utente_corrente = None
if 'fase' not in st.session_state:
    st.session_state.fase = 'login'
if 'conteggio' not in st.session_state:
    st.session_state.conteggio = 0
valori_tags = {}
def calcola_diff_like_dislike(dati):
    for tag, valori in dati['tags'].items():
        valori_tags[tag] = valori['like'] + valori['dislike']
if st.session_state.utente_corrente and st.session_state.utente_corrente in st.session_state.utenti:
    calcola_diff_like_dislike(st.session_state.utenti[st.session_state.utente_corrente])

#print(imgs_2)
#logica likes
def cambia_valore(n): 
    st.session_state["conteggio"] +=1
    #print(st.session_state["conteggio"])      
    tag_corrente = imgs_2[st.session_state.random_index]["tag"]
    corr =st.session_state.utente_corrente 
    if tag_corrente not in st.session_state.utenti[corr]["tags"]:
        st.session_state.utenti[corr]["tags"][tag_corrente] = {"like": 0,"dislike":0}
    if n ==1:
        st.session_state.utenti[corr]["tags"][tag_corrente]["like"] += 1
    else:
        st.session_state.utenti[corr]["tags"][tag_corrente]["dislike"] -= 1
    if st.session_state["conteggio"] < iterazioni_per_apprendere:
        n = np.random.randint(0, n_imgs)
        if n == st.session_state.random_index:
            n = np.random.randint(0, n_imgs)
    else: 
        n = genera_indice_ponderato(imgs_2, valori_tags) 
        if n == st.session_state.random_index:  
            n = genera_indice_ponderato(imgs_2, valori_tags) 
    st.session_state.random_index = n
    
    #if(n != st.session_state.random_index):
    #    st.session_state.random_index = n
    #else:
    #    st.session_state.random_index = np.random.randint(0, n_imgs)
    calcola_diff_like_dislike(st.session_state.utenti[corr])
    


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

with st.sidebar:
     st.caption("""
### App page
Questa applicazione mostra cosa accade dietro le quinte dei social media.  
È suddivisa in **tre sezioni** principali: **App**, **Server** e **Filtraggio**.

- **📲App**
   🔐Esegui il login  con un nome,📝completa la registrazione, 🏠accedi alla home page  
  nella home page puoi interaggire con dei post
- **🗄️Server**  
  Raccoglie ed analizza i dati degli utenti.
- **🕵️‍♂️Filtaggio**  
   Mostra come chi gestisce la piattaforma può filtrare e utilizzare i dati per creare profili, influenzare l’esperienza d’uso o venderli a terzi.
""")


st.title("🧠 Simulatore Social Media")
tab_app,tab_server,tab_filtro = st.tabs(["App","Server","Filtraggio"])


with tab_app:
    # @st.fragment()
    #def fun_incremento_3():  
    # fun_incremento_3()
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
        st.subheader("🏠Home")

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
        st.session_state.conteggio = 0

    #LOGIN
    if st.session_state.fase == 'login':
        st.info("Inserisci un nome e prova l'applicazione.")
        st.text_input("Inserisci nome:", key="temp_nome")
        st.button("Login", on_click=esegui_login,use_container_width=True)

    #REGISTRAZIONE
    elif st.session_state.fase == 'registrazione':
        st.write(f"Benvenuto/a **{st.session_state.utente_corrente}**, completa la registrazione:")
        st.number_input("Età:", min_value=0, key="temp_eta")
        st.text_input("Città:", key="temp_citta")
        st.button("Registrati", on_click=esegui_registrazione,use_container_width=True)

    #HOME
    elif st.session_state.fase == 'home':
        if "random_index" not in st.session_state:
           st.session_state["random_index"] = 0 
        nome = st.session_state.utente_corrente
        utente = st.session_state.utenti.get(nome, {})
        col1,col2,col3 = st.columns([1,4,1])
        with col2:
            col1,col2 = st.columns([4,1])
            with col1:
                st.success(f"Benvenuto/a {nome} !")
            with col2:
                logout = st.button("Logout",on_click=esegui_logout,type="primary")
        #with col3:
        #st.write(f"Età: {utente.get('eta')}")
        #st.write(f"Città: {utente.get('citta')}")
        numeri_immagini_galleria = []
        immagini_galleria = 9
        #@st.fragment()
        def fun_incremento_2():
            col1, col2, col3 = st.columns([1, 4, 1])  
            with col2:
                #st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
                st.image(f'static/{imgs_2[st.session_state.random_index]["url"]}',caption=f"{imgs_2[st.session_state.random_index]['tag'].capitalize()}")
                col1,col2 = st.columns([1,1])
                with col1:
                    st.button("👍",on_click=  cambia_valore,args=(1,),use_container_width=True)
                with col2:
                    st.button("👎",on_click= cambia_valore,args=(-1,),use_container_width=True)
            
            if st.session_state["conteggio"] <iterazioni_per_apprendere:
                st.info(f"Fase di apprendimento, continua ad interaggire ..., il modello sta analizzando i tuoi interessi.")
                col1,col2 = st.columns([1,5])
                with col1:
                    st.write(f"Progresso: {st.session_state.conteggio}/{iterazioni_per_apprendere}")
                with col2:
                    st.progress((st.session_state.conteggio)/iterazioni_per_apprendere)
                st.caption("In questa fase, il modello genera immagini in modo casuale. Attraverso successive interazioni, il sistema applica algoritmi di apprendimento probabilistico per identificare pattern nei tuoi interessi visivi e ottimizzare la generazione delle immagini in base alle tue preferenze implicite.")
                with st.expander("Probabilità categorie:"):
                    st.write("Nella fase di appendimento tutte le categorie hanno la stessa probabilità di essere mostrate")
            else:
                st.success("Il modello ha completato la fase di apprendimento. A partire dai dati raccolti, applicherà criteri di similarità e ottimizzazione per selezionare e generare solo immagini coerenti con i tuoi interessi.")
                st.caption("Ora il modello inizierà a generare immagini in linea con i tuoi interessi, appresi durante le iterazioni precedenti. Le immagini mostrate da questo momento in poi saranno ottimizzate per rispecchiare al meglio le tue preferenze e gusti, così come inferiti dai dati raccolti.")
                with st.expander("Probabilità categorie:"):
                    i = 0
                    while i < immagini_galleria:
                        n = genera_indice_ponderato(imgs_2, valori_tags)
                        if n not in numeri_immagini_galleria:
                            numeri_immagini_galleria.append(n)
                            i+=1
                    #n_chiamate = 10
                    #risul = [genera_indice_ponderato(imgs_2, valori_tags) for _ in range(n_chiamate)]
                    risultati = [imgs_2[i]["tag"] for i in numeri_immagini_galleria]
                    conteggio = Counter(risultati)
                    etichette = list(conteggio.keys())
                    valori = list(conteggio.values())
                    # Grafico a torta
                    fig, ax = plt.subplots()
                    ax.pie(valori, labels=etichette, autopct='%1.1f%%', startangle=90)
                    ax.axis('equal')  # per rendere il cerchio perfetto
                    #col1,col2 = st.columns([1,3])
                    #with col1:
                    #    st.markdown(f"""<div style="margin-top:100px"></div>""",unsafe_allow_html=True)
                    #    # Mostra anche i numeri assoluti se vuoi
                    #    st.write("Frequenze assolute:", dict(conteggio))
                    #with col2:
                    st.pyplot(fig)
            #grafico
            col1,col2,col3 = st.columns([1,8,1])
            with col2:
                st.divider()
                chart_data = pd.DataFrame.from_dict(st.session_state.utenti[st.session_state.utente_corrente]["tags"], orient='index')
                chart_data.rename(columns={'index': 'Tag'}, inplace=True)
                with st.expander("Grafico Like/Dislike"):
                    if len(chart_data)==0:
                        st.subheader("Inizia a mettere Like/Dislike per vedere il grafico")
                    else:
                        #st.bar_chart(chart_data)
                        df = chart_data
                        #print("df1: ",df)
                        grafico(df)               
        fun_incremento_2() 
        st.header("Per te:")
        st.caption("""**Suggerimento:** prova a concentrarti su una sola categoria. In questo modo, il modello potrà affinare la sua comprensione dei tuoi interessi e generare immagini sempre più **pertinenti e specifiche** rispetto a quella tematica.
""")
        if st.session_state["conteggio"]>=iterazioni_per_apprendere:
            for i in range(0,immagini_galleria,3):
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.image(f"static/{imgs_2[numeri_immagini_galleria[i]]['url']}")
                with col2:
                    st.image(f"static/{imgs_2[numeri_immagini_galleria[i+1]]['url']}")
                with col3:
                    st.image(f"static/{imgs_2[numeri_immagini_galleria[i+2]]['url']}")
        else:
            st.info("Completa la fase di apprendimento per vedere i post suggeriti")
        #@st.fragment()
        #def fun_gellery(): 
        #   col1,col2,col3 = st.columns([1,1,1])
        #    with col1:
        #        
        #        selected_image = image_select(
        #            label="Clicca su un'immagine",
        #            images=[
        #                "static/citta_1.jpg",
        #                "static/citta_2.jpg",
        #                "static/citta_3.jpg",
        #            ],
        #            #captions=["Città 1", "Città 2", "Città 3"],
        #        )
        #        if selected_image:
        #            st.write("Hai selezionato:", selected_image)
        #            
        #       
        #        #st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
        #        st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
        #    with col2:
        #        st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
        #        st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
        #    with col3:
        #        st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))
        #        st.image(os.path.join(os.getcwd(),"static",imgs_2[st.session_state.random_index]["url"]))

        #if False:
        #    fun_gellery()
     
with tab_server:
    possibili_interessi = {
    "montagna": ["Escursionismo", "Campeggio", "Neve", "Natura", "Fauna selvatica", "Trekking", "Alpinismo"],
    "mare": ["Spiaggia", "Barca", "Surf", "Pesca", "Snorkeling", "Acqua salata", "Oceano", "Relax"],
    "citta": ["Architettura", "Vita notturna", "Cultura urbana", "Musei", "Trasporti", "Eventi", "Grattacieli"],
    "auto": ["Motori", "Auto sportive", "Guida autonoma", "Tecnologia", "Design", "Velocità", "Mobilità"],
    "bici": ["Ciclismo", "Ecologia", "Mobilità sostenibile", "Percorsi naturali", "Sport", "Salute", "Tempo libero"]
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
    st.subheader("📊 Analisi Utenti Registrati")
    st.markdown("""
                <div style="width:100%; background:#f5f5f5;padding:20px;border-radius:10px;margin:10px 0;"> 
                    In questa sezione sono raccolti tutti i dati degli utenti, divisi per: 
                    <ul style="margin:0;"> 
                        <li>Distribuzione d'età</li> 
                        <li>Città di residenza</li> 
                        <li>Grafici Like/Dislike</li> 
                    </ul>
                <div style="display: none;">
                    <pre>
                        <code> ciao</code>
                    </pre>
                </div>
                </div>
                """,unsafe_allow_html=True)
    df = pd.DataFrame(data)
    #Elenco utenti
    st.subheader("Utenti registrati")
    valori_utenti = [] 
    for i, row in df.iterrows():
        #st.markdown(f"- **{row['nome']}** – {row['citta']}, {row['eta']} anni")
        valori_utenti.append(f""" 
                    <div style="width:100%;display:flex;align-items:center;justify-content:center;margin:10px auto 15px"> 
                        <img src="https://cdn-icons-png.flaticon.com/512/1077/1077063.png " alt="Profile" width="35"> 
                    </div>
                    <div style="height:50%;display:flex;flex-direction:column;justify-content:space-around">
                        <div style="display:flex;justify-content:space-around"> 
                            <div>{row["nome"]}</div>
                            <div>{row["eta"]}</div>
                        </div>
                        <div style="width:100%;text-align:center;">{row["citta"]}</div>
                    </div>
                 """)
    cards_utenti=[]
    for i in range(len(valori_utenti)):
       cards_utenti.append(f"""<div style="width:100px;height:150px; background:#e4efff;border-radius:10px;margin:10px;padding:5px;">{valori_utenti[i]}</div>""")
    st.markdown(f"""
                <div style="display:flex; width:100%; justify-content:space-around; margin:30px 0;flex-wrap:wrap;">{"".join(cards_utenti)}</div>
                """,unsafe_allow_html=True)
        
    
    #st.subheader("dati utenti: ")
    with st.expander("Dati utenti (Json):",expanded=False):
        st.write(dati_utenti)
    
    st.subheader("Distribuzione età")
    st.bar_chart(df["eta"].value_counts().sort_index())
    if False:
        #Mappa utenti
        st.subheader("Mappa utenti per città")
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v10',
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

    
    #Grafici
    st.subheader("Grafici Like/Dislike per ogni utente")
    st.info("I dati vengono aggiornati solo dopo il logout dell'utente")

    col1, col2 = st.columns(2)
    colonne = [col1,col2]
    for idx, (utente, dati) in enumerate(st.session_state.utenti.items()):
        
        with colonne[idx % 2]:  # Alterna tra col1 e col2
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
                if count < count_min:
                    count_min = count
                    tag_min = tag
            if tags:
                st.session_state["utenti"][utente]["max"] = tag_max
                st.session_state["utenti"][utente]["min"] = tag_min
                st.write(f"#### {utente.capitalize()} ({dati['citta']}, {dati['eta']} anni)")
                df = pd.DataFrame.from_dict(tags, orient="index")
                grafico(df)
                st.success(f"**Interesse principale:** {(tag_max).capitalize()}")
                if tag_max in possibili_interessi:
                    with st.expander("**:green[Possibili interessi]**",):
                        for item in possibili_interessi[tag_max]:
                            st.write(item)
                        #st.write(f"**:green[Possibili interessi:]** \n" + " |".join(possibili_interessi[tag_max]))
                st.error(f"**Disinteresse principale:** {(tag_min).capitalize()}")
                if tag_min in possibili_interessi:
                     with st.expander("**:red[Possibili disinteressi]**"):
                        for item in possibili_interessi[tag_max]:
                            st.write(item)
                    #st.write(f"Possibili disinteressi: \n" + " | | ".join(possibili_interessi[tag_min]))
            else:
                st.info(f"L'utente {utente} non ha ancora nessun tag.")
            st.divider()     
with tab_filtro:
    utenti = st.session_state.get("utenti", {})
    st.subheader("🎯 Filtra gli utenti")
    
    #st.info("In questa sezione puoi filtrare tutti gli utenti, per età, citta, interesse e parole chiavi riferite agli interessi  ")
    st.markdown("""
                <div style="width:100%; background:#f5f5f5;padding:20px;border-radius:10px;margin:10px 0;"> 
                    In questa sezione puoi filtrare tutti gli utenti per: 
                    <ul style="margin:0;"> 
                        <li>Età</li> 
                        <li>Città</li> 
                        <li>Interesse</li> 
                        <li>Possibili interessi</li> 
                    </ul>
                <div style="display: none;">
                    <pre>
                        <code> ciao</code>
                    </pre>
                </div>
                </div>
                """,unsafe_allow_html=True)
    
    citta_disponibili = list({dati["citta"] for dati in utenti.values()})
    tag_possibili = list(set(tag for dati in utenti.values() for tag in dati["tags"]))
    st.subheader("🔍 Filtro utenti")
    eta_range = st.slider("🎂 Età", 1, 99, (18, 30))
    citta_selezionate = st.multiselect("🏙️ Città", citta_disponibili)
    interesse_principale = st.selectbox("🌟 Interesse principale", [""] + tag_possibili, index=0)
    #tag_specifici = st.multiselect("Filtra per tag specifici", tag_possibili)
    tutti_possibili = list(set(chain(*possibili_interessi.values())))
    possibile_interesse = st.selectbox("Filtra per parole chiave correlate", [""] + tutti_possibili, index=0)
    mostra_like_dislike = st.checkbox("📊 Mostra utenti con like/dislike",value=False)
    st.divider()

    # 🔍 FILTRAGGIO
    utenti_filtrati = {}
    for nome, dati in utenti.items():
        eta = dati["eta"]
        citta = dati["citta"]
        max_tag = dati.get("max", "")
        min_tag = dati.get("min", "")
        tags = dati.get("tags", {})
        
        if not (eta_range[0] <= eta <= eta_range[1]):
            continue
        if citta_selezionate and citta not in citta_selezionate:
            continue
        if interesse_principale and max_tag != interesse_principale:
            continue
        if possibile_interesse:
            interesse_utente = dati.get("max")
            parole_correlate = possibili_interessi.get(interesse_utente, [])
            if possibile_interesse not in parole_correlate:
                continue
        utenti_filtrati[nome] = dati

    st.markdown("## 📋 Risultati filtrati")

    if utenti_filtrati:
        for nome, dati in utenti_filtrati.items():
            st.markdown(f"**👤 {nome.capitalize()}** – {dati['eta']} anni, {dati['citta']}")
            st.success(f"✨ Interesse principale: {dati.get('max', 'N/A').capitalize()}")
            st.error(f"😑 Disinteresse principale: {dati.get('min', 'N/A').capitalize()}")
            if mostra_like_dislike:
                with st.expander("📈 Dettagli Like/Dislike"):
                    for tag, valori in dati["tags"].items():
                        st.write(f"🔹 {tag.capitalize()}    → 👍 {valori['like']} | 👎 {valori['dislike']}")
            st.divider()
    else:
        st.info("🙁 Nessun utente trovato con i criteri selezionati.")

    
#footer
st.markdown("""<div style="height:50px"/>""",unsafe_allow_html=True)
#st.divider()
st.warning("Nessun dato viene raccolto realmente, qualsiasi informazione inserita verrà cancellata non appena si chiude l'app")
#print(st.session_state.utenti)
#print(st.session_state.utente_corrente)
#print(st.session_state.fase)
