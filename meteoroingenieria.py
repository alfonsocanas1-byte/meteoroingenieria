import streamlit as st
import meteoromineriadatos as mineria
import meteorodesarrollosoftware as software
import meteoroflota as flota
import meteorocasos as casos

# Estilos obligatorios para que el celular se vea bien en todos los módulos
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3, p { color: #00d4ff !important; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    menu = st.radio("Navegación", ["Inicio", "Minería", "Software", "Flota", "Casos"])

if menu == "Inicio":
    st.title("Meteoro-ingeniería")
    st.write("Bienvenido al Hub Central.")

elif menu == "Minería":
    mineria.mostrar_metodologia() # Llama a la función dentro de tu otro archivo

elif menu == "Software":
    software.mostrar_curso_ia()

elif menu == "Flota":
    flota.mostrar_optimizacion_flota()

elif menu == "Casos":
    casos.mostrar_casos_reales()