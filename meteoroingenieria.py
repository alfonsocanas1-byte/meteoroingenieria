import streamlit as st
# Importamos con nombres que respetan la identidad de cada módulo
import meteoromineriadatos as mineria_de_datos
import meteorodesarrollosoftware as software_ia
import meteoroflota as optimizacion_flota
import meteorocasos as casos_reales

# Estilos para asegurar legibilidad cian en celular y PC
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3, p { color: #00d4ff !important; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("🚀 Navegación")
    menu = st.radio(
        "Seleccione un módulo estratégico:",
        ["Inicio", "Minería de Datos", "Software e IA", "Optimización de Flota", "Casos Reales"]
    )

if menu == "Inicio":
    st.title("Meteoro-ingeniería")
    st.write("Bienvenido al Hub de Control Estratégico.")

elif menu == "Minería de Datos":
    mineria_de_datos.mostrar_metodologia()

elif menu == "Software e IA":
    software_ia.mostrar_curso_ia()

elif menu == "Optimización de Flota":
    optimizacion_flota.mostrar_optimizacion_flota()

elif menu == "Casos Reales":
    casos_reales.mostrar_casos_reales()