import streamlit as st

def mostrar_casos_reales():
    """
    Renderiza la sección de Casos Reales y Análisis 
    con diseño de flujo sincronizado para el hub de Meteoro-ingeniería.
    """
    st.title("📂 Casos Reales y Análisis")
    
    # Enlace de contacto para consultoría basada en casos
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20me%20interesa%20conocer%20más%20sobre%20los%20casos%20de%20éxito"
    st.link_button("Solicitar asesoría técnica: 3122204688 📱", ws_link)
    
    st.markdown("---")
    
    # Declaración de enfoque estratégico
    st.markdown(f"""
    <div style="background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 5px solid #00d4ff; margin-bottom: 30px;">
        <p style="color: #ffffff; font-size: 1.1rem; line-height: 1.6; margin: 0;">
        No solo vemos máquinas; vemos flujos de capital y eficiencia. Cada caso real analizado 
        alimenta nuestro algoritmo de <b>Minería de Datos</b> para prevenir fugas de dinero. 
        Transformamos problemas operativos en activos estratégicos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Transformación de Problemas en Activos (Casos de Éxito)")

    # Definición de los casos con la estructura de pasos sincronizada
    casos = [
        {
            "id": 1, 
            "t": "Control de Aceite Hidráulico", 
            "p": "Pérdida de integridad en la información recolectada en campo y errores en la toma de decisiones.",
            "s": "Implementación de digitalización directa desde la fuente. Eliminamos el error humano asegurando datos puros.",
            "r": "Decisiones basadas en datos reales e impecables, no en suposiciones."
        },
        {
            "id": 2, 
            "t": "Gestión de Mangueras In-house", 
            "p": "Altos tiempos de inactividad (Downtime) por dependencia de proveedores externos y logística lenta.",
            "s": "Transición estratégica de compra externa a ensamblaje propio (In-house). Rediseño de logística y control.",
            "r": "Reducción drástica del tiempo de espera por repuestos y ahorro operativo inmediato."
        }
    ]
    
    # Renderizado con flechas de flujo sincronizadas (↓↓↓)
    for i, c in enumerate(casos):
        st.markdown(f"""
            <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 2px solid #00d4ff; margin-bottom: 5px;">
                <div style="color: #00d4ff; font-weight: bold; font-size: 1.3rem; margin-bottom: 10px;">
                    CASO {c['id']}: {c['t']}
                </div>
                <p style="color: #ff4b4b; font-weight: bold; margin-bottom: 5px;">⚠️ Problema:</p>
                <p style="color: #ccd6f6; margin-bottom: 15px;">{c['p']}</p>
                <p style="color: #00d4ff; font-weight: bold; margin-bottom: 5px;">🛠️ Solución Meteoro:</p>
                <p style="color: #ccd6f6; margin-bottom: 15px;">{c['s']}</p>
                <p style="color: #00ff7f; font-weight: bold; margin-bottom: 5px;">📈 Resultado:</p>
                <p style="color: #ccd6f6; margin-bottom: 0;">{c['r']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Indicador de flujo visual entre casos
        if i < len(casos) - 1:
            st.markdown("""
                <div style="text-align: center; margin: 10px 0;">
                    <span style="color: #00d4ff; font-size: 2rem; font-weight: bold;">↓↓↓</span>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("Nuestra metodología garantiza que cada lección aprendida se convierta en una mejora para su Imperio.")

if __name__ == "__main__":
    st.set_page_config(page_title="Casos y Análisis | Meteoro", layout="wide")
    mostrar_casos_reales()