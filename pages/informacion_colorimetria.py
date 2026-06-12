import streamlit as st
st.title("Información del Proyecto")
st.pdf("pages/InformacionColorimetria.pdf", height=800)
if st.button("⬅ Volver al Inicio"):
    st.switch_page("../Portafolio.py")
