import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------------
st.set_page_config(
    page_title="Abogadas-Hermandad | Defensa Legal de la Mujer en Chile",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# ESTILOS CSS - ESTÉ TICA CÁLIDA (CREMA, BLANCO Y DORADO)
# Inspirado en Círculo Defensa Legal / Schneider Abogados
# ---------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    /* FORZAR FONDO Y TEXTO EN TODO STREAMLIT (Evita Modo Oscuro) */
    [data-testid="stAppViewContainer"], 
    [data-testid="stHeader"], 
    .stApp, body, html {
        background-color: #FAF7F2 !important;
        color: #2D251E !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Ocultar elementos nativos de Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {
        visibility: hidden !important;
        height: 0px !important;
    }

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 3rem !important;
        max-width: 1150px !important;
    }

    /* BARRA SUPERIOR DE ANUNCIO / ENCABEZADO CÁLIDO */
    .top-bar {
        background-color: #4A121A;
        color: #D4AF37;
        text-align: center;
        padding: 8px 15px;
        font-size: 0.82rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        font-weight: 500;
        margin-bottom: 2rem;
    }

    /* TITULAR Y MARCA */
    .brand-header {
        text-align: center;
        padding: 1rem 0 2rem 0;
    }

    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #4A121A !important;
        letter-spacing: 1px;
        margin: 0;
    }

    .brand-subtitle {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #B8860B !important;
        margin-top: 0.5rem;
        font-weight: 600;
    }

    /* LÍNEA SEPARADORA DORADA */
    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, rgba(184,134,11,0) 0%, rgba(184,134,11,0.6) 50%, rgba(184,134,11,0) 100%);
        margin: 2.5rem 0;
    }

    /* HERO BANNER ESTILO BUFETE */
    .hero-container {
        background-color: #FFFFFF;
        border: 1px solid #E8DFD1;
        border-radius: 4px;
        padding: 3.5rem 2.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(74, 18, 26, 0.03);
    }

    .hero-heading {
        font-family: 'Playfair Display', serif;
        font-size: 2.4rem;
        color: #4A121A !important;
        font-weight: 600;
        line-height: 1.3;
        margin-bottom: 1.2rem;
    }

    .hero-subtext {
        font-size: 1.05rem;
        color: #5A4E44 !important;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.7;
    }

    /* INDICADORES / M ÉTRICAS ESTILO CÍRCULO DEFENSA */
    .stat-card {
        background: #FDFBF7;
        border: 1px solid #E8DFD1;
        border-radius: 4px;
        padding: 1.5rem 1rem;
        text-align: center;
    }

    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #4A121A !important;
    }

    .stat-label {
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #8C7A6B !important;
        margin-top: 0.3rem;
    }

    /* TARJETAS DE SERVICIOS */
    .card-service {
        background-color: #FFFFFF;
        border: 1px solid #E8DFD1;
        border-top: 3px solid #B8860B;
        border-radius: 4px;
        padding: 2rem 1.5rem;
        height: 100%;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.02);
    }

    .card-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: #4A121A !important;
        margin-bottom: 0.8rem;
    }

    .card-desc {
        font-size: 0.93rem;
        color: #5A4E44 !important;
        line-height: 1.6;
    }

    /* SECCIÓN ABOGADA DIRECTORA */
    .profile-box {
        background-color: #FFFFFF;
        border: 1px solid #E8DFD1;
        border-radius: 4px;
        padding: 2.5rem;
    }

    .profile-name {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        color: #4A121A !important;
        font-weight: 700;
    }

    .profile-title {
        color: #B8860B !important;
        font-size: 0.88rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 1.2rem;
    }

    /* ALERTA / URGENCIA */
    .urgency-banner {
        background-color: #FFFDF9;
        border: 1px solid #E8DFD1;
        border-left: 4px solid #4A121A;
        padding: 1.2rem 1.5rem;
        border-radius: 4px;
        font-size: 0.93rem;
        color: #4A121A !important;
        margin-bottom: 2rem;
    }

    /* FORMULARIO DE CONTACTO PERSONALIZADO */
    div[data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E8DFD1 !important;
        border-radius: 6px !important;
        padding: 2rem !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02) !important;
    }

    /* INPUTS CÁLIDOS */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: #FAF7F2 !important;
        border-color: #E8DFD1 !important;
        color: #2D251E !important;
    }

    /* BOTÓN ESTILO DORADO LUJO */
    .stButton > button {
        background: linear-gradient(135deg, #C5A059 0%, #A8833D 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.75rem 2rem !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        width: 100% !important;
        box-shadow: 0 3px 10px rgba(168, 131, 61, 0.2) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #B8860B 0%, #8C6219 100%) !important;
        box-shadow: 0 4px 15px rgba(168, 131, 61, 0.3) !important;
    }

    /* EXPANDERS (FAQ) */
    .stExpander {
        background-color: #FFFFFF !important;
        border: 1px solid #E8DFD1 !important;
        border-radius: 4px !important;
        margin-bottom: 0.5rem !important;
    }

    /* Texto global dentro de parrafos y etiquetas */
    p, span, label, h1, h2, h3, h4 {
        color: #2D251E !important;
    }

    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BARRA DE ANUNCIO CÁLIDA
# ---------------------------------------------------------
st.markdown("""
    <div class="top-bar">
        📞 CONSULTA CONFIDENCIAL • ASESORÍA LEGAL CON PERSPECTIVA DE GÉNERO EN TODO CHILE
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CABECERA Y LOGOTIPO
# ---------------------------------------------------------
st.markdown("""
    <div class="brand-header">
        <div class="brand-title">ABOGADAS HERMANDAD</div>
        <div class="brand-subtitle">Estudio Jurídico Especializado en Derechos de la Mujer</div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO PRINCIPAL
# ---------------------------------------------------------
st.markdown("""
    <div class="hero-container">
        <div class="hero-heading">Defensa jurídica firme, humana y libre de prejuicios</div>
        <div class="hero-p" style="font-size: 1.05rem; color: #5A4E44; max-width: 820px; margin: 0 auto; line-height: 1.7;">
            Acompañamos a mujeres en todo Chile frente a situaciones complejas de violencia intrafamiliar, agresiones, vulneración de derechos, acoso laboral y derecho de familia. Tu seguridad y la de tus hijos es nuestra prioridad absoluta.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# M étricas / Cifras
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="stat-card"><div class="stat-number">100%</div><div class="stat-label">Confidencialidad</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="stat-card"><div class="stat-number">24 hrs</div><div class="stat-label">Respuesta Inmediata</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="stat-card"><div class="stat-number">Nacional</div><div class="stat-label">Atención en todo Chile</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="stat-card"><div class="stat-number">Especialistas</div><div class="stat-label">Derecho de la Mujer</div></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ALERTA DE EMERGENCIA / VIF
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div class="urgency-banner">
        <b>¿Enfrentas una situación de riesgo inminente?</b><br>
        En caso de violencia intrafamiliar aguda, puedes llamar al <b>Fono Familia de Carabineros (149)</b> o al <b>1455 (SernamEG)</b>. Para representación judicial y solicitud urgente de medidas de protección y alejamiento, estamos preparadas para actuar por ti.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ÁREAS DE PRÁCTICA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 2.2rem; color: #4A121A !important; margin-bottom: 2rem;'>Áreas de Práctica & Especialización</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card-service">
            <div class="card-title">Protección VIF y Agresiones</div>
            <div class="card-desc">
                Tramitación prioritaria de medidas cautelares de alejamiento, salida del agresor del hogar común, querellas criminales por agresiones físicas, psicológicas y amenazas.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card-service">
            <div class="card-title">Derecho de Familia</div>
            <div class="card-desc">
                Demandas y retención de pensión de alimentos (fondos AFP y bancarios), cuidado personal (tuición), régimen de visitas y divorcios.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card-service">
            <div class="card-title">Acoso Laboral y Ley Karin</div>
            <div class="card-desc">
                Defensa y querellas laborales frente a acoso sexual, acoso laboral en el trabajo, tutela de derechos fundamentales y despidos injustificados por maternidad.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
        <div class="card-service">
            <div class="card-title">Representación Penal a Víctimas</div>
            <div class="card-desc">
                Acompañamiento a víctimas de delitos sexuales y violencia. Nos aseguramos de que seas tratada con dignidad durante todo el proceso penal ante Fiscalía.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
        <div class="card-service">
            <div class="card-title">Medidas Cautelares de Urgencia</div>
            <div class="card-desc">
                Estrategia jurídica para resguardar la seguridad física, emocional y los bienes patrimoniales de forma rápida en los Tribunales de Familia o Garantía.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
        <div class="card-service">
            <div class="card-title">Asesoría Preventiva</div>
            <div class="card-desc">
                Orientación técnica previa a tomar decisiones definitivas: separación de bienes, acuerdos de cuidadores y redacción de estipulaciones sin ambigüedades.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ABOGADA DIRECTORA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 2.2rem; color: #4A121A !important; margin-bottom: 2rem;'>Abogada Directora</h2>", unsafe_allow_html=True)

p_col1, p_col2 = st.columns([1, 2])

with p_col1:
    st.markdown("""
        <div style="background-color: #FAF7F2; border: 1px solid #E8DFD1; border-radius: 4px; height: 100%; min-height: 220px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 1.5rem;">
            <div>
                <div style="font-family: Playfair Display, serif; font-size: 1.5rem; color: #4A121A; font-weight: 700;">
                    María-Francisca Valentina
                </div>
                <div style="font-size: 0.85rem; color: #B8860B; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.4rem;">
                    Abogada Litigante
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with p_col2:
    st.markdown("""
        <div class="profile-box">
            <div class="profile-name">María-Francisca Valentina</div>
            <div class="profile-title">Socia Fundadora & Abogada Directora</div>
            <p style="color: #5A4E44; line-height: 1.7; font-size: 0.98rem;">
                Abogada dedicada a la litigación en materias de Familia y Penal, enfocada en la protección integral de los derechos de las mujeres en Chile. 
                Fundó <b>Abogadas-Hermandad</b> buscando ofrecer un espacio de alta solidez jurídica, libre de revictimización, donde cada clienta reciba una representación clara, cercana y contundente.
            </p>
            <p style="color: #8C7A6B; font-size: 0.88rem; margin-top: 1rem;">
                📍 Cobertura presencial en la Región Metropolitana y tramitación electrónica coordinada para tribunales de todo Chile.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# FORMULARIO DE CONTACTO ELEGANTE
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 2.2rem; color: #4A121A !important; margin-bottom: 0.5rem;'>Agenda tu Consulta Confidencial</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8C7A6B; font-size: 0.95rem; margin-bottom: 2rem;'>Tu mensaje será revisado bajo estricto secreto profesional.</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    fc1, fc2 = st.columns(2)
    
    with fc1:
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono o WhatsApp (+56 9...)")
        region = st.selectbox("Región", [
            "Región Metropolitana", "Valparaíso", "Biobío", "Antofagasta", "Coquimbo", 
            "O'Higgins", "Maule", "La Araucanía", "Los Lagos", "Otra región de Chile"
        ])

    with fc2:
        correo = st.text_input("Correo electrónico")
        materia = st.selectbox("Materia de la consulta", [
            "Violencia Intrafamiliar (VIF) / Alejamiento",
            "Pensión de Alimentos / Retención de Fondos",
            "Cuidado Personal / Visitas",
            "Acoso Laboral / Ley Karin",
            "Derecho Penal / Querellas a Víctimas",
            "Otra consulta legal"
        ])
        horario = st.text_input("Horario preferente para llamada")

    mensaje = st.text_area("Cuéntanos brevemente tu caso (Sin tecnicismos legales)")
    
    submitted = st.form_submit_button("Enviar Consulta Confidencial →")
    
    if submitted:
        if nombre and (telefono or correo):
            st.success("✅ Tu consulta ha sido enviada con éxito. Nos pondremos en contacto contigo a la brevedad con la mayor discreción.")
        else:
            st.error("Por favor completa tu nombre y al menos una vía de contacto (Teléfono o Correo).")

# ---------------------------------------------------------
# PREGUNTAS FRECUENTES
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 1.8rem; color: #4A121A !important; margin-bottom: 1.5rem;'>Preguntas Frecuentes</h2>", unsafe_allow_html=True)

with st.expander("¿Cómo se solicita una medida cautelar de alejamiento inmediata?"):
    st.write("Se interpone ante el Tribunal de Familia o de Garantía una solicitud de protección por violencia intrafamiliar. El tribunal puede dictar la prohibición de acercamiento y la salida del agresor en plazos muy breves.")

with st.expander("¿Qué ocurre si el demandado no paga la pensión de alimentos?"):
    st.write("Solicitamos la liquidación de la deuda y aplicamos las herramientas de la Ley de Papitos Corazón: arresto nocturno, suspensión de licencia de conducir, retención de devolución de impuestos y fondos de AFP o bancarios.")

with st.expander("¿Cómo funciona la Ley Karin frente al acoso laboral?"):
    st.write("La Ley Karin exige a las empresas protocolos rigurosos de prevención e investigación ante acoso laboral y sexual. Te orientamos para activar la denuncia interna o accionar judicialmente ante la Inspección del Trabajo y Tribunales Laborales.")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; font-size: 0.85rem; color: #8C7A6B; padding-bottom: 2rem;">
        © 2026 <b>Abogadas-Hermandad</b> • Estudio Jurídico de la Mujer en Chile<br>
        <i>Compromiso, Integridad y Defensa Legal Efectiva.</i>
    </div>
""", unsafe_allow_html=True)
