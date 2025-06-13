import streamlit as st
import os
import base64
#from streamlit_javascript import st_javascript
from datetime import datetime
#import streamlit.components.v1 as components

#from streamlit_js_eval import streamlit_js_eval
import platform
import matplotlib.pyplot as plt

def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
#st.title("Home")
img_base64 = get_image_base64("./static/imgs_site/img1.jpg")
home_titolo = "Dentro l'Agoritmo"
home_caption = "Scopri come i social decidono cosa vedi. Un viaggio interattivo nel cuore degli algoritmi che modellano la tua bacheca."

st.markdown(f"""
            <div style = "
            position:relative; 
            over-flow:hidden;
            border-radius: 10px;
            display: flex;
            flex-direction: row;
            justify-content: space-around;
            margin-bottom : 100px;
            border-radius:20px;
            overflow:hidden;
            ">
            <div style= "background: rgba(255, 255, 255, 0.4); 
  backdrop-filter: blur(8px); 
  -webkit-backdrop-filter: blur(8px);padding: 10px 40px ;position:absolute;top:50%;left:50%; transform:translate(-50%,-50%); text-align:center; border-radius: 10px;color:#000">
            <h3> {home_titolo} </h3>
            <p> {home_caption}</p>
            </div>
            <img style="width:100%;" style="border-radius:10px;" src="data:image/jpeg;base64,{img_base64}" alt="img" with="100">
            </div>
            """, unsafe_allow_html=True)

#video_file = open('./static/imgs_site/scrolling_video.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

#img_url0 = "./static/img2.avif"
#img_url = os.path.join(os.getcwd(),"static/imgs_site","bici_1.jpg")
#st.write(img_url)


st.subheader("""Ogni giorno trascorriamo ore su piattaforme digitali. Ci sembrano libere, aperte, personalizzate. Ma siamo sicuri che lo siano davvero?""")
col1,col2 = st.columns([1,1])
with col1:
    #st.title("col1")
    st.write(""" Dietro ogni like, ogni suggerimento, ogni notifica… c’è un algoritmo.E questi algoritmi non sono neutri. In questo sito vi portiamo dentro il cuore delle piattaforme digitali per capire come funzionano, come ci influenzano… e perché tutto questo conta""")
with col2:
    st.image(os.path.join(os.getcwd(),"static","imgs_site/img2.jpg"))

#img_url0 = "./static/bici_1.jpg"
#img_url = os.path.join(os.getcwd(),"static","bici_1.jpg")



#now = datetime.now()
ora = "nessun dato"
Sistema = "nessun dato"
Python = "nessun dato"

if False:
    st.subheader("💡 Esempio pratico")
    if st.button("Test",use_container_width=True):
        now = datetime.now()
        ora = now.strftime("%Y-%m-%d %H:%M:%S")
        Sistema = f"{platform.system()} {platform.release()}"
        Python = platform.python_version()
        st.markdown(f"""
                <div style = "background :#ffffff11;
                padding: 10px; 
                border-radius: 10px;
                margin: 20px 0;
                ">
                <div style = "
                padding: 10px;  
                display: flex;
                flex-direction: column;
                justify-content: space-around
                ">
                <h4>📋 Informazioni raccolte:</h4>
                <p> 🕒 Data e ora: {ora}</p>
                <p> 🖥️ Sistema: {Sistema}</p>
                <p> 🐍 Python version: {Python}</p>
                <p style ='display:none; margin:0; flex:1'> , personalizzate. Ma siamo sicuri che lo siano davvero? Dietro ogni like, ogni sugge </p>
                <div style ="display:none; border-radius:10px; overflow: hidden">
                <img  src="data:image/jpeg;base64,{img_base64}" alt="img" width="100" height="120">
                </div>
                </div>
                </div>
                
                """, unsafe_allow_html=True)


    else: 
        st.info("Premi il pulsante per raccogliere informazioni.")

st.divider()
#with st.container():
#    st.markdown("---")  # linea di separazione
#    col1, col2 = st.columns([2, 1])  # testo largo, immagine stretta
#
#    with col1:
#        st.write("Dietro ogni like, ogni suggerimento, si nasconde un algoritmo.")
#
    #with col2:
    #    st.image(img_base64, width=100)


#st.markdown("## 💡 Come funziona l'algoritmo")
#imp ----------------------

#imp ----------------------
# Inizializza lo stato
if "click_counts" not in st.session_state:
    st.session_state.click_counts = {
        "ambiente": 0,
        "politica": 0,
        "salute": 0,
        "sport": 0,
        "finanza": 0
    }

