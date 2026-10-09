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
# ESTADO DEL TEMA (MODO CLARO CÁLIDO / MODO OSCURO DORADO)
# ---------------------------------------------------------
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "light"

def toggle_theme():
    if st.session_state.theme_mode == "light":
        st.session_state.theme_mode = "dark"
    else:
        st.session_state.theme_mode = "light"

is_dark = st.session_state.theme_mode == "dark"

# ---------------------------------------------------------
# VARIABLES DE COLOR (CERO ROJOS - SOLO CREMAS, AMARILLOS Y DORADOS)
# ---------------------------------------------------------
if is_dark:
    bg_app = "#161411"
    bg_card = "#221E19"
    bg_secondary = "#2D2720"
    border_color = "#4D402F"
    text_main = "#F7F3EA"
    text_muted = "#C7B9A5"
    gold_main = "#E0B354"
    gold_hover = "#F0C868"
    scale_angle = "rotate(12deg) translateY(4px)" # Balanza baja en modo oscuro
    status_text = "Modo Oscuro Activo (Balanza Abajo)"
else:
    bg_app = "#FAF7F0"
    bg_card = "#FFFFFF"
    bg_secondary = "#F4ECE0"
    border_color = "#EADCC9"
    text_main = "#2E261F"
    text_muted = "#7A6D5E"
    gold_main = "#C5A059"
    gold_hover = "#A8833D"
    scale_angle = "rotate(0deg) translateY(0px)" # Balanza sube / nivelada en modo claro
    status_text = "Modo Claro Activo (Balanza Arriba)"

