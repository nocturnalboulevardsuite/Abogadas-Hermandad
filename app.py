import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Abogadas-Hermandad | Defensa Legal de la Mujer en Chile",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# ESTILOS CSS PERSONALIZADOS (Blanco y Dorado Minimalista)
# ---------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #2C2C2C;
        background-color: #FAFAFA;
    }

    /* Ocultar elementos nativos innecesarios de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* Header y Navegación */
    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #1A1A1A;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 0px;
    }
    
    .brand-subtitle {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #C5A059;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 600;
    }

    .gold-divider {
        height: 1px;
        background: linear-gradient(90deg, rgba(197,160,89,0) 0%, rgba(197,160,89,0.8) 50%, rgba(197,160,89,0) 100%);
        margin: 2rem 0;
    }

    /* Hero Banner */
    .hero-box {
        background-color: #FFFFFF;
        border: 1px solid #F0E6D2;
        border-radius: 12px;
        padding: 3.5rem 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
        margin-bottom: 3rem;
    }

    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.5rem;
        font-weight: 600;
        color: #111111;
        line-height: 1.2;
        margin-bottom: 1rem;
    }

    .hero-p {
        font-size: 1.1rem;
        color: #555555;
        max-width: 750px;
        margin: 0 auto 1.5rem auto;
        line-height: 1.6;
    }

    /* Targetas de Servicios / Áreas */
    .service-card {
        background: #FFFFFF;
        border: 1px solid #EAE6DF;
        border-top: 3px solid #C5A059;
        border-radius: 8px;
        padding: 1.8rem;
        height: 100%;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
        transition: transform 0.2s ease;
    }

    .service-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #1A1A1A;
        margin-bottom: 0.8rem;
    }

    .service-desc {
        font-size: 0.92rem;
        color: #666666;
        line-height: 1.5;
    }

    /* Perfil de la Abogada */
    .profile-card {
        background: #FFFFFF;
        border: 1px solid #EAE6DF;
        border-radius: 12px;
        padding: 2.5rem;
        margin-top: 1rem;
    }

    .profile-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #1A1A1A;
        margin-bottom: 0.2rem;
    }

    .profile-role {
        color: #C5A059;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }

    /* Botón de Estilo Dorado */
    .stButton>button {
        background-color: #C5A059 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #A8833D !important;
        box-shadow: 0 4px 12px rgba(197, 160, 89, 0.3) !important;
    }

    /* Cajas de Alerta Sensible */
    .emergency-box {
        background-color: #FFFDF9;
        border-left: 4px solid #C5A059;
        padding: 1.2rem;
        border-radius: 4px;
        margin-bottom: 2rem;
        font-size: 0.95rem;
        color: #4A4A4A;
    }

    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ENCABEZADO Y LOGO TEXTUAL
# ---------------------------------------------------------
st.markdown('<div class="brand-title">ABOGADAS HERMANDAD</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-subtitle">Estudio Jurídico de la Mujer & Acompañamiento Integral • Chile</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO / PRESENTACIÓN PRINCIPAL
# ---------------------------------------------------------
st.markdown("""
    <div class="hero-box">
        <div class="hero-title">Defensa jurídica firme, cercana y libre de prejuicios.</div>
        <div class="hero-p">
            Te acompañamos frente a situaciones complejas de violencia, vulneración de derechos, acoso laboral y conflictos de familia en Chile. Tu tranquilidad y seguridad jurídica son nuestra única prioridad.
        </div>
    </div>
""", unsafe_allow_html=True)

# Alerta confidencial/urgencias
st.markdown("""
    <div class="emergency-box">
        <b>¿Necesitas ayuda urgente?</b> Si estás enfrentando una situación de riesgo inminente por Violencia Intrafamiliar (VIF), recuerda que puedes comunicarte directamente al <b>Fono Familia de Carabineros (149)</b> o al <b>1455 (SernamEG)</b>. Para representación e interposición de medidas de protección legales, cuenta con nosotras.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ÁREAS DE ESPECIALIZACIÓN
# ---------------------------------------------------------
st.markdown("<h3 style='text-align: center; font-family: Cormorant Garamond, serif; font-size: 2rem; margin-bottom: 2rem; color: #1A1A1A;'>Especialidades Legales</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Protección VIF y Agresiones</div>
            <div class="service-desc">
                Tramitación rápida de medidas cautelares de alejamiento, salida del agresor del hogar común, querellas criminales por agresiones, amenazas y violencia intrafamiliar.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Derecho de Familia</div>
            <div class="service-desc">
                Demandas de pensión de alimentos, retención de fondos (AFP y bancarios), cuidado personal (tuición), relación directa y regular (visitas) y divorcios.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Acoso y Ley Karin</div>
            <div class="service-desc">
                Asesoría e intervención legal por acoso laboral, acoso sexual en el trabajo, tutela de derechos fundamentales y despidos injustificados por maternidad o género.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Representación Penal</div>
            <div class="service-desc">
                Acompañamiento a víctimas de delitos sexuales, lesiones y acoso. Nos aseguramos de que tu voz sea escuchada con dignidad en el Ministerio Público.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Medidas de Emergencia</div>
            <div class="service-desc">
                Orientación técnica estratégica previa a denuncias para resguardar la seguridad física, emocional y patrimonial de ti y de tus hijos.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Asesoría Preventiva</div>
            <div class="service-desc">
                Revisión de acuerdos, capitulaciones matrimoniales, separación de bienes y orientación clara en lenguaje sencillo antes de tomar decisiones judiciales.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# EQUIPO / EQUIPO LÍDER
# ---------------------------------------------------------
st.markdown("<h3 style='text-align: center; font-family: Cormorant Garamond, serif; font-size: 2rem; margin-bottom: 1.5rem; color: #1A1A1A;'>Nuestra Abogada Fundadora</h3>", unsafe_allow_html=True)

col_profile, col_text = st.columns([1, 2])

with col_profile:
    # Espacio para foto profesional o avatar elegante
    st.markdown("""
        <div style="background: #FAF7F0; border: 1px solid #E6D5B8; border-radius: 12px; height: 100%; min-height: 250px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 1rem;">
            <span style="font-family: Cormorant Garamond, serif; font-size: 1.3rem; color: #C5A059;">
                <b>María-Francisca Valentina</b><br>
                <i style="font-size: 0.9rem; color: #777777;">Abogada Litigante</i>
            </span>
        </div>
    """, unsafe_allow_html=True)

with col_text:
    st.markdown("""
        <div class="profile-card">
            <div class="profile-name">María-Francisca Valentina</div>
            <div class="profile-role">Abogada Directora & Socia Fundadora</div>
            <p style="color: #555555; line-height: 1.6; font-size: 0.98rem;">
                Especialista en litigación familiar y penal con un marcado enfoque de derechos humanos y perspectiva de género en Chile. 
                Fundó <b>Abogadas-Hermandad</b> con la convicción de que la defensa jurídica de las mujeres debe combinar un nivel técnico impecable con empatía real, contención y transparencia absoluta.
            </p>
            <p style="color: #777777; font-size: 0.9rem; margin-top: 1rem;">
                • Cobertura en Región Metropolitana y representación judicial coordinada en todo Chile.<br>
                • Atención presencial previa cita y orientación remota por videollamada segura.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# FORMULARIO DE CONTACTO / CONSULTA
# ---------------------------------------------------------
st.markdown("<h3 style='text-align: center; font-family: Cormorant Garamond, serif; font-size: 2rem; margin-bottom: 0.5rem; color: #1A1A1A;'>Agenda tu Orientación Legal</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666666; font-size: 0.95rem; margin-bottom: 2rem;'>Tu información está protegida bajo estricto secreto profesional y absoluta confidencialidad.</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    f_col1, f_col2 = st.columns(2)
    
    with f_col1:
        nombre = st.text_input("Nombre completo (o de preferencia)")
        telefono = st.text_input("Teléfono de contacto / WhatsApp (+56 9...)")
        region = st.selectbox("Región de residencia", [
            "Región Metropolitana", "Valparaíso", "Biobío", "Antofagasta", "Coquimbo", 
            "O'Higgins", "Maule", "La Araucanía", "Los Lagos", "Otra región de Chile"
        ])

    with f_col2:
        correo = st.text_input("Correo electrónico")
        materia = st.selectbox("Materia de la consulta", [
            "Violencia Intrafamiliar (VIF) / Medidas de Protección",
            "Pensión de Alimentos / Retenciones de Fondos",
            "Cuidado Personal / Relación Directa y Regular",
            "Acoso Laboral / Ley Karin",
            "Derecho Penal / Denuncias y Querellas",
            "Otro asunto legal"
        ])
        horario = st.text_input("Horario preferente de contacto (ej: Tardes, Mañanas)")

    mensaje = st.text_area("Cuéntanos brevemente tu situación (Sin necesidad de usar términos legales)")
    
    submitted = st.form_submit_button("Enviar consulta confidencial")
    
    if submitted:
        if nombre and (telefono or correo):
            st.success("✅ Gracias por tu confianza. Tu consulta ha sido enviada con éxito. Te contactaremos dentro de las próximas 24 horas hábiles de manera discreta.")
        else:
            st.error("Por favor completa tu nombre y al menos un método de contacto (Teléfono o Correo).")

# ---------------------------------------------------------
# PREGUNTAS FRECUENTES (ACCORDION MINIMALISTA)
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-family: Cormorant Garamond, serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: #1A1A1A;'>Preguntas Frecuentes</h3>", unsafe_allow_html=True)

with st.expander("¿Cómo funcionan las medidas de protección ante agresiones o VIF?"):
    st.write("Las medidas de protección (como la prohibición de acercamiento o la salida del agresor del hogar) se tramitan ante los Tribunales de Familia o de Garantía. Podemos interponer la solicitud de manera urgente para resguardar tu integridad de inmediato.")

with st.expander("¿Qué necesito para demandar la pensión de alimentos o hacer efectiva la retención?"):
    st.write("Se requiere certificado de nacimiento de los hijos e información básica del demandado. Nos encargamos de calcular las necesidades, gestionar el proceso en el Tribunal y solicitar la inscripción en el Registro Nacional de Deudores o la retención de fondos si corresponde.")

with st.expander("¿Atienden casos en todo Chile?"):
    st.write("Sí. Con la tramitación digital del Poder Judicial de Chile, coordinamos audiencias y reuniones por videollamada para clientes en cualquier región del país, asegurando el mismo nivel de dedicación que presencialmente.")

# ---------------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------------
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; font-size: 0.85rem; color: #888888; padding-bottom: 2rem;">
        © 2026 <b>Abogadas-Hermandad</b>. Todos los derechos reservados.<br>
        <i>Defensa Legal de la Mujer en Chile • Compromiso, Ética y Confidencialidad.</i>
    </div>
""", unsafe_allow_html=True)
