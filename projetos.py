import streamlit as st

def run():
    st.subheader("Projetos")
    st.write("Abaixo você encontra o link para o vídeo explicativo do meu projeto")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
             <iframe width="350" height="197" src="https://www.youtube.com/embed/kII6r_bT8Zg?si=XX2zeAN-yfA68NRv" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      
        """, unsafe_allow_html=True)
