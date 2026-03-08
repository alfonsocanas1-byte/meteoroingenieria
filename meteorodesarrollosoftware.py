import streamlit as st

def mostrar_curso_ia():
    """
    Renderiza la sección del Curso de Ingeniería de Software con IA 
    con diseño de flujo paso a paso para el hub de Meteoro-ingeniería.
    """
    st.title("🚀 Curso de Ingeniería de Software con IA Gemini")
    
    # Enlace de contacto directo
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20el%20curso%20de%20IA"
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    st.markdown("---")
    st.subheader("Hoja de Ruta de Aprendizaje (Pasos de Ejecución)")

    # Estructura del curso (7 pilares sincronizados)
    puntos = [
        {"id": 1, "t": "Herramientas de desarrollo", "d": "Instalación y configuración técnica para empezar a construir soluciones reales."},
        {"id": 2, "t": "Arquitectura y diseño", "d": "Cómo estructurar un software para que sea indestructible y escalable."},
        {"id": 3, "t": "Redacción para IA (Prompt Engineering)", "d": "Dominio de Gemini para generar código base eficiente y profesional."},
        {"id": 4, "t": "Gestión de Repositorios (GitHub)", "d": "Control de versiones y despliegue seguro en la nube para tu negocio."},
        {"id": 5, "t": "Ecosistema Streamlit", "d": "Desarrollo de interfaces interactivas que transforman datos en decisiones."},
        {"id": 6, "t": "Ejecución y Pruebas", "d": "Puesta en marcha del software en entornos de producción reales."},
        {"id": 7, "t": "Ciclo de Mejoramiento Continuo", "d": "Uso de la IA para auditar, refactorizar y potenciar el software creado."}
    ]
    
    # Renderizado con flechas de flujo sincronizadas con Minería de Datos
    for i, p in enumerate(puntos):
        # Card del paso con borde resaltado
        st.markdown(f"""
            <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 2px solid #00d4ff; margin-bottom: 5px;">
                <div style="color: #00d4ff; font-weight: bold; font-size: 1.3rem; margin-bottom: 10px;">
                    PASO {p['id']}: {p['t']}
                </div>
                <p style="color: #ccd6f6; font-size: 1.05rem;">{p['d']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Dibujar flecha indicadora de flujo (excepto en el último paso)
        if i < len(puntos) - 1:
            st.markdown("""
                <div style="text-align: center; margin: 10px 0;">
                    <span style="color: #00d4ff; font-size: 2rem; font-weight: bold;">↓↓↓</span>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("Este mapa de aprendizaje está diseñado para que usted tome el control total de la creación de herramientas digitales para su empresa.")

if __name__ == "__main__":
    st.set_page_config(page_title="Curso Software IA | Meteoro", layout="wide")
    mostrar_curso_ia()