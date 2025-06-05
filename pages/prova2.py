import streamlit as st
import matplotlib.pyplot as plt
st.markdown("""
## 📌 Come funziona l'algoritmo (dei social media)

Gli algoritmi dei social media **non mostrano i contenuti in ordine cronologico**, ma li selezionano in base a ciò che *pensano* ti terrà più tempo sulla piattaforma.

Ogni **like**, **clic**, **pausa** e **scroll** viene registrato: l’algoritmo **impara da te**, ma **non per te**.  
Il suo obiettivo non è informarti o arricchirti, ma **farti restare**, perché più tempo trascorso equivale a:

- più **dati**
- più **pubblicità**
- più **profitto**

Nel processo, i contenuti **più provocatori**, **polarizzanti** o **emotivamente forti** tendono a emergere, anche se non sono quelli che cercavi.

> Alla fine, l’algoritmo non riflette i tuoi interessi: **li influenza**.
""")
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
    if st.button("🌱 Ambiente2"):
        st.session_state.bias = "ambiente"
        st.session_state.counter += 1
with col2:
    if st.button("💣 Politica2"):
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
