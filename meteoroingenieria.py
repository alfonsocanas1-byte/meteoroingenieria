# --- ESTILOS CSS ACTUALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3 { color: #00d4ff !important; }
    
    /* Ajuste para que los módulos sean legibles en fondo oscuro (Móvil y PC) */
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

# --- DENTRO DE IF MENU == "INICIO" ---
if menu == "Inicio":
    st.title("Meteoro-ingeniería")
    
    # Subtítulos con el nuevo estilo legible
    st.markdown("""
    <div style="margin-top: 20px;">
        <p class="modulo-inicio">🔹 Minería de Datos</p>
        <p class="modulo-inicio">🔹 Desarrollo de Software con IA</p>
        <p class="modulo-inicio">🔹 Optimización de Flota</p>
        <p class="modulo-inicio">🔹 Casos de Análisis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")