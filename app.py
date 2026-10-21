import base64
import os

import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="Abogadas Hermandad | Defensa Legal de la Mujer",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# DATOS DEL ESTUDIO
# =========================================================
PHONE_DISPLAY = "+56 9 5492 2730"
PHONE_TEL = "+56954922730"
EMAIL = "Lex.Mfrancisca@gmail.com"
WA_LINK = "https://wa.me/56954922730?text=Hola%2C%20quisiera%20agendar%20una%20consulta%20confidencial."


# =========================================================
# UTILIDADES
# =========================================================
def html(markup: str) -> None:
    """Renderiza HTML sin sangrías para que Markdown no lo convierta en bloque de código."""
    clean = "\n".join(line.strip() for line in markup.splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


def image_to_data_uri(path: str):
    if not os.path.exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().lstrip(".") or "jpeg"
    ext = "jpeg" if ext == "jpg" else ext
    with open(path, "rb") as f:
        return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"


# =========================================================
# ESTILOS
# El tema se cambia en el navegador (sin recargar la página),
# por eso la balanza puede animarse de forma continua.
# =========================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Instrument+Sans:wght@400;500;600;700&display=swap');

:root {
  --bg: #F7F4EC;
  --surface: #FFFFFF;
  --surface-2: #EFEADF;
  --line: #DCD4C3;
  --line-strong: #C4B89F;
  --ink: #15202B;
  --muted: #5D6570;
  --gold: #B08A33;
  --gold-ink: #87661C;
  --gold-soft: rgba(176,138,51,0.10);
  --wine: #7C2338;
  --nav: rgba(247,244,236,0.86);
  --shadow: rgba(21,32,43,0.08);
  --on-ink: #F7F4EC;
  --ease: cubic-bezier(.65,0,.35,1);
  --ease-out: cubic-bezier(.16,1,.3,1);
  --serif: 'Libre Caslon Display', 'Libre Caslon Text', Georgia, serif;
  --serif-text: 'Libre Caslon Text', Georgia, serif;
  --sans: 'Instrument Sans', system-ui, -apple-system, sans-serif;
}
:root[data-theme="dark"] {
  --bg: #0E141B;
  --surface: #141C25;
  --surface-2: #1A2430;
  --line: #26323F;
  --line-strong: #3A4757;
  --ink: #ECE7DC;
  --muted: #9AA3AE;
  --gold: #D4AE5E;
  --gold-ink: #DDB96B;
  --gold-soft: rgba(212,174,94,0.10);
  --wine: #E08497;
  --nav: rgba(14,20,27,0.84);
  --shadow: rgba(0,0,0,0.40);
  --on-ink: #0E141B;
}

html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
  background: var(--bg) !important;
  color: var(--ink) !important;
  font-family: var(--sans) !important;
  transition: background-color .8s var(--ease), color .8s var(--ease);
}
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding-top: 7.5rem !important; padding-bottom: 2rem !important; max-width: 1160px !important; }
::selection { background: var(--gold); color: #15202B; }
h1, h2, h3, h4 { font-family: var(--serif) !important; color: var(--ink) !important; font-weight: 400 !important; letter-spacing: -0.01em; }
p, span, li, label { color: inherit; }
a { text-decoration: none !important; color: inherit; }
a:focus-visible, button:focus-visible { outline: 2px solid var(--gold) !important; outline-offset: 3px; }

/* Transiciones de tema en todas las superficies */
.surface-t, .utility-bar, .site-nav, .practice-row, .case-card, .credential, .contact-panel, .portrait, .theme-switch {
  transition: background-color .8s var(--ease), border-color .8s var(--ease), color .8s var(--ease);
}

/* ---------- Barra de emergencia ---------- */
.utility-bar {
  position: fixed; top: 0; left: 0; right: 0; height: 36px; z-index: 1000001;
  background: var(--ink); color: var(--on-ink);
  display: flex; align-items: center; justify-content: center; gap: 1.4rem;
  font-size: .8rem; font-weight: 500;
}
.utility-bar span { color: var(--on-ink); opacity: .8; }
.utility-bar a { color: var(--on-ink) !important; font-weight: 700; border-bottom: 1px solid transparent; transition: border-color .3s; }
.utility-bar a:hover { border-color: var(--on-ink); }

/* ---------- Navegación ---------- */
.site-nav {
  position: fixed; top: 36px; left: 0; right: 0; height: 72px; z-index: 1000000;
  display: flex; align-items: center; justify-content: space-between; padding: 0 5%;
  background: var(--nav); border-bottom: 1px solid var(--line);
  backdrop-filter: saturate(140%) blur(12px); -webkit-backdrop-filter: saturate(140%) blur(12px);
  transition: height .5s var(--ease), background-color .8s var(--ease), border-color .8s var(--ease);
}
.site-nav.is-scrolled { height: 60px; }
.brand { display: flex; align-items: center; gap: 12px; }
.brand-name { font-family: var(--serif); font-size: 1.35rem; color: var(--ink); line-height: 1; }
.brand-sub { display: block; font-family: var(--sans); font-size: .7rem; color: var(--muted); margin-top: 4px; letter-spacing: .04em; }
.nav-links { display: flex; align-items: center; gap: 2rem; }
.nav-links a.nl { position: relative; font-size: .88rem; font-weight: 500; color: var(--ink); padding: 6px 0; }
.nav-links a.nl::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 1px; background: var(--gold);
  transform: scaleX(0); transform-origin: left; transition: transform .5s var(--ease); }
