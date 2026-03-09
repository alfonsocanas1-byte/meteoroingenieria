import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Meteoro-ingeniería", layout="wide")

# 2. ESTILOS CSS ACTUALIZADOS (Legibles en móvil y PC)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3 { color: #00d4ff !important; }
    
    /* Letras cian para que resalten sobre el fondo negro en el celular */
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

# 3. BARRA LATERAL (Necesaria para definir la variable 'menu')
with st.sidebar:
    st.image("https://www.meteoroingenieria.com/s/logo.png", width=200) # Cambia por tu logo real
    menu = st.radio("Navegación", ["Inicio", "Minería de Datos", "Software IA", "Optimización", "Casos"])

# 4. LÓGICA DE PÁGINAS
if menu == "Inicio":
    st.title("Meteoro-ingeniería")
    
    # Instrucción visual para el cliente
    st.markdown('<p class="nav-instruction">Utilice el menú lateral para explorar los servicios estratégicos</p>', unsafe_allow_html=True)
    
    # Subtítulos legibles en fondo oscuro
    st.markdown("""
    <div style="margin-top: 20px;">
        <p class="modulo-inicio">🔹 Minería de Datos</p>
        <p class="modulo-inicio">🔹 Desarrollo de Software con IA</p>
        <p class="modulo-inicio">🔹 Optimización de Flota</p>
        <p class="modulo-inicio">🔹 Casos de Análisis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Cuadro de filosofía del Imperio
    st.markdown("""
    <div class="philosophy-box">
        <h3 style="margin-top:0;">Estrategia y Resultados</h3>
        <p>Transformamos la complejidad operativa en activos digitales. 
        Nuestra ingeniería no solo soluciona problemas, crea ventajas competitivas indestructibles.</p>
    </div>
    """, unsafe_allow_html=True)

# Aquí puedes añadir los otros 'elif menu == ...' para los demás módulos