# ---------------------------------------------------------
# ESTILOS CSS DINÁMICOS
# ---------------------------------------------------------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    /* Forzar fondo y tipografía global de Streamlit */
    [data-testid="stAppViewContainer"], 
    [data-testid="stHeader"], 
    .stApp, body, html {{
        background-color: {bg_app} !important;
        color: {text_main} !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: all 0.4s ease-in-out;
    }}

    /* Ocultar elementos nativos de Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {{
        visibility: hidden !important;
        height: 0px !important;
    }}

    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        max-width: 1120px !important;
    }}

    /* BARRA SUPERIOR DORADA */
    .top-bar {{
        background-color: {bg_secondary};
        color: {gold_main};
        border-bottom: 1px solid {border_color};
        text-align: center;
        padding: 10px 15px;
        font-size: 0.82rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 1.5rem;
        border-radius: 4px;
    }}

    /* BOTÓN Y BALANZA DE LA JUSTICIA CON ANIMACIÓN */
    .theme-toggle-container {{
        display: flex;
        justify-content: flex-end;
        align-items: center;
        margin-bottom: 1rem;
    }}

    .scale-icon-box {{
        width: 42px;
        height: 42px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
    }}

    .justice-scale-svg {{
        transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
        transform: {scale_angle};
        transform-origin: center;
    }}

    /* ENCABEZADO Y BRANDING */
    .brand-header {{
        text-align: center;
        padding: 1rem 0 2rem 0;
    }}

    .brand-title {{
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 700;
        color: {text_main} !important;
        letter-spacing: 1px;
        margin: 0;
    }}

    .brand-subtitle {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.88rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: {gold_main} !important;
        margin-top: 0.6rem;
        font-weight: 600;
    }}

    .gold-divider {{
        height: 1px;
        background: linear-gradient(90deg, rgba(197,160,89,0) 0%, {gold_main} 50%, rgba(197,160,89,0) 100%);
        margin: 2.5rem 0;
    }}

    /* HERO BANNER */
    .hero-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        border-radius: 8px;
        padding: 3.5rem 2.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}

    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: {text_main} !important;
        font-weight: 700;
        line-height: 1.3;
        margin-bottom: 1.2rem;
    }}

    .hero-text {{
        font-size: 1.08rem;
        color: {text_muted} !important;
        max-width: 820px;
        margin: 0 auto;
        line-height: 1.7;
    }}

    /* TARJETAS DE SERVICIO */
    .service-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        border-top: 3px solid {gold_main};
        border-radius: 6px;
        padding: 2rem 1.5rem;
        height: 100%;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
    }}

    .service-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: {gold_main} !important;
        margin-bottom: 0.8rem;
    }}

    .service-desc {{
        font-size: 0.94rem;
        color: {text_muted} !important;
        line-height: 1.6;
    }}

    /* TARJETA PROFILE DE LA ABOGADA */
    .profile-box {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        border-radius: 8px;
        padding: 2.5rem;
    }}

    .profile-name {{
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        color: {text_main} !important;
        font-weight: 700;
    }}

    .profile-role {{
        color: {gold_main} !important;
        font-size: 0.88rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 1rem;
    }}

    /* CAJA DE URGENCIA AMARILLA/DORADA */
    .emergency-box {{
        background-color: {bg_secondary};
        border: 1px solid {border_color};
        border-left: 4px solid {gold_main};
        padding: 1.3rem;
        border-radius: 6px;
        margin-bottom: 2rem;
        font-size: 0.95rem;
        color: {text_main} !important;
    }}

    /* BOTONES STREAMLIT */
    .stButton > button {{
        background: linear-gradient(135deg, {gold_main} 0%, #A8833D 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.7rem 1.8rem !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
    }}

    .stButton > button:hover {{
        box-shadow: 0 4px 15px rgba(197, 160, 89, 0.4) !important;
        transform: translateY(-1px);
    }}

    /* FORMULARIO Y CAMPOS */
    div[data-testid="stForm"] {{
        background-color: {bg_card} !important;
        border: 1px solid {border_color} !important;
        border-radius: 8px !important;
        padding: 2rem !important;
    }}

    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea {{
        background-color: {bg_app} !important;
        border-color: {border_color} !important;
        color: {text_main} !important;
    }}

    /* PREGUNTAS FRECUENTES */
    .stExpander {{
        background-color: {bg_card} !important;
        border: 1px solid {border_color} !important;
        border-radius: 6px !important;
        margin-bottom: 0.6rem !important;
    }}

    p, span, label, h1, h2, h3, h4 {{
        color: {text_main} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BARRA SUPERIOR & BOTÓN CON BALANZA ANIMADA
# ---------------------------------------------------------
st.markdown("""
    <div class="top-bar">
        ⚖️ CONSULTA LEGAL CONFIDENCIAL • DEFENSA DE LA MUJER EN TODO CHILE
    </div>
""", unsafe_allow_html=True)

# Contenedor del Botón e Icono Vectorial de Balanza
col_space, col_btn = st.columns([3, 1])

with col_btn:
    # SVG Vectorial de la Balanza de la Justicia (Dorado)
    scale_svg = f"""
    <div class="theme-toggle-container">
        <div class="scale-icon-box">
            <svg class="justice-scale-svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <!-- Base y Pilar Central -->
                <path d="M12 3v17" />
                <path d="M8 21h8" />
                <!-- Barra Horizontal de Equilibrio -->
                <path d="M5 7h14" />
                <!-- Platillo Izquierdo -->
                <path d="M5 7l-3 6h6l-3-6z" />
                <!-- Platillo Derecho -->
                <path d="M19 7l-3 6h6l-3-6z" />
            </svg>
        </div>
    </div>
    """
    st.markdown(scale_svg, unsafe_allow_html=True)
    
    label_btn = "☀️ Modo Claro" if is_dark else "🌙 Modo Oscuro"
    st.button(label_btn, on_click=toggle_theme, use_container_width=True)

# ---------------------------------------------------------
# LOGOTIPO Y ENCABEZADO
# ---------------------------------------------------------
st.markdown("""
    <div class="brand-header">
        <div class="brand-title">ABOGADAS HERMANDAD</div>
        <div class="brand-subtitle">Estudio Jurídico de la Mujer & Acompañamiento Integral</div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO PRINCIPAL
# ---------------------------------------------------------
st.markdown("""
    <div class="hero-card">
        <div class="hero-title">Defensa legal especializada, humana y libre de prejuicios</div>
        <div class="hero-text">
            Te acompañamos con rigor técnico y máxima confidencialidad ante situaciones complejas de violencia intrafamiliar, vulneración de derechos, acoso laboral y conflictos de familia en Chile. Tu tranquilidad jurídica es nuestro compromiso.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ALERTA DE URGENCIA / VIF
# ---------------------------------------------------------
st.markdown("""
    <div class="emergency-box">
        <b>¿Enfrentas una situación de riesgo inminente?</b><br>
        En casos de Violencia Intrafamiliar (VIF) aguda, recuerda comunicarte directamente al <b>Fono Familia de Carabineros (149)</b> o al <b>1455 (SernamEG)</b>. Para representación legal express e interposición urgente de medidas de protección y alejamiento, cuenta con nuestro equipo.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ÁREAS DE PRÁCTICA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 2.2rem; margin-bottom: 2rem;'>Áreas de Especialización</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Protección VIF y Agresiones</div>
            <div class="service-desc">
                Tramitación prioritaria de medidas cautelares de alejamiento, expulsión del agresor del hogar común, querellas criminales por agresiones físicas, psicológicas y amenazas.
            </div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Derecho de Familia</div>
            <div class="service-desc">
                Demandas de pensión de alimentos, retención de fondos (AFP y cuentas bancarias), cuidado personal (tuición), relación directa y regular (visitas) y divorcios.
            </div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Acoso Laboral y Ley Karin</div>
            <div class="service-desc">
                Intervención legal estratégica ante acoso laboral, acoso sexual en el trabajo, tutela de derechos fundamentales y despidos injustificados por maternidad o género.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Representación Penal a Víctimas</div>
            <div class="service-desc">
                Acompañamiento a víctimas de delitos sexuales y violencia. Nos aseguramos de que seas tratada con dignidad durante todo el proceso penal ante el Ministerio Público.
            </div>
        </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Medidas de Emergencia</div>
            <div class="service-desc">
                Orientación técnica previa a denuncias para resguardar la seguridad física, emocional y patrimonial de ti y de tus hijos en Tribunales de Familia o Garantía.
            </div>
        </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
        <div class="service-card">
            <div class="service-title">Asesoría Preventiva</div>
            <div class="service-desc">
                Revisión de acuerdos, separación de bienes, capitulaciones matrimoniales y orientación en lenguaje claro antes de tomar decisiones judiciales definitivas.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ABOGADA DIRECTORA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 2.2rem; margin-bottom: 2rem;'>Nuestra Abogada Directora</h2>", unsafe_allow_html=True)

col_p1, col_p2 = st.columns([1, 2])

with col_p1:
    st.markdown(f"""
        <div style="background-color: {bg_secondary}; border: 1px solid {border_color}; border-radius: 8px; height: 100%; min-height: 220px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 1.5rem;">
            <div>
                <div style="font-family: Playfair Display, serif; font-size: 1.6rem; color: {text_main}; font-weight: 700;">
                    María-Francisca Valentina
                </div>
                <div style="font-size: 0.85rem; color: {gold_main}; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.4rem; font-weight: 600;">
                    Abogada Litigante
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
        <div class="profile-box">
            <div class="profile-name">María-Francisca Valentina</div>
            <div class="profile-role">Abogada Directora & Socia Fundadora</div>
            <p style="line-height: 1.7; font-size: 0.98rem;">
                Especialista en litigación familiar y penal con enfoque de derechos humanos y perspectiva de género en Chile. 
                Fundó <b>Abogadas-Hermandad</b> con la visión de ofrecer una defensa técnica de la más alta exigencia, combinada con contención real y transparencia absoluta para cada clienta.
            </p>
            <p style="font-size: 0.88rem; margin-top: 1rem; opacity: 0.8;">
                • Cobertura en la Región Metropolitana y tramitación electrónica coordinada en tribunales de todo Chile.<br>
                • Atención presencial previa reserva y reuniones remotas por videollamada cifrada.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# FORMULARIO DE CONSULTA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 2.2rem; margin-bottom: 0.5rem;'>Agenda tu Consulta Confidencial</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.95rem; margin-bottom: 2rem; opacity: 0.8;'>Tus datos están protegidos bajo estricto secreto profesional.</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    fc1, fc2 = st.columns(2)
    
    with fc1:
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono / WhatsApp (+56 9...)")
        region = st.selectbox("Región de residencia", [
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
        horario = st.text_input("Horario preferente de contacto")

    mensaje = st.text_area("Cuéntanos brevemente tu caso (sin tecnicismos legales)")
    
    submitted = st.form_submit_button("Enviar consulta confidencial →")
    
    if submitted:
        if nombre and (telefono or correo):
            st.success("✅ Tu consulta ha sido enviada con éxito. Te contactaremos dentro de las próximas 24 horas hábiles con la mayor discreción.")
        else:
            st.error("Por favor completa tu nombre y al menos un método de contacto (Teléfono o Correo).")

# ---------------------------------------------------------
# PREGUNTAS FRECUENTES
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-family: Playfair Display, serif; font-size: 1.8rem; margin-bottom: 1.5rem;'>Preguntas Frecuentes</h2>", unsafe_allow_html=True)

with st.expander("¿Cómo se solicita una medida cautelar de alejamiento de urgencia?"):
    st.write("Se tramita ante el Tribunal de Familia o de Garantía. Solicitamos medidas cautelares inmediatas de prohibición de acercamiento y la expulsión del agresor del hogar común para resguardar tu integridad física y emocional.")

with st.expander("¿Qué acciones existen si no pagan la pensión de alimentos?"):
    st.write("Solicitamos la liquidación de la deuda y la aplicación de las medidas de la Ley de Papitos Corazón: retención de fondos de AFP o bancarios, suspensión de licencia de conducir, arraigo nacional e inscripción en el Registro Nacional de Deudores.")

with st.expander("¿Atienden causas fuera de Santiago?"):
    st.write("Sí. Gracias a la tramitación electrónica del Poder Judicial en Chile, representamos y coordinamos audiencias para clientas en todo el territorio nacional.")

# ---------------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------------
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; font-size: 0.85rem; color: {text_muted}; padding-bottom: 2rem;">
        © 2026 <b>Abogadas-Hermandad</b> • Estudio Jurídico de la Mujer en Chile<br>
        <i>Compromiso, Integridad y Defensa Legal Efectiva.</i>
    </div>
""", unsafe_allow_html=True)
