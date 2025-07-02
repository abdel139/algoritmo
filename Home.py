import streamlit as st
import os
import base64
#from streamlit_javascript import st_javascript
from datetime import datetime
#import streamlit.components.v1 as components
import plotly.graph_objects as go
#from streamlit_js_eval import streamlit_js_eval
import platform
import matplotlib.pyplot as plt
import random

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "### per il progetto di *:blue[internet e social media]*, semplice dimostrazione su come gli algoritmi funzionano fornendo esempi iterativi",
        }
)

def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    


#st.title("Home")
first_home = get_image_base64("./static/imgs_site/img1.jpg")
home_titolo = "Dentro l'Algoritmo"
home_caption = "Scopri come i social decidono cosa vedi. Un viaggio interattivo nel cuore degli algoritmi che modellano la tua bacheca."

#st.sidebar.title("Home page")
#st.sidebar.caption("""Questa pagina introduce in modo semplice e intuitivo il funzionamento degli algoritmi sui social media. È pensata per farti capire come i contenuti vengono selezionati, ordinati e mostrati in base a determinati criteri invisibili ma molto influenti. """)
with st.sidebar:
    st.caption("""
### Home page

Questa pagina introduce in modo semplice e interattivo il funzionamento degli algoritmi sui social media.

**Contenuti principali:**

- **🕹️ Introduzione agli algoritmi**  
  Una spiegazione chiara e accessibile su cosa sono gli algoritmi sociali.
- **🧠 Economia dell'Attenzione e Social Media**  
  cos'è e quali sono le sue conseguenze.
- **🫧 Bias e bolle informative**  
  Come ci finiamo senza accorgercene.

- **💡Esempi pratici**  
 per ogni sezione sono disponibili diverse simulazioni con cui si può interagire.


""")


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
              -webkit-backdrop-filter: blur(8px);padding: 10px 40px ;position:absolute;top:50%;left:50%; transform:translate(-50%,-50%); text-align:center; border-radius: 10px;color:#111">
            <h3> {home_titolo} </h3>
            <p> {home_caption}</p>
            </div>
            <img style="width:100%;" style="border-radius:10px;" src="data:image/jpeg;base64,{first_home}" alt="img" with="100">
            </div>
            """, unsafe_allow_html=True)

#video_file = open('./static/imgs_site/scrolling_video.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

#img_url0 = "./static/img2.avif"
#img_url = os.path.join(os.getcwd(),"static/imgs_site","bici_1.jpg")
#st.write(img_url)


st.header(""" 📱 Social media: chi guida chi?""")
#st.subheader("""Ogni giorno trascorriamo ore su piattaforme digitali. Ci sembrano libere, aperte, personalizzate. Ma siamo sicuri che lo siano davvero?""")
col1,col2 = st.columns([1,1])
with col1:
    #st.title("col1")
    #st.write(""" Dietro ogni like, ogni suggerimento, ogni notifica… c’è un algoritmo.E questi algoritmi non sono neutri. In questo sito vi portiamo dentro il cuore delle piattaforme digitali per capire come funzionano, come ci influenzano… e perché tutto questo conta""")
    st.markdown("""Ogni giorno passiamo ore su piattaforme che sembrano libere e personalizzate.\n
Ma dietro ogni like o notifica c’è un algoritmo che decide cosa vediamo.
Questi sistemi non sono neutri: influenzano i nostri pensieri, emozioni e scelte.
In questo sito vi mostriamo come funzionano.""")
with col2:
    #st.image(os.path.join(os.getcwd(),"static","imgs_site/img2.jpg"))
    st.image("static/imgs_site/img2.jpg")



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


st.markdown("""
<div style="border-left: 4px solid #888; padding: 15px; background-color: rgb(239,239,239); color: rgb(51,51,51); font-style: italic; margin: 20px 0; max-width: 700px;">

<h4><span style="color:#666">Partiamo da:</span> cos’è un algoritmo dei social media?</h4>
<p>È un insieme di regole e segnali che ordinano i contenuti su una piattaforma social, decidendo cosa mostrarti in base a quanto è probabile che ti piaccia o interagisca con essi.<br>
Lo scopo è offrire un’esperienza personalizzata e coinvolgente: per questo nessun feed è uguale a un altro, anche se segui gli stessi account.</p>

