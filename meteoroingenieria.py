import streamlit as st
import meteoromineriadatos as mineria_de_datos
import meteorodesarrollosoftware as software_ia
import meteoroflota as optimizacion_flota
import meteorocasos as casos_reales

# CONFIGURACIÓN DE PÁGINA (Asegura que el tema oscuro sea el default)
st.set_page_config(page_title="Meteoro-ingeniería", layout="wide")

# ESTILOS DE ALTO CONTRASTE (Cian sobre Fondo Oscuro)
st.markdown("""
    <style>
    /* Fondo oscuro para toda la aplicación */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Forzar color cian en todos los textos para que se vean en el celular */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown {
        color: #00d4ff !important;
    }

    /* Estilo para los botones de radio en el sidebar */
    .stRadio label {
        color: #00d4ff !important;
    }

    /* Ajuste para que el fondo del sidebar también sea oscuro */
    [data-testid="stSidebar"] {
        background-color: #161b22;
    }
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
    st.subheader("Hub de Control Estratégico")
    st.write("Bienvenido. La ingeniería de datos al servicio de su rentabilidad.")

elif menu == "Minería de Datos":
    mineria_de_datos.mostrar_metodologia()

elif menu == "Software e IA":
    software_ia.mostrar_curso_ia()

elif menu == "Optimización de Flota":
    optimizacion_flota.mostrar_optimizacion_flota()

elif menu == "Casos Reales":
    casos_reales.mostrar_casos_reales()