.nav-links a.nl:hover::after, .nav-links a.nl.active::after { transform: scaleX(1); }
.nav-cta { font-size: .86rem; font-weight: 600; padding: 10px 18px; border: 1px solid var(--ink); color: var(--ink);
  transition: background-color .4s var(--ease), color .4s var(--ease); }
.nav-cta:hover { background: var(--ink); color: var(--on-ink) !important; }

/* Interruptor de tema */
.theme-switch { display: inline-flex; align-items: center; gap: 10px; background: transparent; border: 1px solid var(--line-strong);
  padding: 6px 12px 6px 6px; cursor: pointer; font-family: var(--sans); font-size: .8rem; font-weight: 600; color: var(--ink); }
.theme-switch .track { width: 34px; height: 18px; border: 1px solid var(--line-strong); position: relative; background: var(--surface-2); }
.theme-switch .knob { position: absolute; top: 2px; left: 2px; width: 12px; height: 12px; background: var(--gold);
  transition: transform .6s var(--ease); }
:root[data-theme="dark"] .theme-switch .knob { transform: translateX(16px); }
.theme-switch .lbl-dark { display: none; }
:root[data-theme="dark"] .theme-switch .lbl-dark { display: inline; }
:root[data-theme="dark"] .theme-switch .lbl-light { display: none; }

/* ---------- Hero ---------- */
.hero { display: grid; grid-template-columns: 1.25fr 1fr; gap: 0; border: 1px solid var(--line); background: var(--surface); margin-top: 1.5rem; }
.hero-copy { padding: 4rem 3.5rem; border-right: 1px solid var(--line); }
.hero-meta { display: flex; gap: 1rem; align-items: center; font-size: .85rem; color: var(--muted); margin-bottom: 2.2rem; }
.hero-meta .rule { flex: 0 0 48px; height: 1px; background: var(--gold); transform-origin: left; animation: drawX 1.2s var(--ease) .2s both; }
.hero-title { font-family: var(--serif); font-size: clamp(2.6rem, 5vw, 4.3rem); line-height: 1.04; color: var(--ink); margin: 0 0 1.8rem; font-weight: 400; }
.hero-title .ln { display: block; overflow: hidden; }
.hero-title .ln > span { display: block; transform: translateY(100%); animation: rise 1.1s var(--ease-out) both; }
.hero-title .ln:nth-child(2) > span { animation-delay: .1s; }
.hero-title .ln:nth-child(3) > span { animation-delay: .2s; }
.hero-lead { font-family: var(--serif-text); font-size: 1.08rem; line-height: 1.8; color: var(--muted); max-width: 33rem; margin: 0 0 2.6rem;
  animation: fade .9s var(--ease) .5s both; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; animation: fade .9s var(--ease) .65s both; }
.btn { display: inline-flex; align-items: center; gap: 12px; padding: 15px 26px; font-size: .92rem; font-weight: 600; border: 1px solid var(--ink);
  transition: background-color .45s var(--ease), color .45s var(--ease), border-color .45s var(--ease); }
.btn-primary { background: var(--ink); color: var(--on-ink) !important; }
.btn-primary:hover { background: var(--gold); border-color: var(--gold); color: #15202B !important; }
.btn-secondary { background: transparent; color: var(--ink) !important; border-color: var(--line-strong); }
.btn-secondary:hover { border-color: var(--ink); }
.btn .arrow { display: inline-block; width: 18px; height: 1px; background: currentColor; position: relative; transition: width .45s var(--ease); }
.btn .arrow::after { content: ""; position: absolute; right: 0; top: -3px; width: 7px; height: 7px; border-top: 1px solid currentColor; border-right: 1px solid currentColor; transform: rotate(45deg); }
.btn:hover .arrow { width: 26px; }

.hero-facts { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line); margin-top: 3.2rem; padding-top: 1.6rem; gap: 1rem;
  animation: fade .9s var(--ease) .8s both; }
.hero-facts b { display: block; font-family: var(--serif); font-weight: 400; font-size: 1.15rem; color: var(--ink); margin-bottom: 4px; }
.hero-facts span { font-size: .82rem; color: var(--muted); line-height: 1.5; }

/* Panel de la balanza */
.scale-panel { position: relative; display: flex; flex-direction: column; justify-content: space-between; padding: 2.2rem; background: var(--surface-2);
  transition: background-color .8s var(--ease); }
.scale-panel .corner { position: absolute; width: 18px; height: 18px; border-color: var(--gold); border-style: solid; }
.scale-panel .c1 { top: 16px; left: 16px; border-width: 1px 0 0 1px; }
.scale-panel .c2 { top: 16px; right: 16px; border-width: 1px 1px 0 0; }
.scale-panel .c3 { bottom: 16px; left: 16px; border-width: 0 0 1px 1px; }
.scale-panel .c4 { bottom: 16px; right: 16px; border-width: 0 1px 1px 0; }
.scale-wrap { flex: 1; display: grid; place-items: center; cursor: pointer; padding: 1rem 0; }
.scale-svg { width: 88%; max-width: 360px; height: auto; overflow: visible; }
.scale-svg .stroke { stroke: var(--gold); transition: stroke .8s var(--ease); }
.scale-svg .fill { fill: var(--gold); transition: fill .8s var(--ease); }
.scale-svg .pan-fill { fill: var(--gold); fill-opacity: .14; }
.scale-svg .shadow-line { stroke: var(--line-strong); }