<h4>Perché sono importanti?</h4>
<p>Gli algoritmi filtrano l’enorme quantità di contenuti disponibili, influenzando chi vede cosa.<br>
Per i brand, questo significa che l’algoritmo determina la visibilità dei loro contenuti, sia tra i follower sia tra utenti nuovi.<br>
L’algoritmo impara rapidamente dai tuoi comportamenti (like, follow, interazioni) e ti propone sempre più contenuti simili a quelli che ti piacciono.</p>

<h4>Come funzionano?</h4>
<p>Le piattaforme come TikTok o Twitter (ora X) usano algoritmi basati su machine learning e “segnali di ranking” personalizzati, cioè parametri che valutano l’importanza di ogni contenuto per ogni utente in un dato momento.<br>
Questi segnali si basano sulle tue precedenti interazioni e hanno un effetto a catena che ti mantiene attivo sulla piattaforma proponendoti contenuti che probabilmente apprezzerai.</p>

<h4>In sintesi</h4>
<p>L’algoritmo scansiona tutti i contenuti disponibili, li valuta e li ordina per offrirti un feed fatto su misura per te.<br>
Nei prossimi approfondimenti si analizzeranno i segnali specifici per ogni piattaforma e come i creatori di contenuti possono “dialogare” con l’algoritmo per aumentare la loro visibilità.</p>
<!--
<p style="font-style: normal; font-size: 0.9em; color: #333; margin-top: 20px;">
Fonte: <a href="https://blog.hootsuite.com/social-media-algorithm/" target="_blank">Hootsuite blog</a>
</p> -->

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
st.subheader("🕹️ Simula come un algoritmo decide cosa vedrai")

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
with st.expander("📊 Evoluzione del tuo feed:"):
    col1,col2,col3 = st.columns([1,4,1])
    with col2:
        st.markdown("### 📊 Evoluzione del tuo feed")
        fig, ax = plt.subplots()
        categorie = list(st.session_state.click_counts.keys())
        valori = list(st.session_state.click_counts.values())
        ax.bar(categorie, valori, color='skyblue')
        ax.set_ylabel("Interazioni")
        ax.set_title("Distribuzione dei contenuti nel feed")
        st.pyplot(fig)
        st.write("quiiiiiiiiiiiii")

# Footer
st.caption("🔍 Questa è una simulazione educativa. Nessun dato reale viene usato.")


# ------------------



#st.markdown("""<div style="margin-top: 50px;"></div>""",unsafe_allow_html=True)
st.divider()
st.header("👀Economia dell'Attenzione e Social Media")
st.markdown("""<div style="margin-top: 20px;"></div>""",unsafe_allow_html=True)
#st.subheader("Scopri come gli algoritmi influenzano ciò che vedi ogni giorno online")


col1,col2 = st.columns([4,2])
with col1:
    st.markdown("""
                Dopo aver compreso come funziona un algoritmo, è importante capire **perché opera in questo modo**.  
                Il suo scopo non è solo mostrarti ciò che ti piace, ma soprattutto **mantenerti il più a lungo possibile sulla piattaforma**.  
                Ogni contenuto, notifica o suggerimento è progettato per **catturare la tua attenzione** e spingerti a restare, scrollare e interagire sempre di più.  
                Questo ci porta a parlare di un concetto chiave: l’**economia dell’attenzione**, che spiega come **l’attenzione degli utenti sia diventata una risorsa preziosa e limitata**.  
                In un mondo di contenuti infiniti, trattenere la tua attenzione è l’**obiettivo principale dei social media e degli algoritmi che li governano**.
                """)
with col2:
    st.image("static/imgs_site/scrolling_youth.jpg")


