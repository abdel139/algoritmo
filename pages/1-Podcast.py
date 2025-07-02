import streamlit as st
st.title("🎙️ Il design invisibile del potere")
st.markdown("""
                <div style="width:100%; background:#f5f5f5;padding:20px;border-radius:10px;margin:10px 0;"> 
                Benvenuti al nostro podcast, dove esploriamo come le piattaforme digitali e i social media riescano a catturare la nostra attenzione e a generare meccanismi di dipendenza.
                </div>
                """,unsafe_allow_html=True)
    
st.markdown("""<div style="margin-top: 30px;"></div>""",unsafe_allow_html=True)
#st.audio("imgs_site/podcast.mp3", format="audio/mpeg", loop=True)
#with open("static/imgs_site/podcast.mp3", "rb") as audio_file:
#    st.audio(audio_file.read(), format="audio/mp3")

def fun(seconds):
    st.session_state.start_time = seconds



# Carica file audio
audio_file = open("static/imgs_site/podcast.mp3", "rb").read()

# Inizializza lo stato se non esiste
if "start_time" not in st.session_state:
    st.session_state.start_time = 0



# Esempio di timestamps: fittizi, puoi generarli in base alla tua traccia e trascrizione
timestamps = {
    "*1. Cos’è esattamente la gamification? E perché viene usata sempre di più nelle piattaforme digitali?*": 30,
    "*2. I social media sembrano giochi senza fine. Quali sono gli elementi di “gioco” nascosti nelle nostre app quotidiane?*": 62,
    "*3. Cosa succede nel nostro cervello quando riceviamo un like, una notifica, una reazione? Perché ci agganciano così tanto?*": 152,
    "*3. Cosa succede nel nostro cervello quando riceviamo un like, una notifica, una reazione? Perché ci agganciano così tanto?*": 2*60 + 32,
    "*4. Alcuni psicologi paragonano i social a slot machine: c’è davvero una dinamica di dipendenza dietro il design delle piattaforme?*": 3*60 + 35,
    "*5. Come cambia il nostro modo di vivere le relazioni, l’identità e l’autostima in un ambiente che ci misura a “punti”?*": 4*60+31,
    "*6. In che modo questi sistemi si collegano al modello economico delle piattaforme? Cosa guadagnano dal nostro coinvolgimento continuo?*": 5*60+38,
    "*7. La gamification può essere usata anche in ambiti meno visibili, come l’educazione o la politica. C’è un rischio di manipolazione sociale?*": 6*60+42,
    "*8. Se tutto è diventato un gioco… siamo ancora i giocatori, o siamo diventati i pedoni?*": 7*60+30,
}


# Riproduci audio dal tempo specificato
st.audio(
    audio_file,
    format="audio/mp3",
    start_time=st.session_state.start_time
)
st.markdown("""<div style="margin-top: 50px;"></div>""",unsafe_allow_html=True)
st.subheader("Le domande dell'episodio:")
# Crea pulsanti formattati come link
#for label, seconds in timestamps.items():
#    st.button(label, key=label,use_container_width=True,on_click=fun(seconds))
for label, seconds in timestamps.items():
    st.button(label, key=label, use_container_width=True, on_click=lambda s=seconds: fun(s))    
#st.experimental_rerun()  # Ricarica il player con start_time aggiornato
#st.markdown("""<div style="background:#eee; padding:5px 10px;border-radius: 10px;display:flex"><p style ="margin-right:10px">1 </p> <p>Cos’è esattamente la gamification? E perché viene usata sempre di più nelle piattaforme digitali?</p></div>""",unsafe_allow_html=True)
#st.markdown("""<div style="background:#eee; margin:10px 0; padding:5px 10px;border-radius: 10px;display:flex"><p style ="margin-right:10px">1 </p> <p>Cos’è esattamente la gamification? E perché viene usata sempre di più nelle piattaforme digitali?</p></div>""",unsafe_allow_html=True)
#st.markdown("*1. Cos’è esattamente la gamification? E perché viene usata sempre di più nelle piattaforme digitali?*")
#st.markdown("*2. I social media sembrano giochi senza fine. Quali sono gli elementi di “gioco” nascosti nelle nostre app quotidiane?*")
#st.markdown("*3. Cosa succede nel nostro cervello quando riceviamo un like, una notifica, una reazione? Perché ci agganciano così tanto?*")
#st.markdown("*4. Alcuni psicologi paragonano i social a slot machine: c’è davvero una dinamica di dipendenza dietro il design delle piattaforme?*")
#st.markdown("*5. Come cambia il nostro modo di vivere le relazioni, l’identità e l’autostima in un ambiente che ci misura a “punti”?*")
#st.markdown("*6. In che modo questi sistemi si collegano al modello economico delle piattaforme? Cosa guadagnano dal nostro coinvolgimento continuo?*")
#st.markdown("*7. La gamification può essere usata anche in ambiti meno visibili, come l’educazione o la politica. C’è un rischio di manipolazione sociale?*")
#st.markdown("*8. Se tutto è diventato un gioco… siamo ancora i giocatori, o siamo diventati i pedoni?*")