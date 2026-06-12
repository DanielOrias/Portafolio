import streamlit as st

st.title("Portafolio de proyetos")

st.header("Daniel Orias Rojas")

st.info("""Información de contacto:

**Correo electrónico:** danieloriasr@gmail.com

**Teléfono de contacto: +506 6481-4565**""")
st.markdown("#### LinkedIn:")
st.page_link("https://www.linkedin.com/in/daniel-orias-2a4779410", label="**:blue[Daniel Orias | LinkedIn.com]**")

st.container(height=30, border=False)


st.subheader("**Proyecto:** :green[Color spectral matching]")
if st.button("Información del proyecto"):
    st.switch_page("pages/informacion_colorimetria.py")


st.link_button("Código del proyecto", "https://github.com")


st.link_button("Demo del proyecto", "https://github.com")