st.markdown(f"""
<div style="border-left: 4px solid #888; padding: 15px; background-color: rgb(239,239,239); color: rgb(51,51,51); font-style: italic; margin: 20px 0; max-width: 700px;">

<h4>Cos’è l’economia dell’attenzione?</h4>
<p>È un modello economico in cui l’attenzione delle persone diventa una risorsa scarsa e preziosa. In un mondo dove i contenuti sono infiniti ma il tempo è limitato, ciò che cattura e trattiene la tua attenzione ha più valore.</p>

<h4>Che legame ha con gli algoritmi?</h4>
<p>Gli algoritmi dei social media sono strumenti centrali dell’economia dell’attenzione: selezionano i contenuti che massimizzano il tempo che trascorri sulla piattaforma, spingendoti a interagire ancora di più.<br>
Più resti connesso, più dati generi, più pubblicità possono esserti mostrate — e più profitti ottiene la piattaforma.</p>

<h4>Quali sono le conseguenze?</h4>
<p>Questo meccanismo può portare a <strong>feed altamente personalizzati ma anche limitanti</strong>, che ti mostrano sempre contenuti simili, creando una “bolla”.<br>
Può anche incentivare contenuti estremi, emozionali o controversi, perché attirano più clic e interazioni.</p>

<h4>In sintesi</h4>
<p>L’economia dell’attenzione spiega perché piattaforme e algoritmi non sono neutrali: competono per il tuo tempo e progettano esperienze che ti spingano a tornare continuamente, spesso a scapito della varietà o della qualità dei contenuti.</p>
 
<!--<p style="font-style: normal; font-size: 0.9em; color: #333; margin-top: 20px;">
Fonte: <a href="https://www.nytimes.com/interactive/2022/11/22/opinion/social-media-attention-economy.html" target="_blank">New York Times – Attention Economy</a>
</p>-->

</div>
""", unsafe_allow_html=True)


st.subheader("💡 Esempio pratico")
st.subheader("🧠 Economia dell’attenzione: cosa scegli di guardare?")

st.markdown("""
<div style="border-left: 6px solid #f63366; background-color: #eee; padding: 1rem; margin-bottom: 2rem;">
<strong>🎮 Simulazione:</strong><br>
Hai solo <strong>3 click</strong> da spendere. Scegli i contenuti che attirano di più la tua attenzione.<br>
Al termine vedrai quali tipi di contenuti "vincono" e perché.
</div>
""", unsafe_allow_html=True)

def reset_e_a():
    st.session_state.attention_clicks = 0
    for key in st.session_state.content_scores:
        st.session_state.content_scores[key] = 0
# Inizializzazione stato
if "attention_clicks" not in st.session_state:
    st.session_state.attention_clicks = 0
    st.session_state.content_scores = {
        "scandalo": 0,
        "dramma": 0,
        "calma": 0,
        "approfondimento": 0,
        "disinformazione": 0
    }

# Contenuti da visualizzare (casuali a ogni refresh)
contenuti_possibili = [
    ("scandalo", "💥 Scandalo clamoroso al governo!"),
    ("dramma", "😱 Video choc: crolla ponte in diretta"),
    ("calma", "🌅 Meditazione e benessere in 5 minuti"),
    ("approfondimento", "📚 Perché la crisi climatica è complessa"),
    ("disinformazione", "🧪 Il vaccino cambia il tuo DNA?"),
]

contenuti_mostrati = random.sample(contenuti_possibili, 5)

# Mostra contenuti e pulsanti
for categoria, titolo in contenuti_mostrati:
    if st.session_state.attention_clicks < 3:
        if st.button(titolo):
            st.session_state.content_scores[categoria] += 1
            st.session_state.attention_clicks += 1

# Quando i click sono esauriti
if st.session_state.attention_clicks >= 3:
    st.divider()
    st.markdown("### 📊 Risultato della tua attenzione")
    
    sorted_scores = sorted(st.session_state.content_scores.items(), key=lambda x: -x[1])
    for cat, score in sorted_scores:
        if score > 0:
            st.markdown(f"**{cat.capitalize()}**: {score} clic")

    st.info("⚠️ I contenuti più drammatici o scioccanti tendono a vincere l’attenzione.")

    with st.expander("Perché succede?"):
        st.markdown("""
        Le piattaforme privilegiano i contenuti che ottengono più click, anche se sono estremi o scorretti.
        Questo può alimentare ansia, disinformazione o polarizzazione.
        """)

    st.button("🔄 Riprova",on_click=reset_e_a,use_container_width=True)
        

# Footer
st.caption("🔍 Simulazione semplificata: in un vero feed, queste dinamiche avvengono continuamente.")



