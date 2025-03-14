import streamlit as st

import streamlit as st

def run():
    st.subheader("Contatos")

    st.write("Meus meios de contato")

    # LinkedIn
    linkedin_url = "https://www.linkedin.com/in/richard-silva-murila-840472278/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24"/> LinkedIn: @Richard Silva Murila</a>', unsafe_allow_html=True)

    # Instagram
    instagram_url = "https://www.instagram.com/ri_silva._/"
    st.markdown(f'<a href="{instagram_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="24"/> Instagram: @ri_silva</a>', unsafe_allow_html=True)

    
    # WhatsApp
    whatsapp_url = "https://web.whatsapp.com/"
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="24"/> WhatsApp: (11) 941851926 </a>', unsafe_allow_html=True)

    # GitHub
    github_url = "https://github.com/richard251213/richard251213.github.io"
    st.markdown(f'<a href="{github_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="24"/> GitHub: @RichardSilvaMurila</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    run()