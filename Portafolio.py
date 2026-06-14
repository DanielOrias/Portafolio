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
col_imagen, col_espacio = st.columns([1, 3])

with col_imagen:
    # 2. Pegamos aquí el enlace directo que nos dio Firebase Storage
    st.image(
        "https://i.postimg.cc/SsJ0M77q/Chat-GPT-Image-12-jun-2026-04-13-31-a-m.png", 
        use_container_width=True
    )

if st.button("**:black[Desarrollo Matemático]**", type="primary"):
    st.switch_page("pages/informacion_colorimetria.py")


st.link_button("**:blue[Código del proyecto]**", "https://github.com/DanielOrias/Color_spectral_matching")

st.link_button("Demo del proyecto", "https://github.com")