#with st.expander("Cos'è l'economia dell'attenzione?"):
#    st.markdown("""
#    Le piattaforme digitali competono per una cosa: **la tua attenzione**. Ogni notifica, like o video suggerito ha un obiettivo: **trattenerti**.  
#    Scopri come il tuo comportamento viene trasformato in dati e monetizzato.
#    """)
#    st.image("static/imgs_site/attention_market.jpg", caption="La tua attenzione vale più di quanto pensi")
#    st.radio("Sai quanto tempo passi al giorno sui social?", ["Meno di 1 ora", "1-3 ore", "Più di 4 ore"])

st.markdown("""<div style = "with:100%;margin:50px 0 0 0;"></div>""",unsafe_allow_html=True)
st.subheader("🎯 Bias e bolle informative")
st.image("static/imgs_site/filter_bubble.jpg")
st.markdown("""
Gli algoritmi ti mostrano contenuti **simili ai tuoi gusti**.  
Risultato? Vedi sempre le **stesse idee**, e ti allontani da chi la pensa diversamente.
""")

st.markdown("""
<div style="border-left: 4px solid #888; padding: 15px; background-color: rgb(239,239,239); color: rgb(51,51,51); font-style: italic; margin: 20px 0; max-width: 700px;">

<h4>🫧 Come finiamo nella nostra bolla (senza accorgercene)</h4>

<p>Quando interagisci con un contenuto — un like, un commento, una visualizzazione — l’algoritmo registra il tuo interesse e te ne propone di simili.</p>

<p>Nel tempo, questo comportamento ti porta dentro una <strong>bolla informativa</strong>: un ambiente digitale dove leggi solo opinioni simili alle tue, e raramente ti imbatti in punti di vista diversi.</p>

<p>Il fenomeno si amplifica con i <strong>bias cognitivi</strong>, cioè scorciatoie mentali che usiamo per semplificare la realtà. Uno dei più comuni è il <em>confirmation bias</em>: tendiamo a cercare e ricordare solo le informazioni che confermano le nostre idee.</p>

<p>Il risultato? Una visione sempre più polarizzata e chiusa del mondo, dove si fatica a dialogare con chi la pensa diversamente.</p>
<!--
<p style="font-style: normal; font-size: 0.9em; color: #333; margin-top: 20px;">
Fonte: <a href="https://www.scientificamerican.com/article/the-delusion-of-consensus-in-the-facebook-news-feed/" target="_blank">Scientific American</a>
</p> -->

</div>
""", unsafe_allow_html=True)

st.success("“Più ci assomiglia, più lo vediamo. Più lo vediamo, più ci convince.”")


st.subheader("💡 Esempio pratico")
st.subheader("🧠 Prova ad uscire dalla bolla")
st.markdown("""
<div style="border-left: 6px solid #f63366; background-color: #eee; padding: 1rem; margin-bottom: 2rem;">
<strong>🎯 Simulazione:</strong><br>
Cambia categoria, cambia tema... ma i contenuti si assomigliano sempre.<br>
Riuscirai davvero a uscire dalla tua bolla informativa?
</div>
""", unsafe_allow_html=True)

# Setup iniziale
if "bubble_bias" not in st.session_state:
    st.session_state.bubble_bias = {
        "focus": "politica",  # bias dominante iniziale
        "clicks": 0
    }

# Contenuti per ogni categoria (visti da una sola prospettiva)
bubble_content = {
    "politica": [
        "💣 Tutti mentono, ma alcuni lo fanno meglio",
        "⚖️ Sistema corrotto, niente cambierà",
        "📉 La democrazia è un'illusione"
    ],
    "ambiente": [
        "🌍 Le élite usano il clima per controllarci",
        "🔥 Panico climatico? È tutto pilotato",
        "💨 Chi guadagna davvero con la green economy"
    ],
    "salute": [
        "💊 Verità nascoste dalle industrie",
        "🧠 Esperti manipolano i dati",
        "🥦 Naturalismo estremo come unica salvezza"
    ],
    "finanza": [
        "💰 Le banche vogliono controllarti",
        "📉 Il crollo è vicino (di nuovo)",
        "🏦 Inflazione? Qualcuno ci guadagna sempre"
    ],
    "tecnologia": [
        "🤖 Gli algoritmi decidono per te",
        "📱 Tutto ciò che fai è tracciato",
        "🧠 Dipendenza digitale creata a tavolino"
    ]
}

st.markdown("#### 🔍 Scegli una categoria")