/* Brazo y platillos: equilibrio en claro, desbalance en oscuro */
.beam { transform-origin: 180px 78px; transform: rotate(0deg); transition: transform 1.6s var(--ease); }
.pan-l { transform-origin: 56px 80px; transition: transform 1.6s var(--ease); }
.pan-r { transform-origin: 304px 80px; transition: transform 1.6s var(--ease); }
:root[data-theme="dark"] .beam { transform: rotate(-13deg); }
:root[data-theme="dark"] .pan-l, :root[data-theme="dark"] .pan-r { transform: rotate(13deg); }
.scale-state { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--line-strong); padding-top: 1rem;
  font-size: .8rem; color: var(--muted); }
.scale-state .s-dark { display: none; }
:root[data-theme="dark"] .scale-state .s-dark { display: inline; }
:root[data-theme="dark"] .scale-state .s-light { display: none; }
.scale-state .angle { font-family: var(--serif); font-size: 1rem; color: var(--ink); }

@keyframes rise { to { transform: translateY(0); } }
@keyframes fade { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@keyframes drawX { from { transform: scaleX(0); } to { transform: scaleX(1); } }

/* ---------- Secciones ---------- */
.section { padding: 6rem 0 0; scroll-margin-top: 120px; }
.sec-head { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: end; margin-bottom: 2.6rem; }
.sec-head h2 { font-size: clamp(2.1rem, 3.6vw, 3.1rem) !important; line-height: 1.05; margin: 0 !important; }
.sec-head p { font-family: var(--serif-text); color: var(--muted); line-height: 1.75; font-size: 1rem; margin: 0; max-width: 30rem; justify-self: end; }
.sec-rule { height: 1px; background: var(--line-strong); margin-bottom: 0; transform-origin: left; transform: scaleX(0); transition: transform 1.4s var(--ease); }
.sec-rule.in { transform: scaleX(1); }

/* Áreas de práctica: filas tipo índice */
.practice { border-bottom: 1px solid var(--line-strong); }
.practice-row { position: relative; display: grid; grid-template-columns: 64px 1.1fr 1.6fr 40px; gap: 2rem; align-items: start;
  padding: 2.2rem 1.4rem; border-top: 1px solid var(--line); overflow: hidden; }
.practice-row:first-child { border-top: none; }
.practice-row::before { content: ""; position: absolute; inset: 0; background: var(--surface); transform: scaleY(0); transform-origin: bottom;
  transition: transform .6s var(--ease); z-index: 0; }
.practice-row::after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: var(--gold);
  transform: scaleY(0); transform-origin: top; transition: transform .6s var(--ease); }
.practice-row:hover::before, .practice-row:hover::after { transform: scaleY(1); }
.practice-row > * { position: relative; z-index: 1; }
.p-icon { width: 48px; height: 48px; border: 1px solid var(--line-strong); display: grid; place-items: center; transition: border-color .6s var(--ease); }
.practice-row:hover .p-icon { border-color: var(--gold); }
.p-icon svg { stroke: var(--gold-ink); }
.practice-row h3 { font-size: 1.75rem !important; margin: .2rem 0 0 !important; line-height: 1.15; }
.p-body p { font-family: var(--serif-text); color: var(--muted); line-height: 1.75; font-size: .97rem; margin: 0 0 1rem; }
.p-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.p-tags span { font-size: .78rem; font-weight: 500; color: var(--ink); border: 1px solid var(--line); padding: 5px 10px; }
.p-go { justify-self: end; margin-top: .6rem; width: 36px; height: 36px; border: 1px solid var(--line-strong); display: grid; place-items: center;
  transition: background-color .5s var(--ease), border-color .5s var(--ease); }
.p-go i { display: block; width: 8px; height: 8px; border-top: 1px solid var(--ink); border-right: 1px solid var(--ink); transform: rotate(45deg); margin-left: -3px; }
.practice-row:hover .p-go { background: var(--ink); border-color: var(--ink); }
.practice-row:hover .p-go i { border-color: var(--on-ink); }

/* Proceso */
.steps { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line-strong); }
.step { padding: 2.2rem 2.2rem 0 0; position: relative; }
.step::before { content: ""; position: absolute; top: -1px; left: 0; height: 2px; width: 100%; background: var(--gold);
  transform: scaleX(0); transform-origin: left; transition: transform 1s var(--ease); }
.step.in::before { transform: scaleX(1); }
.step:nth-child(2)::before { transition-delay: .35s; }
.step:nth-child(3)::before { transition-delay: .7s; }
.step-n { font-family: var(--serif); font-size: .95rem; color: var(--gold-ink); margin-bottom: 1.2rem; }
.step h4 { font-size: 1.5rem !important; margin: 0 0 .7rem !important; }
.step p { font-family: var(--serif-text); color: var(--muted); font-size: .95rem; line-height: 1.75; margin: 0; }

/* Equipo */
.team { display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 0; border: 1px solid var(--line); background: var(--surface); }
.portrait { position: relative; aspect-ratio: 4/5; overflow: hidden; background: var(--surface-2); border-right: 1px solid var(--line); }
.portrait img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%) contrast(1.05); transform: scale(1.02);
  transition: filter 1.2s var(--ease), transform 1.6s var(--ease); }
.team:hover .portrait img { filter: grayscale(0%); transform: scale(1); }
.monogram { width: 100%; height: 100%; display: grid; place-items: center; font-family: var(--serif); font-size: 6rem; color: var(--gold-ink); }
.team-body { padding: 3.5rem; display: flex; flex-direction: column; justify-content: center; }
.team-role { font-size: .85rem; font-weight: 600; color: var(--gold-ink); margin-bottom: .8rem; }
.team-body h3 { font-size: clamp(2.2rem, 3.8vw, 3rem) !important; margin: 0 0 1.4rem !important; line-height: 1.05; }
.team-bio { font-family: var(--serif-text); color: var(--muted); line-height: 1.85; font-size: 1rem; margin: 0 0 1.8rem; }
.team-quote { font-family: var(--serif-text); font-style: italic; font-size: 1.15rem; line-height: 1.6; color: var(--ink);
  border-left: 2px solid var(--gold); padding-left: 1.3rem; margin: 0 0 2.2rem; }
