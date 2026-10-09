import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Abogadas Hermandad | Defensa Legal de la Mujer",
    page_icon="⚖", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# ESTADO DEL TEMA
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
# VARIABLES DE COLOR Y ANIMACIÓN
# ---------------------------------------------------------
if is_dark:
    bg_app = "#12110E"
    bg_nav = "#181714"
    bg_card = "#1C1A17"
    bg_secondary = "#26231E"
    border_color = "#3A342C"
    text_main = "#F7F4ED"
    text_muted = "#B8B0A1"
    gold_main = "#E5C06A"
    gold_bright = "#FFD700"
    btn_text = "Cambiar Tema Claro"
    # La balanza se inclina hacia abajo
    scale_transform = "rotate(15deg) translateY(4px)"
else:
    bg_app = "#FCF8EB"        # Blanco más amarillento / crema cálido
    bg_nav = "#FFFFFF"
    bg_card = "#FFFFFF"
    bg_secondary = "#F2EDDF"
    border_color = "#E8DFCA"
    text_main = "#1E1A15"     
    text_muted = "#6B6255"
    gold_main = "#D4AF37"     
    gold_bright = "#E5B80B"   
    btn_text = "Cambiar Tema Oscuro"
    # La balanza sube / se mantiene equilibrada
    scale_transform = "rotate(0deg) translateY(0px)"

