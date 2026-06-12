import streamlit as st
#----------
with open("pages/InformacionColorimetria.pdf", "rb") as f:
    st.download_button(
        "Abrir PDF",
        f,
        file_name="InformacionColorimetria.pdf"
    )




#---------------
st.title("Información del Proyecto")
st.pdf("pages/InformacionColorimetria.pdf", height=800)
if st.button("⬅ Volver al Inicio"):
    st.switch_page("../Portafolio.py")