.team-areas { display: grid; grid-template-columns: repeat(2, 1fr); border-top: 1px solid var(--line); }
.team-areas div { padding: 1rem 0; border-bottom: 1px solid var(--line); font-size: .88rem; color: var(--ink); }
.team-areas div:nth-child(odd) { padding-right: 1rem; }

/* Casos: carrusel continuo sobrio */
.cases { overflow: hidden; border-top: 1px solid var(--line-strong); border-bottom: 1px solid var(--line-strong); }
.cases-track { display: flex; width: max-content; animation: slide 60s linear infinite; }
.cases:hover .cases-track { animation-play-state: paused; }
@keyframes slide { to { transform: translateX(-50%); } }
.case-card { width: 360px; flex-shrink: 0; white-space: normal; padding: 2.2rem 2rem; border-right: 1px solid var(--line); background: transparent; }
.case-card:hover { background: var(--surface); }
.case-cat { font-size: .78rem; font-weight: 600; color: var(--gold-ink); margin-bottom: 1rem; display: flex; align-items: center; gap: 10px; }
.case-cat::before { content: ""; width: 16px; height: 1px; background: var(--gold); }
.case-card h4 { font-size: 1.45rem !important; margin: 0 0 .7rem !important; line-height: 1.2; }
.case-card p { font-family: var(--serif-text); font-size: .9rem; color: var(--muted); line-height: 1.7; margin: 0; }
.note { font-size: .78rem; color: var(--muted); margin-top: 1rem; }

/* Formación */
.credentials { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--line); background: var(--surface); }
.credential { border-right: 1px solid var(--line); }
.credential:last-child { border-right: none; }
.cred-img { height: 200px; overflow: hidden; border-bottom: 1px solid var(--line); }
.cred-img img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%); transition: filter 1s var(--ease), transform 1.4s var(--ease); }
.credential:hover .cred-img img { filter: grayscale(0%); transform: scale(1.04); }
.cred-body { padding: 1.8rem; }
.cred-body small { font-size: .78rem; font-weight: 600; color: var(--gold-ink); }
.cred-body h4 { font-size: 1.35rem !important; margin: .5rem 0 .6rem !important; line-height: 1.2; }
.cred-body p { font-family: var(--serif-text); color: var(--muted); font-size: .9rem; line-height: 1.7; margin: 0; }

/* Contacto */
.contact-panel { background: var(--ink); color: var(--on-ink); padding: 2.6rem; height: 100%; display: flex; flex-direction: column; gap: 1.6rem; }
.contact-panel h3 { color: var(--on-ink) !important; font-size: 2rem !important; margin: 0 !important; line-height: 1.1; }
.contact-panel p { font-family: var(--serif-text); color: var(--on-ink); opacity: .78; line-height: 1.75; margin: 0; font-size: .95rem; }
.c-line { display: flex; flex-direction: column; gap: 4px; padding: 1rem 0; border-top: 1px solid rgba(127,127,127,.35); }
.c-line small { font-size: .76rem; opacity: .65; color: var(--on-ink); }
.c-line a { color: var(--on-ink) !important; font-size: 1.02rem; font-weight: 600; transition: color .4s var(--ease); }
.c-line a:hover { color: var(--gold) !important; }
.c-lock { display: flex; gap: 10px; align-items: flex-start; font-size: .82rem; color: var(--on-ink); opacity: .8; margin-top: auto; line-height: 1.6; }

[data-testid="stForm"] { background: var(--surface) !important; border: 1px solid var(--line) !important; border-radius: 0 !important; padding: 2.4rem !important;
  transition: background-color .8s var(--ease), border-color .8s var(--ease); }