# ---------------------------------------------------------
# ESTILOS CSS DINÁMICOS Y ESTRUCTURA
# ---------------------------------------------------------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    [data-testid="stAppViewContainer"], 
    .stApp, body, html {{
        background-color: {bg_app} !important;
        color: {text_main} !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: background-color 0.4s ease, color 0.4s ease;
    }}

    #MainMenu, footer, header, [data-testid="stHeader"] {{
        visibility: hidden !important;
        height: 0px !important;
    }}

    .block-container {{
        padding-top: 6rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px !important;
    }}

    /* NAVBAR FIJO */
    .custom-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background-color: {bg_nav};
        border-bottom: 1px solid {border_color};
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 5%;
        z-index: 999999;
        box-shadow: 0 2px 15px rgba(0,0,0,0.04);
        transition: background-color 0.4s ease;
    }}

    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: {text_main};
        letter-spacing: 1px;
    }}

    .nav-links {{
        display: flex;
        gap: 2rem;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: {text_main};
    }}
    
    .nav-links span {{
        cursor: pointer;
        transition: color 0.3s;
    }}

    .nav-links span:hover {{
        color: {gold_bright};
    }}

    /* BALANZA ANIMADA Y BOTÓN TEMA CENTRADO */
    .theme-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 1.5rem auto 3rem auto;
        gap: 8px;
    }}

    .animated-scale {{
        transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        transform: {scale_transform};
        transform-origin: 50% 20%;
    }}

    /* BOTONES GLOBALES CON ZOOM DINÁMICO */
    .stButton > button {{
        background-color: {bg_app} !important;
        color: {text_main} !important;
        border: 1px solid {border_color} !important;
        border-radius: 4px !important;
        padding: 0.5rem 1.2rem !important; /* Más pequeño */
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        display: flex !important;
        margin: 0 auto !important; /* Centrado */
    }}

    .stButton > button:hover {{
        border-color: {gold_bright} !important;
        color: {gold_bright} !important;
        transform: scale(1.04) !important; /* Sutil zoom al pasar el ratón */
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.15) !important;
    }}

    .btn-primary > button {{
        background-color: {gold_main} !important;
        color: #FFFFFF !important;
        border: none !important;
        font-size: 0.9rem !important;
        padding: 0.8rem 2rem !important;
    }}
    
    .btn-primary > button:hover {{
        background-color: {gold_bright} !important;
        color: #FFFFFF !important;
        transform: scale(1.04) !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.3) !important;
    }}

    /* HERO BANNER */
    .hero-section {{
        text-align: center;
        padding: 3rem 1rem 1rem 1rem;
    }}

    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: {text_main};
        line-height: 1.1;
        margin-bottom: 1.5rem;
    }}

    .hero-subtitle {{
        font-size: 1.1rem;
        color: {text_muted};
        max-width: 800px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }}

    .gold-line {{
        width: 60px;
        height: 2px;
        background-color: {gold_bright};
        margin: 0 auto 2rem auto;
    }}

    /* CAJA DE URGENCIA */
    .alert-box {{
        background-color: {bg_secondary};
        border-left: 4px solid {gold_bright};
        padding: 1.5rem 2rem;
        margin: 2rem 0;
        border-radius: 4px;
        color: {text_main};
        transition: background-color 0.4s ease;
    }}
    
    .alert-title {{
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    /* TARJETAS DE SERVICIO */
    .service-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        padding: 2.5rem 2rem;
        border-radius: 6px;
        transition: transform 0.4s ease, box-shadow 0.4s ease, border-color 0.4s ease;
        height: 100%;
        text-align: left;
    }}

    .service-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        border-color: {gold_bright};
    }}

    .service-icon {{
        margin-bottom: 1.2rem;
    }}

    .service-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: {text_main};
        margin-bottom: 1rem;
    }}

    .service-desc {{
        font-size: 0.95rem;
        color: {text_muted};
        line-height: 1.6;
    }}

    h1, h2, h3, h4 {{
        font-family: 'Playfair Display', serif !important;
        color: {text_main} !important;
    }}
    
    p, label, span {{
        color: {text_main} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ÍCONOS SVG MEJORADOS (ALTA CALIDAD)
# ---------------------------------------------------------
icon_scale_nav = f"""<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v17M8 21h8M5 7h14M5 7l-3 6h6l-3-6zM19 7l-3 6h6l-3-6z"/></svg>"""

# Balanza grande para la animación
icon_scale_animated = f"""
<svg class="animated-scale" width="45" height="45" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 3v17" />
    <path d="M8 21h8" />
    <path d="M5 7h14" />
    <path d="M5 7l-3 6h6l-3-6z" />
    <path d="M19 7l-3 6h6l-3-6z" />
</svg>
"""

icon_alert = f"""<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01"/></svg>"""
icon_shield = f"""<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>"""
icon_users = f"""<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 7a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>"""
icon_briefcase = f"""<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>"""
icon_check = f"""<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>"""

# ---------------------------------------------------------
# NAVBAR SUPERIOR FIJO
# ---------------------------------------------------------
st.markdown(f"""
    <div class="custom-navbar">
        <div class="nav-brand">
            {icon_scale_nav}
            HERMANDAD
        </div>
        <div class="nav-links">
            <span>Inicio</span>
            <span>Áreas de Práctica</span>
            <span>Equipo</span>
            <span>Contacto</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BALANZA ANIMADA Y BOTÓN DE TEMA (CENTRADO)
# ---------------------------------------------------------
col_left, col_center, col_right = st.columns([4, 2, 4])
with col_center:
    st.markdown(f'<div class="theme-wrapper">{icon_scale_animated}</div>', unsafe_allow_html=True)
    st.button(btn_text, on_click=toggle_theme, use_container_width=False)

# ---------------------------------------------------------
# SECCIÓN HERO
# ---------------------------------------------------------
st.markdown(f"""
    <div class="hero-section">
        <div class="gold-line"></div>
        <div class="hero-title">Defensa legal especializada,<br>humana y libre de prejuicios.</div>
        <div class="hero-subtitle">
            Te acompañamos con rigor técnico y máxima confidencialidad ante situaciones complejas de violencia intrafamiliar, vulneración de derechos, acoso laboral y conflictos de familia en Chile. Tu tranquilidad jurídica es nuestro compromiso.
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ALERTA DE URGENCIA
# ---------------------------------------------------------
st.markdown(f"""
    <div class="alert-box">
        <div class="alert-title">{icon_alert} ¿Enfrentas una situación de riesgo inminente?</div>
        <div style="font-size: 0.95rem; line-height: 1.6; margin-top: 8px;">
            En casos de Violencia Intrafamiliar (VIF) aguda, comunícate directamente al <b>Fono Familia de Carabineros (149)</b> o al <b>1455 (SernamEG)</b>. 
            Para representación legal express e interposición urgente de medidas de protección y alejamiento, cuenta con nuestro equipo.
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# ÁREAS DE PRÁCTICA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0 2.5rem 0;'>Áreas de Especialización</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_shield}</div>
            <div class="service-title">Protección y VIF</div>
            <div class="service-desc">
                Tramitación prioritaria de medidas cautelares de alejamiento, expulsión del agresor del hogar común y querellas criminales por agresiones.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_users}</div>
            <div class="service-title">Derecho de Familia</div>
            <div class="service-desc">
                Demandas de pensión de alimentos, retención de fondos (AFP y bancos), cuidado personal, relación directa y regular (visitas) y divorcios.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_briefcase}</div>
            <div class="service-title">Acoso Laboral (Ley Karin)</div>
            <div class="service-desc">
                Intervención legal estratégica ante acoso laboral o sexual en el trabajo, tutela de derechos fundamentales y despidos por maternidad.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# FORMULARIO DE CONSULTA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 3rem; margin-bottom: 0.5rem;'>Agenda tu Consulta Confidencial</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; margin-bottom: 3rem;'>Tus datos están protegidos bajo estricto secreto profesional.</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    fc1, fc2 = st.columns(2)
    
    with fc1:
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono / WhatsApp (+56 9...)")

    with fc2:
        correo = st.text_input("Correo electrónico")
        materia = st.selectbox("Materia de la consulta", [
            "Violencia Intrafamiliar (VIF) / Alejamiento",
            "Pensión de Alimentos / Retención de Fondos",
            "Cuidado Personal / Visitas",
            "Acoso Laboral / Ley Karin",
            "Otra consulta legal"
        ])

    mensaje = st.text_area("Cuéntanos brevemente tu caso (sin tecnicismos legales)")
    
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    submitted = st.form_submit_button("Enviar consulta confidencial")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted:
        if nombre and (telefono or correo):
            st.markdown(f"""
                <div style="background-color: rgba(46, 139, 87, 0.1); border-left: 4px solid #2E8B57; padding: 1rem; color: #2E8B57; font-weight: 600; display: flex; align-items: center; gap: 10px; margin-top: 1rem; border-radius: 4px;">
                    {icon_check} Tu consulta ha sido enviada con éxito. Te contactaremos a la brevedad.
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Por favor completa tu nombre y al menos un método de contacto (Teléfono o Correo).")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(f"""
    <div style="text-align: center; font-size: 0.9rem; color: {text_muted}; padding-top: 4rem; padding-bottom: 2rem;">
        <div class="gold-line" style="width: 40px; margin-bottom: 1.5rem;"></div>
        © 2026 <b>Abogadas Hermandad</b> • Estudio Jurídico de la Mujer en Chile<br>
        <span style="font-style: italic;">Compromiso, Integridad y Defensa Legal Efectiva.</span>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SCRIPT DE AUDIO: EFECTO DE CLIC "BAMBÚ" EN BOTONES
# ---------------------------------------------------------
# Inyectamos un pequeño script de sonido en la ventana padre (donde viven los botones de Streamlit).
components.html("""
<script>
    const doc = window.parent.document;
    
    // Función para sintetizar un sonido de bambú/madera (percusivo y rápido)
    function playBambooClick() {
        const AudioContext = window.parent.AudioContext || window.parent.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        
        const osc = ctx.createOscillator();
        const gainNode = ctx.createGain();
        
        // El tipo 'triangle' o 'sine' con una caída rápida de frecuencia emula un golpe de madera
        osc.type = 'triangle';
        
        // Empieza agudo y cae rápidamente para dar efecto percusivo
        osc.frequency.setValueAtTime(600, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(150, ctx.currentTime + 0.05);
        
        // Envolvente de volumen (ataque rápido, decaimiento rápido)
        gainNode.gain.setValueAtTime(0.8, ctx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.08);
        
        osc.connect(gainNode);
        gainNode.connect(ctx.destination);
        
        osc.start();
        osc.stop(ctx.currentTime + 0.1);
    }

    // Escuchar los clics globalmente y reproducir sonido si es un botón de Streamlit
    if (!doc.bambooListenerAdded) {
        doc.addEventListener('mousedown', function(e) {
            if (e.target.closest('.stButton > button') || e.target.closest('.btn-primary > button')) {
                playBambooClick();
            }
        });
        doc.bambooListenerAdded = true;
    }
</script>
""", height=0, width=0)
