import streamlit as st

st.set_page_config(
    page_title="Trafic cycliste à Paris",  # 🡐 C'est ça le titre de l'onglet navigateur
    page_icon="🚲",  # (optionnel) l'emoji devient l'icône dans l'onglet
    layout="wide"  # (optionnel) pour utiliser toute la largeur
)

# Barre latérale pour choisir la page
page = st.sidebar.radio("Choisir une page", ["Trafic Dataset", "Météo Dataset", "DataViz & Conclusion"])

# Affichage en fonction de la sélection
if page == "Trafic Dataset":
    st.markdown("<h1 style='text-align: center;'>🚲 Trafic Dataset</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Découverte et modifications du jeu de données initial</p>", unsafe_allow_html=True)
    st.components.v1.html(open("Trafic_vélo.html").read(), height=800, scrolling=True)

elif page == "Météo Dataset":
    st.markdown("<h1 style='text-align: center;'>☀️ Météo Dataset</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enrichissement avec des données météo</p>", unsafe_allow_html=True)
    st.components.v1.html(open("Meteo.html").read(), height=800, scrolling=True)

elif page == "DataViz & Conclusion":
    st.markdown("<h1 style='text-align: center;'>📈 DataViz</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Page 1 : Général∙ Page 2 : Observations périodiques ∙ Page 3 : Meteo</p>", unsafe_allow_html=True)
    st.components.v1.html(
    '''
    <iframe title="Trafic" width="100%" height="450" 
    src="https://app.powerbi.com/view?r=eyJrIjoiNGEyYzNmODgtM2QzZC00ZTFjLWJmMDMtM2NhNzEyYjU5ZDg3IiwidCI6IjhiNmJkNTdiLTk5ZjItNGU3My1hY2U5LWRlNmY3OGE5MDE1ZCJ9" 
    frameborder="0" allowFullScreen="true"></iframe>
    ''', height = 500, scrolling=True
)
    st.markdown("<h1 style='text-align: center;'>💬 Conclusion</h1>", unsafe_allow_html=True)
    st.write("Nous avons pu observer que le trafic cycliste à Paris est en constante augmentation, avec des pics notables pendant les mois d'été. Les données météo semblent également avoir un impact significatif sur le nombre de cyclistes.")
    st.write("Nous avons également remarqué que les jours de pluie, le trafic cycliste diminue considérablement, tandis que les jours ensoleillés voient une augmentation du nombre de cyclistes.")
    st.write("Ces informations peuvent être utiles pour les décideurs afin d'améliorer les infrastructures cyclables et de promouvoir l'utilisation du vélo comme moyen de transport durable.")
    