col1, col2, col3, col4, col5 = st.columns(5)
clicked = None
if col1.button("💣 Politica",key="politica2"):
    clicked = "politica"
if col2.button("🌱 Ambiente",key="ambiente2"):
    clicked = "ambiente"
if col3.button("💊 Salute",key="salute2"):
    clicked = "salute"
if col4.button("💰 Finanza",key="finanza2"):
    clicked = "finanza"
if col5.button("📱 Tecnologia"):
    clicked = "tecnologia"

if clicked:
    st.session_state.bubble_bias["clicks"] += 1
    # Non mostra davvero contenuti nuovi della categoria scelta, ma filtra sempre dalla "focus"
    focus = st.session_state.bubble_bias["focus"]
    contenuti = random.sample(bubble_content[focus], 2)
    
    st.markdown("#### 🔁 Contenuti mostrati")
    for c in contenuti:
        st.markdown(f"- {c}")

    if clicked != focus and st.session_state.bubble_bias["clicks"] >= 4:
        # Dopo vari tentativi, la bolla può "cedere"
        st.success("✨ Hai rotto la bolla! Stai iniziando a vedere altri punti di vista.")
        st.session_state.bubble_bias["focus"] = clicked
        st.session_state.bubble_bias["clicks"] = 0
    elif clicked != focus:
        st.info("🙈 La bolla resiste. Prova ancora...")
    else:
        st.caption("📌 Algoritmo rafforzato: conferma la tua visione.")

# Reset
if st.button("🔄 Reset simulazione",use_container_width=True):
    st.session_state.bubble_bias = {"focus": "politica", "clicks": 0}




st.subheader("📊 Quanto sei nella bolla?")
st.markdown("Ogni clic che conferma il tuo bias rafforza la bolla. Cambiare categoria più volte può ridurla.")

clicks = st.session_state.bubble_bias["clicks"]
max_clicks = 6
livello = min(clicks / max_clicks, 1.0)

#fig, ax = plt.subplots()
#ax.barh(["Bolla attuale"], [livello], color='crimson' if livello >= 0.7 else 'orange' if livello >= 0.3 else 'green')
#ax.set_xlim(0, 1)
#ax.set_title("📈 Livello di intrappolamento nella bolla")
#ax.set_xlabel("0 = mente aperta • 1 = feed polarizzato")
#st.pyplot(fig)


plt.style.use("seaborn-v0_8-darkgrid")  # Stile coerente

fig, ax = plt.subplots(figsize=(6, 3.5))

# Colore dinamico in base al livello
color = 'crimson' if livello >= 0.7 else 'orange' if livello >= 0.3 else 'green'

ax.barh(["Bolla attuale"], [livello], color=color)

ax.set_xlim(0, 1)
ax.set_xlabel("0 = mente aperta • 1 = feed polarizzato", fontsize=12)
ax.set_title("📈 Livello di intrappolamento nella bolla", fontsize=14, weight='bold')

ax.grid(alpha=0.3)

st.pyplot(fig)

with st.expander("🆚 Feed distorto vs Feed bilanciato",expanded=True):
    st.markdown("Ecco un esempio di come lo stesso argomento può essere presentato in due modi diversi:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔴 Feed distorto")
        st.markdown("- 💣 *“Il politico ha mentito di nuovo”*")
        st.markdown("- 💥 *“Sistema marcio, rivoluzione ora”*")
        st.markdown("- 🧨 *“Tutti contro di noi”*")

    with col2:
        st.markdown("### 🟢 Feed bilanciato")
        st.markdown("- 🧭 *“Analisi critica sulle recenti decisioni politiche”*")
        st.markdown("- 📊 *“Pro e contro delle nuove riforme”*")
        st.markdown("- 🧠 *“Voci a confronto: opinioni diverse a confronto”*")

    st.caption("🔍 Questo mostra come il framing e la selezione delle parole cambiano la percezione.")

st.subheader("🎮 Gamification e ricompense invisibili")
st.image("static/imgs_site/gamification.jpg")

st.markdown("""
Gli algoritmi non ti mostrano solo contenuti: ti **premiano** per restare attivo.  
Like, badge, notifiche, cuori, suoni... tutto è progettato per **attivare il cervello** come in un videogioco.
""")