# Contenuti base per categoria
base_content = {
    "ambiente": [
        "🌍 Il clima sta collassando",
        "🔥 Incendi +300%",
        "♻️ La plastica che mangi"
    ],
    "politica": [
        "💥 Il politico ha mentito",
        "🧨 Crisi istituzionale",
        "📉 Collasso in arrivo"
    ],
    "salute": [
        "🥦 Cibi che avvelenano",
        "💊 Verità sui vaccini",
        "🧠 Danni della tecnologia"
    ],
    "sport": [
        "⚽ Arbitro corrotto?",
        "🏃 Tecniche segrete",
        "🥇 Scandali olimpici"
    ],
    "finanza": [
        "📈 Cripto esplosiva?",
        "💸 Chi controlla il tuo conto?",
        "🏦 Report che le banche odiano"
    ]
}


#---------------
# st.markdown("""
# > **What is a social media algorithm?**  
# > A social media algorithm is a set of rules and signals that rank content on a social platform. It organizes content on social feeds based on how likely each individual social media user is to like it and interact with it.  
# >  
# > A social algorithm’s purpose is to create a good user experience by making individual user’s feeds interesting and engaging. Algorithms are the reason why no two users will see exactly the same social content, even if they follow all the same accounts.  
# >  
# > *Fonte: [Hootsuite blog](https://blog.hootsuite.com/social-media-algorithm/)*
# """)

# Per aggiungere uno sfondo e bordo (più evidente), puoi usare HTML + CSS inline
# st.markdown("""
# <div style="border-left: 4px solid #888; padding: 15px; background-color: #f0f0f0; color: #555; font-style: italic; margin: 20px 0;">
# <p><strong>What is a social media algorithm?</strong><br>
# A social media algorithm is a set of rules and signals that rank content on a social platform. It organizes content on social feeds based on how likely each individual social media user is to like it and interact with it.<br><br>
# A social algorithm’s purpose is to create a good user experience by making individual user’s feeds interesting and engaging. Algorithms are the reason why no two users will see exactly the same social content, even if they follow all the same accounts.<br><br>
# <em>Fonte: <a href="https://blog.hootsuite.com/social-media-algorithm/" target="_blank">Hootsuite blog</a></em></p>
# </div>
# """, unsafe_allow_html=True)

st.markdown("""
<div style="border-left: 4px solid #888; padding: 15px; background-color: #f0f0f0; color: #555; font-style: italic; margin: 20px 0; max-width: 700px;">

<h3>Cos’è un algoritmo dei social media?</h3>
<p>È un insieme di regole e segnali che ordinano i contenuti su una piattaforma social, decidendo cosa mostrarti in base a quanto è probabile che ti piaccia o interagisca con essi.<br>
Lo scopo è offrire un’esperienza personalizzata e coinvolgente: per questo nessun feed è uguale a un altro, anche se segui gli stessi account.</p>

<h3>Perché sono importanti?</h3>
<p>Gli algoritmi filtrano l’enorme quantità di contenuti disponibili, influenzando chi vede cosa.<br>
Per i brand, questo significa che l’algoritmo determina la visibilità dei loro contenuti, sia tra i follower sia tra utenti nuovi.<br>
L’algoritmo impara rapidamente dai tuoi comportamenti (like, follow, interazioni) e ti propone sempre più contenuti simili a quelli che ti piacciono.</p>

<h3>Come funzionano?</h3>
<p>Le piattaforme come TikTok o Twitter (ora X) usano algoritmi basati su machine learning e “segnali di ranking” personalizzati, cioè parametri che valutano l’importanza di ogni contenuto per ogni utente in un dato momento.<br>
Questi segnali si basano sulle tue precedenti interazioni e hanno un effetto a catena che ti mantiene attivo sulla piattaforma proponendoti contenuti che probabilmente apprezzerai.</p>

<h3>In sintesi</h3>
<p>L’algoritmo scansiona tutti i contenuti disponibili, li valuta e li ordina per offrirti un feed fatto su misura per te.<br>
Nei prossimi approfondimenti si analizzeranno i segnali specifici per ogni piattaforma e come i creatori di contenuti possono “dialogare” con l’algoritmo per aumentare la loro visibilità.</p>

<p style="font-style: normal; font-size: 0.9em; color: #333; margin-top: 20px;">
Fonte: <a href="https://blog.hootsuite.com/social-media-algorithm/" target="_blank">Hootsuite blog</a>
</p>

</div>
""", unsafe_allow_html=True)

