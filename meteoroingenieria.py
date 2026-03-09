import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Meteoro-ingeniería", layout="wide")

# 2. ESTILOS CSS (Restaurados y mejorados para visibilidad en móvil)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3 { color: #00d4ff !important; }
    
    /* Clase para que los títulos de servicios sean legibles en el celular */
    .modulo-inicio { 
        color: #00d4ff !important; 
        font-weight: bold; 
        margin-bottom: 10px;
        font-size: 1.5rem;
    }
    
    .nav-instruction { 
        background-color: #1e293b; 
        padding: 10px; 
        border-radius: 8px; 
        border: 1px solid #00d4ff; 
        color: #00d4ff; 
        font-weight: bold; 
        text-align: center;
        margin-bottom: 25px;
    }
    .philosophy-box { 
        background-color: #161b22; 
        padding: 25px; 
        border-radius: 15px; 
        border-left: 5px solid #00d4ff; 
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGACIÓN LATERAL
with st.sidebar:
    st.title("🚀 Navegación")
    menu = st.radio(
        "Seleccione un módulo:",
        ["Inicio", "Minería de Datos", "Software e IA", "Optimización de Flota", "Casos Reales"]
    )
    st.write("---")
    st.info("Meteoro-ingeniería: Transformando datos en activos estratégicos.")

# 4. LÓGICA DE MÓDULOS
if menu == "Inicio":
    st.title("Meteoro-ingeniería")
    
    st.markdown('<p class="nav-instruction">Explore los submódulos en el menú lateral para ver nuestra capacidad operativa.</p>', unsafe_allow_html=True)
    
    # Lista de servicios con color cian para legibilidad en móvil
    st.markdown("""
    <div style="margin-top: 20px;">
        <p class="modulo-inicio">🔹 Minería de Datos</p>
        <p class="modulo-inicio">🔹 Desarrollo de Software con IA</p>
        <p class="modulo-inicio">🔹 Optimización de Flota</p>
        <p class="modulo-inicio">🔹 Casos de Análisis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("""
    <div class="philosophy-box">
        <h3 style="margin-top:0;">Nuestra Filosofía</h3>
        <p>No solo solucionamos problemas técnicos; optimizamos flujos de capital. 
        Utilizamos tecnología de vanguardia para que su empresa sea una estructura 
        eficiente, rentable e indestructible.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Minería de Datos":
    st.title("📊 Minería de Datos")
    st.write("Análisis profundo para encontrar fugas de dinero y oportunidades de ahorro.")
    # Aquí puedes importar o llamar a tu lógica de minería

elif menu == "Software e IA":
    st.title("🤖 Desarrollo de Software e IA")
    st.write("Creamos herramientas a medida que automatizan decisiones complejas.")

elif menu == "Optimización de Flota":
    st.title("🚚 Optimización de Flota")
    st.write("Reducción de Downtime y gestión inteligente de mantenimiento.")

elif menu == "Casos Reales":
    st.title("📂 Casos Reales y Análisis")
    st.write("Evidencia de transformaciones logradas en el sector industrial.")