st.markdown("""
<div style="border-left: 4px solid #888; padding: 15px; background-color: rgb(239,239,239); color: rgb(51,51,51); font-style: italic; margin: 20px 0; max-width: 700px;">

<h4>🔁 Il ciclo della ricompensa (senza accorgertene)</h4>

<p>Ogni like ricevuto, ogni nuova visualizzazione o notifica è una piccola <strong>ricompensa</strong>.</p>

<p>Come in un videogioco, queste micro-ricompense ti spingono a continuare: controlli se qualcuno ha risposto, pubblichi di nuovo, torni sull'app.</p>

<p>Si attivano circuiti dopaminici: è lo stesso meccanismo che ci fa tornare su una slot machine o su un videogioco.</p>

<p>Il risultato? Resti connesso più a lungo, ma spesso non sai neanche <strong>perché</strong>.</p>

</div>
""", unsafe_allow_html=True)

st.success("“Ogni notifica è come un premio a sorpresa. E il cervello ama le sorprese.”")


st.subheader("💸 Monetizzazione indiretta")
st.image("static/imgs_site/data_monetization.jpg")

st.markdown("""
I social non ti chiedono soldi. Ma non sono gratis.  
Paghi con delle risorse molto più preziosa: i tuoi **dati** e la **tua attenzione**.
""")

st.markdown("""
<div style="border-left: 4px solid #444; padding: 15px; background-color: #f0f0f0; color: #333; font-style: italic; margin: 20px 0; max-width: 700px;">

<h4>📊 Se non paghi il prodotto, *sei* il prodotto</h4>

<p>Ogni volta che scorri, clicchi, resti su un post... i tuoi dati vengono raccolti.</p>

<p>Le piattaforme li usano per vendere <strong>pubblicità mirata</strong>: più sanno di te, più gli inserzionisti pagano.</p>

<p>Non vendono il tuo nome, ma la tua attenzione, i tuoi interessi, i tuoi clic. Tutto viene <strong>monetizzato</strong>.</p>

<p>Il contenuto che vedi non è neutrale: è ottimizzato per farti rimanere lì — e guadagnare di più.</p>

</div>
""", unsafe_allow_html=True)

st.warning("“Il vero business dei social non sei tu. È il tuo tempo.”")


st.subheader("💡 Esempio pratico")
st.subheader("🎮 Simulazione: quanto resisti alle notifiche?")
st.markdown("""
<div style="border-left: 6px solid #f63366; background-color: #eee; padding: 1rem; margin-bottom: 2rem;">
<strong>🎯 Simulazione:</strong><br>
Clicca il pulsante <span style="color:#888">(Controlla notifica)</span> per vedere cosa succede...  <br>
Le notifiche sono casuali, imprevedibili... come nei social.
</div>
""", unsafe_allow_html=True)

# Stato iniziale
if "clicks" not in st.session_state:
    st.session_state.clicks = 0
    st.session_state.rewards = 0
    st.session_state.reward_history = []

# Azione utente
if st.button("🔔 Controlla notifiche",use_container_width=True):
    st.session_state.clicks += 1
    # 30% di probabilità di ricevere una "ricompensa"
    if random.random() < 0.3:
        st.session_state.rewards += 1
        feedback = random.choice([
            "👍 Hai ricevuto un like!",
            "💬 Qualcuno ha commentato il tuo post!",
            "🔥 Nuovi follower!",
            "🏆 Badge sbloccato!",
            "🔁 Il tuo contenuto è stato condiviso!"
        ])
        st.success(feedback)
    else:
        st.info("Nessuna notifica... ma forse al prossimo clic?")

    # Storico per grafico
    st.session_state.reward_history.append(st.session_state.rewards)

# Grafico
#st.markdown("#### 📊 Ricompense ricevute nel tempo")
#fig, ax = plt.subplots()
#ax.plot(st.session_state.reward_history, marker="o", color="orange")
#ax.set_xlabel("Clic eseguiti")
#ax.set_ylabel("Ricompense accumulate")
#ax.set_title("Andamento delle ricompense")
#st.pyplot(fig)


fig = go.Figure()
fig.add_trace(go.Scatter(
    y=st.session_state.reward_history,
    x=list(range(1, len(st.session_state.reward_history)+1)),
    mode='lines+markers',
    line=dict(color='deeppink', width=3),
    marker=dict(size=10, symbol="star", color='orange'),
    name='Ricompense'
))