#st.image("https://about.fb.com/wp-content/uploads/2021/01/Facebook-News-Feed-ranking-algorithm-graphic_1200x628-1.jpg",
st.image("https://about.fb.com/wp-content/uploads/2021/01/NewsFeed_inline1.png?w=1024",
         caption="Schema dell’algoritmo Facebook (Fonte: Meta)",
         )


#------------------
# Titolo e introduzione
#st.title("🧠 Il Feed Non È Tuo")


st.divider()

st.subheader("💡 Esempio pratico")
st.subheader("Simula come un algoritmo decide cosa vedrai")

st.markdown("""
<div style="border-left: 6px solid #f63366; background-color: #eee; padding: 1rem; margin-bottom: 2rem;">
<strong>🎮 Esempio interattivo:</strong><br>
Questa sezione è una <em>dimostrazione pratica</em> di come i social ti mostrano solo ciò che attira la tua attenzione.
</div>
""", unsafe_allow_html=True)

# Pulsanti per interesse
st.markdown("### ❓ Cosa attira la tua attenzione oggi?")

col1, col2, col3, col4, col5 = st.columns(5)
if col1.button("🌱 Ambiente"):
    st.session_state.click_counts["ambiente"] += 1
if col2.button("💣 Politica"):
    st.session_state.click_counts["politica"] += 1
if col3.button("💪 Salute"):
    st.session_state.click_counts["salute"] += 1
if col4.button("⚽ Sport"):
    st.session_state.click_counts["sport"] += 1
if col5.button("💰 Finanza"):
    st.session_state.click_counts["finanza"] += 1

# Pulsante reset
if st.button("🔄 Reset algoritmo",use_container_width=True):
    for key in st.session_state.click_counts:
        st.session_state.click_counts[key] = 0

# Feed consigliato + contenuti nascosti
#st.markdown("---")
col_feed, col_hidden = st.columns(2)
ok = 1
with col_feed:
    st.markdown("##### 🔁 Contenuti consigliati dal tuo feed")
    for categoria, count in st.session_state.click_counts.items():
        if count > 0:
            st.markdown(f"**📌 {categoria.capitalize()}**")
            articoli = base_content[categoria][:min(count, len(base_content[categoria]))]
            for articolo in articoli:
                st.markdown(f"- {articolo}")
            ok = 0
        
    if ok==1:
        st.caption("Nessuna informazione disponibile")
        ok =0
    total = sum(st.session_state.click_counts.values())

with col_hidden:
    st.markdown("##### 🚫 Contenuti che non ti vengono mostrati")
    for categoria, count in st.session_state.click_counts.items():
        if count == 0:
            st.markdown(f"- *{base_content[categoria][0]}*")
if total==0:
    st.warning(f"Clicca su un pulsante.")
elif total<3:
    st.info(f"Continua ad interaggire")
else:
    st.success(f"Il feed si sta specializzando. Hai interagito {total} volte.")

# Grafico interattivo
col1,col2,col3 = st.columns([1,4,1])
with col2:
    st.markdown("---")
    st.markdown("### 📊 Evoluzione del tuo feed")

    fig, ax = plt.subplots()
    categorie = list(st.session_state.click_counts.keys())
    valori = list(st.session_state.click_counts.values())
    ax.bar(categorie, valori, color='skyblue')
    ax.set_ylabel("Interazioni")
    ax.set_title("Distribuzione dei contenuti nel feed")
    st.pyplot(fig)

# Footer
st.caption("🔍 Questa è una simulazione educativa. Nessun dato reale viene usato.")


# ------------------





# footer 
st.markdown("""<div style = "with:100%;margin:100px 0 0 0;"></div>""",unsafe_allow_html=True)
st.divider()
st.markdown("""
        <div style="width:100%; margin:20px 0; background:rgba(33, 195, 84, 0.1);color: rgb(23, 114, 51);padding:30px 20px; border-radius:10px;">
        <p>Per il corso di Internet e social media realizzato da:</p>
            <ul>
            <li style="list-style: circle;">Abdelkbir Berrahhal [s311085]</li>
            <li style="list-style: circle;">Davide  Cammalleri [s322575]</li>
            <li style="list-style: circle;">Filippo Errigo [s313197]</li>
            <li style="list-style: circle;">Aurora Strafallaci [s325070]</li>
            <li style="list-style: circle;">Angela Fargnoli [s321728]</li>
            </ul>
        </div>
        """,unsafe_allow_html=True)
#st.success("Per il corso di Internet e social media realizzato da: Abdelkbir, Davide, Filippo, Aurora, Angela ")
