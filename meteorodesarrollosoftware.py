import streamlit as st

def mostrar_curso_ia():
    """
    Renderiza la sección del Curso de Ingeniería de Software con IA 
    específicamente para el hub de Meteoro-ingeniería.
    """
    st.title("🚀 Curso de Ingeniería de Software con IA Gemini")
    
    # Enlace de contacto directo
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20el%20curso%20de%20IA"
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    # Estructura del curso (7 pilares de ejecución pura)
    puntos = [
        {"id": 1, "t": "Herramientas de desarrollo", "d": "Instalación y configuración técnica para empezar a construir soluciones reales."},
        {"id": 2, "t": "Arquitectura y diseño", "d": "Cómo estructurar un software para que sea indestructible y escalable."},
        {"id": 3, "t": "Redacción para IA (Prompt Engineering)", "d": "Dominio de Gemini para generar código base eficiente y profesional."},
        {"id": 4, "t": "Gestión de Repositorios (GitHub)", "d": "Control de versiones y despliegue seguro en la nube para tu negocio."},
        {"id": 5, "t": "Ecosistema Streamlit", "d": "Desarrollo de interfaces interactivas que transforman datos en decisiones."},
        {"id": 6, "t": "Ejecución y Pruebas", "d": "Puesta en marcha del software en entornos de producción reales."},
        {"id": 7, "t": "Ciclo de Mejoramiento Continuo", "d": "Uso de la IA para auditar, refactorizar y potenciar el software creado."}
    ]
    
    # Renderizado con la identidad visual de Meteoro-ingeniería
    for p in puntos:
        st.markdown(f"""
            <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px;">
                <div style="color: #00d4ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px;">
                    {p['id']}. {p['t']}
                </div>
                <p style="color: #ccd6f6;">{p['d']}</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    # Configuración de prueba independiente
    st.set_page_config(page_title="Curso Software IA | Meteoro", layout="wide")
    mostrar_curso_ia()