[data-testid="stForm"] label p { font-family: var(--sans) !important; font-weight: 600 !important; font-size: .82rem !important; color: var(--ink) !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div {
  background: var(--bg) !important; color: var(--ink) !important; border-radius: 0 !important; border: 1px solid var(--line) !important;
  font-family: var(--sans) !important; transition: border-color .4s var(--ease), background-color .8s var(--ease); }
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder { color: var(--muted) !important; opacity: .7; }
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus { border-color: var(--gold) !important; box-shadow: none !important; }
[data-testid="stTextInput"] > div > div, [data-testid="stTextArea"] > div > div { border: none !important; background: transparent !important; border-radius: 0 !important; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color: var(--ink) !important; }
[data-baseweb="popover"] ul, [data-baseweb="popover"] li { background: var(--surface) !important; color: var(--ink) !important; }
[data-testid="stFormSubmitButton"] > button {
  width: 100%; background: var(--ink) !important; color: var(--on-ink) !important; border: 1px solid var(--ink) !important; border-radius: 0 !important;
  padding: .95rem 2rem !important; font-weight: 600 !important; transition: background-color .45s var(--ease), border-color .45s var(--ease) !important; }
[data-testid="stFormSubmitButton"] > button p { color: var(--on-ink) !important; font-family: var(--sans) !important; }
[data-testid="stFormSubmitButton"] > button:hover { background: var(--gold) !important; border-color: var(--gold) !important; }
[data-testid="stFormSubmitButton"] > button:hover p { color: #15202B !important; }
.success { display: flex; gap: 12px; align-items: center; padding: 1rem 1.2rem; margin-top: 1rem; border: 1px solid #2E8B57; border-left-width: 3px;
  color: #2E8B57; font-weight: 600; font-size: .92rem; animation: fade .6s var(--ease) both; }

/* Footer */
.site-footer { margin-top: 6rem; border-top: 1px solid var(--line-strong); padding: 2.4rem 0 1rem;
  display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 2rem; font-size: .86rem; color: var(--muted); }
.site-footer b { display: block; font-family: var(--serif); font-weight: 400; font-size: 1.3rem; color: var(--ink); margin-bottom: .4rem; }
.site-footer a { color: var(--ink); }
.site-footer a:hover { color: var(--gold-ink); }
.footer-col div { margin-bottom: .4rem; }

/* WhatsApp */
.wa-float { position: fixed; right: 24px; bottom: 24px; z-index: 1000000; display: flex; align-items: center; gap: 10px;
  background: var(--ink); color: var(--on-ink) !important; padding: 12px 16px; font-size: .85rem; font-weight: 600;
  border: 1px solid var(--ink); box-shadow: 0 14px 34px var(--shadow); transition: background-color .45s var(--ease), color .45s var(--ease); }
.wa-float svg { fill: #25D366; }
.wa-float:hover { background: var(--surface); color: var(--ink) !important; }

/* Revelado al hacer scroll (sobrio) */
.js .reveal { opacity: 0; transform: translateY(18px); transition: opacity .9s var(--ease), transform .9s var(--ease); }
.js .reveal.in { opacity: 1; transform: none; }

/* Responsive */
@media (max-width: 960px) {
  .hero, .team, .credentials { grid-template-columns: 1fr; }
  .hero-copy { padding: 2.6rem 1.6rem; border-right: none; border-bottom: 1px solid var(--line); }
  .portrait { border-right: none; border-bottom: 1px solid var(--line); aspect-ratio: 1; }
  .team-body { padding: 2.2rem 1.6rem; }
  .credential { border-right: none; border-bottom: 1px solid var(--line); }
  .sec-head { grid-template-columns: 1fr; gap: 1rem; }
  .sec-head p { justify-self: start; }
  .practice-row { grid-template-columns: 48px 1fr; gap: 1rem 1.2rem; }
  .practice-row .p-body { grid-column: 1 / -1; }
  .p-go { display: none; }
  .steps { grid-template-columns: 1fr; }
  .step { padding-right: 0; padding-bottom: 1.6rem; }
  .nav-links a.nl { display: none; }
  .hero-facts { grid-template-columns: 1fr; }
  .site-footer { grid-template-columns: 1fr; }
  .utility-bar { gap: .8rem; font-size: .74rem; }
  .utility-bar .hide-sm { display: none; }
  .wa-float span { display: none; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  .js .reveal { opacity: 1; transform: none; }
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

# =========================================================
# ÍCONOS
# =========================================================
def icon(paths: str, size: int = 24) -> str:
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')

logo_svg = """<svg width="34" height="34" viewBox="0 0 36 36" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
<rect x="1" y="1" width="34" height="34" style="stroke:var(--gold)" stroke-width="1.2"/>
<path d="M18 8v20M12 28h12M10 13h16M10 13l-3 7h6l-3-7zM26 13l-3 7h6l-3-7z" style="stroke:var(--gold)" stroke-width="1.3"/></svg>"""

icon_shield = icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>')
icon_family = icon('<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M3 20v-1a5 5 0 0 1 10 0v1"/><path d="M14 20v-.5a3.5 3.5 0 0 1 7 0v.5"/>')
icon_work = icon('<rect x="3" y="7" width="18" height="13"/><path d="M16 7V4H8v3"/><path d="M3 13h18"/>')
icon_lock = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="4" y="11" width="16" height="10"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
icon_check = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2.2" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
icon_wa = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5a9.45 9.45 0 0 1-4.82-1.32l-.35-.21-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.47 9.48-9.47a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.7c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.53A11.32 11.32 0 0 0 12.04.64C5.76.64.65 5.75.65 12.03c0 2.01.52 3.97 1.52 5.7L.55 23.6l6.02-1.58a11.36 11.36 0 0 0 5.47 1.39c6.28 0 11.39-5.11 11.39-11.39 0-3.04-1.18-5.9-3.34-8.05z"/></svg>'

# Balanza: el brazo gira desde el pivote y los platillos contrarrotan para colgar siempre verticales
scale_svg = """
<svg class="scale-svg" viewBox="0 0 360 330" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <line class="shadow-line" x1="60" y1="300" x2="300" y2="300" stroke-width="1"/>
  <path class="stroke" d="M180 70v214" stroke-width="3"/>
  <path class="stroke" d="M128 296h104M146 296l34-14 34 14" stroke-width="3"/>
  <rect class="stroke" x="174" y="40" width="12" height="12" stroke-width="2"/>
  <g class="beam">
    <path class="stroke" d="M44 78h272" stroke-width="3.5"/>
    <circle class="fill" cx="180" cy="78" r="6"/>
    <g class="pan-l">
      <path class="stroke" d="M56 80l-34 92M56 80l34 92" stroke-width="1.4"/>
      <path class="stroke pan-fill" d="M14 172h84c0 18-19 30-42 30s-42-12-42-30z" stroke-width="2"/>
    </g>
    <g class="pan-r">
      <path class="stroke" d="M304 80l-34 92M304 80l34 92" stroke-width="1.4"/>
      <path class="stroke pan-fill" d="M262 172h84c0 18-19 30-42 30s-42-12-42-30z" stroke-width="2"/>
    </g>
  </g>
</svg>"""

# =========================================================
# BARRA DE EMERGENCIA + NAVEGACIÓN + WHATSAPP
# =========================================================
html(f"""
<div class="utility-bar" role="note">
  <span class="hide-sm">Si estás en riesgo inminente:</span>
  <a href="tel:149">149 Fono Familia Carabineros</a>
  <a href="tel:1455">1455 SernamEG</a>
</div>
<nav class="site-nav" aria-label="Navegación principal">
  <a class="brand" href="#inicio" data-scroll="inicio">{logo_svg}
    <span><span class="brand-name">Abogadas Hermandad</span><span class="brand-sub">Estudio jurídico de la mujer</span></span>
  </a>
  <div class="nav-links">
    <a class="nl" href="#areas" data-scroll="areas">Áreas</a>
    <a class="nl" href="#proceso" data-scroll="proceso">Proceso</a>
    <a class="nl" href="#equipo" data-scroll="equipo">Equipo</a>
    <a class="nl" href="#casos" data-scroll="casos">Casos</a>
    <button class="theme-switch" type="button" data-theme-toggle aria-label="Cambiar tema" aria-pressed="false">
      <span class="track"><span class="knob"></span></span>
      <span class="lbl-light">Claro</span><span class="lbl-dark">Oscuro</span>
    </button>
    <a class="nav-cta" href="#contacto" data-scroll="contacto">Agendar consulta</a>
  </div>
</nav>
<a class="wa-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}<span>WhatsApp</span></a>
""")

# =========================================================
# HERO
# =========================================================
html(f"""
<section class="hero" id="inicio">
  <div class="hero-copy">
    <div class="hero-meta"><span class="rule"></span><span>Santiago · Atención en todo Chile</span></div>
    <h1 class="hero-title">
      <span class="ln"><span>Defensa legal</span></span>
      <span class="ln"><span>especializada, humana</span></span>
      <span class="ln"><span>y sin prejuicios.</span></span>
    </h1>
    <p class="hero-lead">Representamos a mujeres en violencia intrafamiliar, derecho de familia y acoso laboral, con rigor técnico, absoluta confidencialidad y explicaciones claras en cada etapa.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#contacto" data-scroll="contacto">Agendar consulta confidencial <span class="arrow"></span></a>
      <a class="btn btn-secondary" href="tel:{PHONE_TEL}">Llamar {PHONE_DISPLAY}</a>
    </div>
    <div class="hero-facts">
      <div><b>Confidencialidad</b><span>Protegida por secreto profesional</span></div>
      <div><b>Medidas urgentes</b><span>Tramitación prioritaria en casos VIF</span></div>
      <div><b>Lenguaje claro</b><span>Sabrás siempre en qué está tu causa</span></div>
    </div>
  </div>
  <div class="scale-panel">
    <span class="corner c1"></span><span class="corner c2"></span><span class="corner c3"></span><span class="corner c4"></span>
    <div class="scale-wrap" data-theme-toggle title="Cambiar tema">{scale_svg}</div>
    <div class="scale-state">
      <span><span class="s-light">Modo claro · en equilibrio</span><span class="s-dark">Modo oscuro · fuera de equilibrio</span></span>
      <span class="angle"><span class="s-light">0°</span><span class="s-dark">13°</span></span>
    </div>
  </div>
</section>
""")

# =========================================================
# ÁREAS DE PRÁCTICA
# =========================================================
areas = [
    (icon_shield, "Protección y violencia intrafamiliar",
     "Tramitación prioritaria de medidas cautelares y acciones penales para resguardar tu integridad y la de tu familia.",
     ["Prohibición de acercamiento", "Salida del agresor del hogar", "Querellas por lesiones"]),
    (icon_family, "Derecho de familia",
     "Representación completa en los procesos que definen el bienestar de tus hijos y la estabilidad de tu hogar.",
     ["Pensión de alimentos", "Retención de fondos AFP", "Cuidado personal", "Relación directa y regular", "Divorcio"]),
    (icon_work, "Acoso laboral y Ley Karin",
     "Intervención estratégica ante acoso laboral o sexual y vulneración de derechos fundamentales en el trabajo.",
     ["Tutela de derechos", "Despido indirecto", "Despido por maternidad"]),
]
rows = "".join(
    f"""<a class="practice-row reveal" href="#contacto" data-scroll="contacto">
      <div class="p-icon">{ic}</div>
      <h3>{t}</h3>
      <div class="p-body"><p>{d}</p><div class="p-tags">{''.join(f'<span>{x}</span>' for x in tags)}</div></div>
      <div class="p-go"><i></i></div>
    </a>"""
    for ic, t, d, tags in areas
)
html(f"""
<section class="section" id="areas">
  <div class="sec-head reveal">
    <h2>Áreas de práctica</h2>
    <p>Tres especialidades con un mismo método: estrategia jurídica precisa y acompañamiento cercano durante todo el proceso.</p>
  </div>
  <div class="sec-rule"></div>
  <div class="practice">{rows}</div>
</section>
""")

# =========================================================
# PROCESO
# =========================================================
steps = [
    ("Primera conversación", "Nos cuentas tu situación de forma confidencial. Evaluamos riesgos, plazos y alternativas reales."),
    ("Estrategia y presupuesto", "Te proponemos un plan de acción concreto, con etapas y costos explicados sin tecnicismos."),
    ("Representación judicial", "Llevamos tu causa ante tribunales y te informamos de cada avance relevante."),
]
steps_html = "".join(
    f"""<div class="step"><div class="step-n">Paso {i + 1}</div><h4>{t}</h4><p>{d}</p></div>"""
    for i, (t, d) in enumerate(steps)
)
html(f"""
<section class="section" id="proceso">
  <div class="sec-head reveal">
    <h2>Cómo trabajamos</h2>
    <p>Un proceso ordenado para que tomes cada decisión con información y respaldo.</p>
  </div>
  <div class="steps" data-steps>{steps_html}</div>
</section>
""")

# =========================================================
# EQUIPO
# =========================================================
photo = image_to_data_uri("fran.jpg")
portrait = (f'<img src="{photo}" alt="Retrato de María-Francisca Valentina" />'
            if photo else '<div class="monogram">MF</div>')
html(f"""
<section class="section" id="equipo">
  <div class="sec-head reveal">
    <h2>Equipo</h2>
    <p>Atención directa con la abogada a cargo de tu causa, desde la primera reunión hasta la sentencia.</p>
  </div>
  <div class="team reveal">
    <div class="portrait">{portrait}</div>
    <div class="team-body">
      <div class="team-role">Abogada fundadora</div>
      <h3>María-Francisca Valentina</h3>
      <p class="team-bio">Especialista en violencia de género, derecho de familia, penal y laboral. Combina litigación técnica con un acompañamiento humano para la protección integral de los derechos de sus clientas.</p>
      <blockquote class="team-quote">Ninguna mujer debería enfrentar sola un proceso judicial. Mi trabajo es que tengas claridad y respaldo en cada decisión.</blockquote>
      <div class="team-areas">
        <div>Violencia de género</div><div>Derecho de familia</div>
        <div>Derecho penal</div><div>Derecho laboral</div>
      </div>
    </div>
  </div>
</section>
""")

# =========================================================
# CASOS DESTACADOS
# =========================================================
cases = [
    ("Protección y VIF", "Medida cautelar en 24 horas",
     "Prohibición de acercamiento y salida del agresor del hogar común, otorgadas por el Juzgado de Familia de Santiago."),
    ("Pensión de alimentos", "Retención de fondos AFP",
     "Cobro de una deuda histórica superior a $14.000.000 mediante retención judicial de fondos previsionales."),
    ("Tutela laboral", "Acoso laboral, Ley Karin",
     "Sentencia favorable con indemnización por vulneración de derechos fundamentales y despido indirecto."),
    ("Derecho de familia", "Cuidado personal definitivo",
     "Resolución que resguarda el interés superior del niño, con régimen de visitas y evaluación psicológica."),
    ("Derecho penal", "Querella por lesiones VIF",
     "Condena firme del Tribunal de Juicio Oral en lo Penal con prohibición absoluta de contacto."),
]
case_cards = "".join(
    f"""<article class="case-card"><div class="case-cat">{c}</div><h4>{t}</h4><p>{d}</p></article>"""
    for c, t, d in cases
)
html(f"""
<section class="section" id="casos">
  <div class="sec-head reveal">
    <h2>Casos destacados</h2>
    <p>Resoluciones obtenidas para nuestras clientas. Pasa el cursor sobre el listado para detenerlo.</p>
  </div>
  <div class="cases reveal"><div class="cases-track">{case_cards}{case_cards}</div></div>
  <p class="note">Casos anonimizados. Los resultados anteriores no garantizan resultados futuros.</p>
</section>
""")

# =========================================================
# FORMACIÓN
# =========================================================
credentials = [
    ("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=800&auto=format&fit=crop",
     "Universidad de Chile", "Diplomado en Derecho de Familia",
     "Litigación oral y medidas cautelares en tribunales de familia."),
    ("https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=800&auto=format&fit=crop",
     "Pontificia Universidad Católica", "Certificación en Ley Karin y género",
     "Prevención, tutela de derechos fundamentales y acoso laboral."),
    ("https://images.unsplash.com/photo-1450133064473-71024230f91b?q=80&w=800&auto=format&fit=crop",
     "Academia Judicial / UDP", "Postítulo en Derecho Penal y VIF",
     "Estrategia penal y querellas por agresiones graves."),
]
cred_html = "".join(
    f"""<article class="credential"><div class="cred-img"><img src="{img}" alt="{t}" loading="lazy"/></div>
    <div class="cred-body"><small>{inst}</small><h4>{t}</h4><p>{d}</p></div></article>"""
    for img, inst, t, d in credentials
)
html(f"""
<section class="section" id="formacion">
  <div class="sec-head reveal">
    <h2>Formación académica</h2>
    <p>Especialización continua en las materias que defendemos ante tribunales.</p>
  </div>
  <div class="credentials reveal">{cred_html}</div>
</section>
""")

# =========================================================
# CONTACTO
# =========================================================
html("""
<section class="section" id="contacto">
  <div class="sec-head reveal">
    <h2>Agenda tu consulta</h2>
    <p>Cuéntanos lo esencial. Te respondemos personalmente por el medio que prefieras.</p>
  </div>
</section>
""")

col_info, col_form = st.columns([1, 1.5], gap="small")

with col_info:
    html(f"""
    <div class="contact-panel reveal">
      <h3>Hablemos con total reserva</h3>
      <p>La primera conversación sirve para entender tu situación y explicarte tus opciones, sin compromiso.</p>
      <div>
        <div class="c-line"><small>Teléfono y WhatsApp</small><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
        <div class="c-line"><small>Correo electrónico</small><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="c-line"><small>Emergencias VIF</small><a href="tel:149">149 Carabineros</a><a href="tel:1455">1455 SernamEG</a></div>
      </div>
      <div class="c-lock">{icon_lock}<span>Toda la información que compartas está protegida por secreto profesional y no se comparte con terceros.</span></div>
    </div>
    """)

with col_form:
    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            nombre = st.text_input("Nombre completo", placeholder="Tu nombre")
            telefono = st.text_input("Teléfono o WhatsApp", placeholder="+56 9 ...")
        with c2:
            correo = st.text_input("Correo electrónico", placeholder="nombre@correo.cl")
            materia = st.selectbox("Materia", [
                "Violencia intrafamiliar / Medidas de protección",
                "Pensión de alimentos / Retención de fondos",
                "Cuidado personal / Visitas",
                "Acoso laboral / Ley Karin",
                "Otra consulta legal",
            ])
        mensaje = st.text_area("Describe brevemente tu caso", placeholder="No necesitas usar términos legales.", height=140)
        submitted = st.form_submit_button("Enviar consulta confidencial")

        if submitted:
            if nombre and (telefono or correo):
                html(f'<div class="success">{icon_check}<span>Consulta enviada. Te contactaremos a la brevedad.</span></div>')
            else:
                st.error("Indica tu nombre y al menos un medio de contacto (teléfono o correo) para poder responderte.")

# =========================================================
# FOOTER
# =========================================================
html(f"""
<footer class="site-footer">
  <div class="footer-col"><b>Abogadas Hermandad</b><div>Estudio jurídico de la mujer en Chile.</div><div>© 2026 Todos los derechos reservados.</div></div>
  <div class="footer-col"><div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
  <div class="footer-col"><div><a href="#areas" data-scroll="areas">Áreas de práctica</a></div><div><a href="#equipo" data-scroll="equipo">Equipo</a></div><div><a href="#contacto" data-scroll="contacto">Agendar consulta</a></div></div>
</footer>
""")

# =========================================================
# INTERACCIONES
# Tema sin recarga (balanza animada), scroll suave, navbar,
# revelado al hacer scroll y sonido de clic en madera.
# =========================================================
components.html("""
<script>
(function () {
  const win = window.parent;
  const doc = win.document;
  const root = doc.documentElement;
  const reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Tema ----------
  function applyTheme(t) {
    root.setAttribute('data-theme', t);
    doc.querySelectorAll('.theme-switch').forEach(b => b.setAttribute('aria-pressed', t === 'dark'));
    try { win.localStorage.setItem('hermandad-theme', t); } catch (e) {}
  }
  let saved = 'light';
  try { saved = win.localStorage.getItem('hermandad-theme') || 'light'; } catch (e) {}
  if (!root.getAttribute('data-theme')) applyTheme(saved);

  // ---------- Revelado al hacer scroll ----------
  root.classList.add('js');
  if (!win.__hhIO) {
    win.__hhIO = new win.IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        if (el.hasAttribute('data-steps')) el.querySelectorAll('.step').forEach(s => s.classList.add('in'));
        el.classList.add('in');
        win.__hhIO.unobserve(el);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
  }
  const observe = () => doc.querySelectorAll('.reveal:not(.in), .sec-rule:not(.in), [data-steps]:not(.in)').forEach(el => {
    if (reduce) { el.classList.add('in'); el.querySelectorAll && el.querySelectorAll('.step').forEach(s => s.classList.add('in')); }
    else win.__hhIO.observe(el);
  });
  observe();
  if (!win.__hhMO) {
    win.__hhMO = new win.MutationObserver(observe);
    win.__hhMO.observe(doc.body, { childList: true, subtree: true });
  }

  if (win.__hhInit) return;
  win.__hhInit = true;

  // ---------- Sonido de clic en madera ----------
  let ctx = null;
  function woodClick() {
    const AC = win.AudioContext || win.webkitAudioContext;
    if (!AC) return;
    ctx = ctx || new AC();
    const t = ctx.currentTime;
    const tone = (f0, f1, g, d) => {
      const o = ctx.createOscillator(), gn = ctx.createGain();
      o.type = 'sine';
      o.frequency.setValueAtTime(f0, t);
      o.frequency.exponentialRampToValueAtTime(f1, t + d * 0.85);
      gn.gain.setValueAtTime(g, t);
      gn.gain.exponentialRampToValueAtTime(0.001, t + d);
      o.connect(gn); gn.connect(ctx.destination); o.start(t); o.stop(t + d + 0.01);
    };
    tone(1050, 400, 0.5, 0.04);
    tone(1600, 800, 0.2, 0.025);
  }

  // ---------- Clics: tema y scroll suave ----------
  doc.addEventListener('click', (e) => {
    const toggle = e.target.closest('[data-theme-toggle]');
    if (toggle) {
      e.preventDefault();
      applyTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
      woodClick();
      return;
    }
    const link = e.target.closest('[data-scroll]');
    if (link) {
      const target = doc.getElementById(link.dataset.scroll);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }
  });

  doc.addEventListener('mousedown', (e) => {
    if (e.target.closest('[data-testid="stFormSubmitButton"] button, .btn-primary, .nav-cta')) woodClick();
  });

  // ---------- Navbar compacta y enlace activo ----------
  const ids = ['areas', 'proceso', 'equipo', 'casos', 'contacto'];
  let ticking = false;
  doc.addEventListener('scroll', (e) => {
    if (ticking) return;
    ticking = true;
    win.requestAnimationFrame(() => {
      const el = e.target === doc ? doc.scrollingElement : e.target;
      const y = el && el.scrollTop ? el.scrollTop : 0;
      const nav = doc.querySelector('.site-nav');
      if (nav) nav.classList.toggle('is-scrolled', y > 40);
      let current = null;
      ids.forEach(id => { const s = doc.getElementById(id); if (s && s.getBoundingClientRect().top < 200) current = id; });
      doc.querySelectorAll('.nav-links a.nl').forEach(a => a.classList.toggle('active', a.dataset.scroll === current));
      ticking = false;
    });
  }, true);
})();
</script>
""", height=0, width=0)
