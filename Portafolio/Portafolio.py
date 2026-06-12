import streamlit as st

st.title("Portafolio de proyetos")
st.header("Daniel Orias Rojas")
st.container(height=30, border=False)
st.subheader("**Proyecto:** :green[Color spectral matching]")
if st.button("Información del proyecto"):
    st.switch_page("pages/informacion_colorimetria.py")

st.link_button("Código del proyecto", "https://github.com")

st.link_button("Demo del proyecto", "https://github.com")