fig.update_layout(
    title="📊 Ricompense ricevute nel tempo",
    xaxis_title="Clic eseguiti",
    yaxis_title="Ricompense totali",
    template="plotly_white",
    plot_bgcolor='rgba(250,250,250,0.95)',
    paper_bgcolor='rgba(255,255,255,0.9)',
    font=dict(size=14),
    height=400
)

st.plotly_chart(fig, use_container_width=True)


# Analisi comportamentale
if st.session_state.clicks >= 10:
    if st.session_state.rewards < 3:
        st.warning("🧠 Ti stai sforzando per ottenere un premio... ma ne ricevi pochi. Questo ti motiva ancora di più.")
    elif st.session_state.rewards >= 6:
        st.success("🎯 Sei stato premiato spesso: il tuo cervello ora vuole ancora più notifiche.")
    else:
        st.info("🔁 Ricompense intermittenti = comportamento rinforzato. il che ti porta a riprovare ogni volta")

def reset_sim():
    st.session_state.clicks = 0
    st.session_state.rewards = 0
    st.session_state.reward_history = []
    print("res")

# Reset
st.button("🔄 Reset simulazione",key="res_2",on_click= reset_sim,use_container_width=True)
   
with st.expander("🧠 Perché funziona così?"):
    st.markdown("""
    I social usano meccanismi simili alle **slot machine**: non sai quando riceverai una ricompensa, ma il fatto che **a volte succeda** ti spinge a provarci ancora.

    Questo si chiama **rinforzo intermittente**: il cervello rilascia dopamina quando ottieni un like, un badge o una notifica, anche se non sempre accade.

    Il risultato? Ti trovi a cliccare compulsivamente, anche senza un reale bisogno.
    """)


st.markdown("""<div style = "with:100%;margin:100px 0 0 0;"></div>""",unsafe_allow_html=True)
st.markdown("### 🎧 Non perderti il nostro podcast e l'App")
st.markdown("""<div style = "with:100%;margin:50px 0 0 0;"></div>""",unsafe_allow_html=True)

col1,col2 = st.columns(2)
with col1:
    st.image("static/imgs_site/podcast_img.jpg")
with col2:
    st.image("static/imgs_site/app_img.png")
col1,col2 = st.columns(2)
with col1:
    st.page_link("pages/1-Podcast.py",label="Guarda il podcast",icon="🎧")
with col2:
    st.page_link("pages/2-App.py",label="Prova la nostra app",icon="📱")



# footer 
st.markdown("""<div style = "with:100%;margin:100px 0 0 0;"></div>""",unsafe_allow_html=True)
st.divider()

st.markdown("### 👨‍🎓 Il nostro team")
st.write("""
Siamo un gruppo di studenti appassionati di tecnologia e comunicazione.
per il progetto del corso di **:green[Internet e Social Media]**, abbiamo scelto queto tema a noi particolarmente caro,
Lo abbiamo fatto con l’obiettivo di promuovere un **uso consapevole dei social**, affinché siano strumenti da utilizzare e non trappole da cui farsi usare.
""")
st.markdown(f"""
        <div style="width:100%; margin:20px 0; background:rgba(33, 195, 84, 0.1);color: rgb(23, 114, 51);padding:30px 20px; border-radius:10px;">
        <p>Membri del gruppo:</p>
            <ul>
            <li style="list-style: circle;"><p style="width: 150px; display:inline-block;margin:0">Berrahhal Abdelkbir</p> [s311085]</li>
            <li style="list-style: circle;"><p style="width: 150px; display:inline-block;margin:0">Cammalleri Davide</p> [s322575]</li>
            <li style="list-style: circle;"><p style="width: 150px; display:inline-block;margin:0">Errigo Filippo </p> [s313197]</li>
            <li style="list-style: circle;"><p style="width: 150px; display:inline-block;margin:0">Fargnoli Angela</p> [s321728]</li>
            <li style="list-style: circle;"><p style="width: 150px; display:inline-block;margin:0">Strafallaci Aurora </p> [s325070]</li>
            </ul>
            <p>Numero gruppo: 8</p>
        </div>
        """,unsafe_allow_html=True)
#st.success("Per il corso di Internet e social media realizzato da: Abdelkbir, Davide, Filippo, Aurora, Angela ")
