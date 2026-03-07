import streamlit as st

def mostrar_casos_reales():
    """
    Renderiza la sección de Casos Reales y Análisis 
    para el hub de Meteoro-ingeniería.
    """
    st.title("📂 Casos Reales y Análisis")
    
    # Enlace de contacto para consultoría basada en casos
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20me%20interesa%20conocer%20más%20sobre%20los%20casos%20de%20éxito"
    st.link_button("Solicitar asesoría técnica: 3122204688 📱", ws_link)
    
    st.write("---")
    st.markdown("### Transformación de Problemas en Activos")

    # Caso 1: Aceite Hidráulico
    with st.expander("📌 Control de Aceite Hidráulico"):
        st.info("**Problema:** Pérdida de integridad en la información recolectada en campo.")
        st.write("""
        **Solución Meteoro:** Implementación de digitalización directa. Eliminamos el error humano 
        y aseguramos que la salud del dato sea impecable desde la fuente.
        """)
        st.success("Resultado: Decisiones basadas en datos puros, no en suposiciones.")

    # Caso 2: Mangueras Hidráulicas
    with st.expander("📌 Gestión de Mangueras In-house"):
        st.info("**Problema:** Altos tiempos de inactividad por dependencia de proveedores externos.")
        st.write("""
        **Solución Meteoro:** Transición estratégica de compra externa a ensamblaje propio (In-house). 
        Diseñamos el control y la logística para que la máquina no espere por un repuesto.
        """)
        st.success("Resultado: Reducción drástica del Downtime y ahorro operativo inmediato.")

    # Sección de Análisis Estratégico
    st.markdown("---")
    st.subheader("Análisis de Valor")
    st.write("""
    No solo vemos máquinas; vemos flujos de capital y eficiencia. Cada caso real analizado 
    alimenta nuestro algoritmo de **Minería de Datos** para prevenir futuras fugas de dinero.
    """)

if __name__ == "__main__":
    # Prueba del módulo
    st.set_page_config(page_title="Casos y Análisis | Meteoro", layout="wide")
    mostrar_casos_reales()