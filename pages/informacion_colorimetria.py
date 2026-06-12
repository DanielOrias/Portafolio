import streamlit as st
#---------
st.title("Información del Proyecto")
st.pdf("pages/InformacionColorimetria.pdf", height=800)

#---------
with open("pages/InformacionColorimetria.pdf", "rb") as f:
    st.download_button(
        "Descargar PDF",
        f,
        file_name="InformacionColorimetria.pdf"
    )
#-------------
if st.button("⬅ Volver al Inicio"):
    st.link_button("Volver al inicio", "https://poratafoliodanielorias.streamlit.app/")
