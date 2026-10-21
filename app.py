import base64
import os

import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN
# =========================================================
BRAND = "Hermanas Hermandad"
PHONE_DISPLAY = "+56 9 5492 2730"
PHONE_TEL = "+56954922730"
EMAIL = "Lex.Mfrancisca@gmail.com"
WA_LINK = "https://wa.me/56954922730?text=Hola%2C%20quisiera%20agendar%20una%20consulta%20confidencial."

st.set_page_config(
    page_title=f"{BRAND} | Estudio Jurídico de la Mujer",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# UTILIDADES
# =========================================================
def html(markup: str) -> None:
    """Renderiza HTML sin sangrías (evita que Markdown lo convierta en bloque de código)."""
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
# Paleta mate: beige, blanco, dorado envejecido y texto negro.
# Tema oscuro: azul noche mate, dorado y texto blanco.
# Movimiento reservado para la balanza y el interruptor de tema.
# =========================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&display=swap');

:root {
  --bg: #F5F1E8;
  --band: #ECE5D6;
  --surface: #FFFFFF;
  --line: #DDD3C0;
  --line-2: #C8BBA2;
  --ink: #161514;
  --muted: #57524A;
  --gold: #A8843F;
  --gold-d: #85672F;
  --btn: #161514;
  --btn-ink: #FFFFFF;
  --deep: #1E1C19;
  --deep-ink: #F5F1E8;
  --r: 4px;
  --ease: cubic-bezier(.45,0,.2,1);
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --alert-h: 44px;
}
:root[data-theme="dark"] {
  --bg: #12161F;
  --band: #171C27;
  --surface: #1B212D;
  --line: #2B3242;
  --line-2: #3A4356;
  --ink: #F4F1EA;
  --muted: #B6B1A7;
  --gold: #C9A45A;
  --gold-d: #D8B670;
  --btn: #C9A45A;
  --btn-ink: #12161F;
  --deep: #0D1017;
  --deep-ink: #F4F1EA;
}
:root.alert-closed { --alert-h: 0px; }

html, body, .stApp { background: var(--bg) !important; color: var(--ink) !important; font-family: var(--sans) !important;
  -webkit-font-smoothing: antialiased; transition: background-color .8s var(--ease), color .8s var(--ease); }
[data-testid="stAppViewContainer"], [data-testid="stMain"] { background: transparent !important; }
html, [data-testid="stMain"], [data-testid="stAppViewContainer"] { scroll-behavior: smooth; }
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding: calc(var(--alert-h) + 76px) 0 0 !important; max-width: 100% !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
::selection { background: var(--gold); color: #FFFFFF; }
h1, h2, h3, h4 { font-family: var(--serif) !important; color: var(--ink) !important; font-weight: 600 !important; letter-spacing: -0.005em; margin: 0; }
p { margin: 0; }
a { text-decoration: none !important; color: inherit; }
a:focus-visible, button:focus-visible { outline: 2px solid var(--gold) !important; outline-offset: 3px; }
::view-transition-old(root), ::view-transition-new(root) { animation-duration: .8s; animation-timing-function: var(--ease); }

.wrap { max-width: 1120px; margin: 0 auto; padding: 0 32px; }
.t { transition: background-color .8s var(--ease), border-color .8s var(--ease), color .8s var(--ease); }

/* ---------- Alerta de peligro inminente ---------- */
.alert-bar { position: fixed; top: 0; left: 0; right: 0; height: 44px; z-index: 1000002; isolation: isolate;
  display: flex; align-items: center; justify-content: center; gap: 12px; padding: 0 56px;
  background: #9E1422; color: #FFFFFF; font-size: .86rem; font-weight: 500; }
.alert-bar::before { content: ""; position: absolute; inset: 0; background: #C41E30; z-index: -1; animation: blink 1.2s steps(1, end) infinite; }
@keyframes blink { 50% { opacity: 0; } }
:root.alert-closed .alert-bar { display: none; }
.alert-bar strong { font-weight: 600; color: #FFFFFF; }
.alert-bar span { color: #FFFFFF; }
.alert-bar a { color: #FFFFFF !important; font-weight: 600; border-bottom: 1px solid rgba(255,255,255,.7); padding-bottom: 1px; white-space: nowrap; }
.alert-bar .sep { opacity: .5; }
.alert-close { position: absolute; right: 16px; top: 50%; transform: translateY(-50%); width: 28px; height: 28px; border: 1px solid rgba(255,255,255,.6);
  border-radius: 2px; background: transparent; color: #FFFFFF; font-size: 16px; line-height: 1; cursor: pointer; display: grid; place-items: center; }
.alert-close:hover { background: rgba(255,255,255,.15); }

/* ---------- Encabezado ---------- */
.site-header { position: fixed; top: var(--alert-h); left: 0; right: 0; height: 76px; z-index: 1000001;
  background: var(--surface); border-bottom: 1px solid var(--line); }
.site-header .wrap { height: 100%; display: flex; align-items: center; justify-content: space-between; }
.brand { display: flex; align-items: center; gap: 14px; }
.brand svg { width: 42px; height: 42px; flex-shrink: 0; }
.brand-name { display: block; font-family: var(--serif); font-size: 1.45rem; font-weight: 700; color: var(--ink); line-height: 1; letter-spacing: .02em; }
.brand-sub { display: block; font-size: .7rem; color: var(--muted); margin-top: 5px; letter-spacing: .08em; }
.nav { display: flex; align-items: center; gap: 28px; }
.nav a.nl { font-size: .86rem; font-weight: 500; color: var(--ink); padding: 6px 0; border-bottom: 1px solid transparent; transition: border-color .3s, color .3s; }
.nav a.nl:hover { border-color: var(--gold); color: var(--gold-d); }
.btn { display: inline-flex; align-items: center; gap: 10px; padding: 13px 22px; border-radius: var(--r); font-size: .88rem; font-weight: 600;
  border: 1px solid var(--btn); background: var(--btn); color: var(--btn-ink) !important; transition: background-color .3s, color .3s, border-color .3s; }
.btn:hover { background: var(--gold); border-color: var(--gold); color: #FFFFFF !important; }
.btn.ghost { background: transparent; color: var(--ink) !important; border-color: var(--line-2); }
.btn.ghost:hover { border-color: var(--ink); background: transparent; color: var(--ink) !important; }
.btn svg { stroke: currentColor; }

/* ---------- Portada ---------- */
.hero { background: var(--band); border-bottom: 1px solid var(--line); padding: 64px 0 0; text-align: center; }
.scale-wrap { width: 340px; max-width: 80vw; margin: 0 auto; }
.scale-wrap svg { width: 100%; height: auto; display: block; overflow: visible; }
.hero .rule { width: 48px; height: 1px; background: var(--gold); margin: 36px auto 28px; }
.hero h1 { font-size: clamp(2.5rem, 5vw, 4rem) !important; line-height: 1.08; max-width: 18ch; margin: 0 auto 22px; }
.hero h1 em { font-style: italic; font-weight: 500; color: var(--gold-d); }
.hero .lead { font-size: 1.05rem; line-height: 1.75; color: var(--muted); max-width: 40rem; margin: 0 auto 32px; }
.hero .actions { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; margin-bottom: 56px; }
.facts { display: grid; grid-template-columns: repeat(3, 1fr); background: var(--surface); border-top: 1px solid var(--line); }
.facts div { padding: 26px 24px; text-align: center; font-size: .86rem; color: var(--muted); }
.facts div + div { border-left: 1px solid var(--line); }
.facts b { display: block; font-family: var(--serif); font-size: 1.25rem; font-weight: 600; color: var(--ink); margin-bottom: 4px; }

/* Balanza: movimiento al cambiar de tema */
.beam, .pan-l, .pan-r, .fab-beam, .fab-pan-l, .fab-pan-r { transition: transform 1.6s var(--ease); }
.beam { transform-origin: 160px 70px; }
.pan-l { transform-origin: 44px 78px; }
.pan-r { transform-origin: 276px 78px; }
:root[data-theme="dark"] .beam { transform: rotate(-10deg); }
:root[data-theme="dark"] .pan-l, :root[data-theme="dark"] .pan-r { transform: rotate(10deg); }

/* ---------- Secciones ---------- */
.section { padding: 96px 0; border-bottom: 1px solid var(--line); scroll-margin-top: 130px; }
.section.alt { background: var(--surface); }
.split { display: grid; grid-template-columns: 320px 1fr; gap: 64px; }
.sec-title .eyebrow { display: block; font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; margin-bottom: 14px; }
.sec-title h2 { font-size: clamp(2rem, 3.4vw, 2.7rem) !important; line-height: 1.1; margin-bottom: 18px; }
.sec-title p { font-size: .98rem; line-height: 1.75; color: var(--muted); }
.sec-title.center { text-align: center; max-width: 40rem; margin: 0 auto 56px; }

/* Áreas: filas */
.rows { border-top: 1px solid var(--ink); }
.row { display: grid; grid-template-columns: 48px 1fr; gap: 24px; padding: 30px 0; border-bottom: 1px solid var(--line); }
.row svg { stroke: var(--gold); }
.row h3 { font-size: 1.6rem !important; margin-bottom: 8px; }
.row p { color: var(--muted); line-height: 1.7; font-size: .95rem; margin-bottom: 12px; }
.row .items { font-size: .86rem; color: var(--ink); line-height: 1.7; }
.row .items span + span::before { content: "  /  "; color: var(--line-2); white-space: pre; }

/* Proceso */
.steps { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--ink); }
.step { padding: 32px 32px 0 0; }
.step + .step { padding-left: 32px; border-left: 1px solid var(--line); }
.step .n { font-family: var(--serif); font-size: 2.4rem; color: var(--gold); line-height: 1; margin-bottom: 18px; }
.step h4 { font-size: 1.4rem !important; margin-bottom: 10px; }
.step p { color: var(--muted); font-size: .94rem; line-height: 1.7; }

/* Equipo */
.team { display: grid; grid-template-columns: 380px 1fr; gap: 64px; align-items: start; }
.portrait { aspect-ratio: 4/5; background: var(--band); border: 1px solid var(--line); padding: 10px; }
.portrait img { width: 100%; height: 100%; object-fit: cover; display: block; filter: saturate(.85); }
.monogram { width: 100%; height: 100%; display: grid; place-items: center; font-family: var(--serif); font-size: 5.5rem; color: var(--gold); background: var(--surface); }
.team .role { font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; }
.team h3 { font-size: clamp(2.1rem, 3.6vw, 2.8rem) !important; margin: 10px 0 20px; line-height: 1.08; }
.team .bio { color: var(--muted); line-height: 1.8; font-size: 1rem; margin-bottom: 28px; }
.quote { border-left: 2px solid var(--gold); padding-left: 22px; font-family: var(--serif); font-style: italic; font-size: 1.35rem; line-height: 1.5; color: var(--ink); margin: 0 0 32px; }
.areas-list { display: grid; grid-template-columns: 1fr 1fr; border-top: 1px solid var(--line); margin-bottom: 28px; }
.areas-list div { padding: 12px 0; border-bottom: 1px solid var(--line); font-size: .9rem; }
.contact-line { display: flex; flex-wrap: wrap; gap: 28px; font-size: .92rem; }
.contact-line a { display: inline-flex; align-items: center; gap: 10px; color: var(--ink); border-bottom: 1px solid var(--line-2); padding-bottom: 3px; transition: border-color .3s; }
.contact-line a:hover { border-color: var(--gold); }
.contact-line svg { stroke: var(--gold); }

/* Casos: tabla */
.cases { border-top: 1px solid var(--ink); }
.case { display: grid; grid-template-columns: 200px 1fr 1.4fr; gap: 32px; padding: 26px 0; border-bottom: 1px solid var(--line); align-items: baseline; }
.case .cat { font-size: .8rem; font-weight: 600; color: var(--gold-d); }
.case h4 { font-size: 1.35rem !important; line-height: 1.25; }
.case p { color: var(--muted); font-size: .92rem; line-height: 1.7; }
.note { font-size: .8rem; color: var(--muted); margin-top: 20px; }

/* Formación */
.creds { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--line); background: var(--surface); }
.cred { padding: 32px 28px; }
.cred + .cred { border-left: 1px solid var(--line); }
.cred svg { stroke: var(--gold); margin-bottom: 20px; }
.cred small { display: block; font-size: .78rem; font-weight: 600; color: var(--gold-d); margin-bottom: 8px; }
.cred h4 { font-size: 1.35rem !important; line-height: 1.2; margin-bottom: 10px; }
.cred p { color: var(--muted); font-size: .9rem; line-height: 1.7; }

/* Contacto */
.contact-section { padding: 96px 0 72px; }
.contact-panel { background: var(--deep); color: var(--deep-ink); padding: 40px; height: 100%; border-radius: var(--r); }
.contact-panel h3 { color: var(--deep-ink) !important; font-size: 2rem !important; margin-bottom: 14px; }
.contact-panel p { color: rgba(245,241,232,.75); line-height: 1.7; font-size: .95rem; margin-bottom: 28px; }
.c-item { display: block; padding: 16px 0; border-top: 1px solid rgba(245,241,232,.15); color: var(--deep-ink) !important; }
.c-item small { display: block; font-size: .74rem; color: rgba(245,241,232,.6); margin-bottom: 4px; }
.c-item b { font-weight: 500; font-size: 1rem; color: var(--deep-ink); }
.c-item:hover b { color: #C9A45A; }
.c-note { font-size: .8rem; line-height: 1.6; color: rgba(245,241,232,.65); border-top: 1px solid rgba(245,241,232,.15); padding-top: 18px; margin-top: 8px; }

[data-testid="stHorizontalBlock"]:has(.contact-panel) { max-width: 1120px; margin: 0 auto !important; padding: 0 32px; gap: 24px !important; }
[data-testid="stForm"] { background: var(--surface) !important; border: 1px solid var(--line) !important; border-radius: var(--r) !important; padding: 36px !important; }
[data-testid="stForm"] [data-testid="stVerticalBlock"] { gap: 1rem !important; }
[data-testid="stForm"] label p { font-weight: 500 !important; font-size: .84rem !important; color: var(--ink) !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div {
  background: var(--bg) !important; color: var(--ink) !important; border-radius: var(--r) !important; border: 1px solid var(--line) !important; font-family: var(--sans) !important; }
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder { color: var(--muted) !important; opacity: .7; }
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus { border-color: var(--gold) !important; box-shadow: none !important; }
[data-testid="stTextInput"] > div > div, [data-testid="stTextArea"] > div > div { border: none !important; background: transparent !important; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color: var(--ink) !important; }
[data-baseweb="popover"] ul { background: var(--surface) !important; }
[data-baseweb="popover"] li { color: var(--ink) !important; }
[data-testid="stFormSubmitButton"] > button { width: 100%; border-radius: var(--r) !important; padding: .9rem 2rem !important;
  background: var(--btn) !important; border: 1px solid var(--btn) !important; transition: background-color .3s, border-color .3s !important; }
[data-testid="stFormSubmitButton"] > button p { color: var(--btn-ink) !important; font-weight: 600 !important; }
[data-testid="stFormSubmitButton"] > button:hover { background: var(--gold) !important; border-color: var(--gold) !important; }
[data-testid="stFormSubmitButton"] > button:hover p { color: #FFFFFF !important; }
.success { padding: 14px 16px; border: 1px solid #3F7D58; border-left-width: 3px; color: #3F7D58; font-size: .9rem; font-weight: 500; }

/* Pie */
.site-footer { background: var(--deep); color: rgba(245,241,232,.7); padding: 56px 0 40px; font-size: .86rem; }
.site-footer .wrap { display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 40px; }
.site-footer b { display: block; font-family: var(--serif); font-size: 1.5rem; font-weight: 700; color: #F5F1E8; margin-bottom: 8px; }
.site-footer a { color: #F5F1E8; }
.site-footer a:hover { color: #C9A45A; }
.site-footer .wrap > div > div { margin-bottom: 8px; }
.site-footer .legal { max-width: 1120px; margin: 40px auto 0; padding: 20px 32px 0; border-top: 1px solid rgba(245,241,232,.12); font-size: .78rem; }

/* ---------- Interruptor de tema (balanza) ---------- */
.theme-fab { position: fixed; left: 24px; bottom: 24px; z-index: 1000001; width: 62px; height: 62px; border-radius: 50%; padding: 0;
  background: var(--surface); border: 1px solid var(--line-2); cursor: pointer; display: grid; place-items: center;
  box-shadow: 0 6px 18px rgba(0,0,0,.12); transition: background-color .8s var(--ease), border-color .8s var(--ease); }
.theme-fab:hover { border-color: var(--gold); }
.theme-fab svg { width: 40px; height: 40px; overflow: visible; }
.fab-beam { transform-origin: 24px 12px; }
.fab-pan-l { transform-origin: 6px 13px; }
.fab-pan-r { transform-origin: 42px 13px; }
:root[data-theme="dark"] .fab-beam { transform: rotate(-14deg); }
:root[data-theme="dark"] .fab-pan-l, :root[data-theme="dark"] .fab-pan-r { transform: rotate(14deg); }
.theme-fab .tip { position: absolute; left: 74px; white-space: nowrap; background: var(--surface); color: var(--ink); border: 1px solid var(--line);
  font-size: .78rem; font-weight: 500; padding: 7px 12px; border-radius: var(--r); opacity: 0; transition: opacity .3s; pointer-events: none; }
.theme-fab:hover .tip, .theme-fab:focus-visible .tip { opacity: 1; }
.tip-dark, :root[data-theme="dark"] .tip-light { display: none; }
:root[data-theme="dark"] .tip-dark { display: inline; }

.wa { position: fixed; right: 24px; bottom: 24px; z-index: 1000001; width: 56px; height: 56px; border-radius: 50%; background: #25D366;
  display: grid; place-items: center; box-shadow: 0 6px 18px rgba(0,0,0,.18); }

/* Aparición sutil al hacer scroll */
.js .reveal { opacity: 0; transition: opacity .9s var(--ease); }
.js .reveal.in { opacity: 1; }

/* Responsive */
@media (max-width: 960px) {
  .wrap { padding: 0 20px; }
  .nav a.nl { display: none; }
  .brand-sub { display: none; }
  .split, .team { grid-template-columns: 1fr; gap: 36px; }
  .team .portrait { max-width: 360px; }
  .steps, .creds, .facts { grid-template-columns: 1fr; }
  .step, .step + .step { padding: 28px 0; border-left: none; border-bottom: 1px solid var(--line); }
  .cred + .cred, .facts div + div { border-left: none; border-top: 1px solid var(--line); }
  .case { grid-template-columns: 1fr; gap: 8px; }
  .site-footer .wrap { grid-template-columns: 1fr; }
  .section { padding: 72px 0; }
  .alert-bar { font-size: .76rem; justify-content: flex-start; padding: 0 48px 0 14px; }
  .alert-bar .hide-sm { display: none; }
  .theme-fab { width: 54px; height: 54px; left: 16px; bottom: 16px; }
  .theme-fab .tip { display: none; }
  .wa { right: 16px; bottom: 16px; }
  [data-testid="stHorizontalBlock"]:has(.contact-panel) { padding: 0 20px; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition-duration: .01ms !important; animation: none !important; }
  .js .reveal { opacity: 1; }
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# =========================================================
# ÍCONOS
# =========================================================
def icon(paths: str, size: int = 26) -> str:
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke-width="1.4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


icon_shield = icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>')
icon_family = icon('<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M3 20v-1a5 5 0 0 1 10 0v1"/><path d="M14 20v-.5a3.5 3.5 0 0 1 7 0v.5"/>')
icon_work = icon('<rect x="3" y="7" width="18" height="13" rx="1.5"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M3 13h18"/>')
icon_cap = icon('<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/><path d="M22 9v6"/>', 28)
icon_mail = icon('<rect x="2" y="4" width="20" height="16" rx="1.5"/><polyline points="22,6 12,13 2,6"/>', 17)
icon_phone = icon('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>', 17)
icon_wa = '<svg width="28" height="28" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5a9.45 9.45 0 0 1-4.82-1.32l-.35-.21-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.47 9.48-9.47a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.7c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.53A11.32 11.32 0 0 0 12.04.64C5.76.64.65 5.75.65 12.03c0 2.01.52 3.97 1.52 5.7L.55 23.6l6.02-1.58a11.36 11.36 0 0 0 5.47 1.39c6.28 0 11.39-5.11 11.39-11.39 0-3.04-1.18-5.9-3.34-8.05z"/></svg>'

logo = """<svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
<circle cx="24" cy="24" r="23" style="stroke:var(--gold)" stroke-width="1"/>
<circle cx="24" cy="24" r="19.5" style="stroke:var(--gold)" stroke-width=".5"/>
<g style="stroke:var(--ink)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
<path d="M24 13.5v19.5M19 33.5h10M20.5 33.5l3.5-2.4 3.5 2.4"/><path d="M13 18Q24 16.4 35 18"/>
<path d="M14 18.4l-3 7.2M14 18.4l3 7.2M10 25.6h8c-.4 2-2 3.1-4 3.1s-3.6-1.1-4-3.1z"/>
<path d="M34 18.4l-3 7.2M34 18.4l3 7.2M30 25.6h8c-.4 2-2 3.1-4 3.1s-3.6-1.1-4-3.1z"/></g>
<circle cx="24" cy="12" r="1.4" style="fill:var(--gold)"/></svg>"""

# =========================================================
# BALANZA REALISTA (latón con volumen y sombras)
# =========================================================
BRASS_DEFS = """
<defs>
  <linearGradient id="hhV" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#EBD6A0"/><stop offset=".45" stop-color="#C19A52"/><stop offset="1" stop-color="#7E5F2A"/>
  </linearGradient>
  <linearGradient id="hhH" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#7A5B27"/><stop offset=".32" stop-color="#E4CB8C"/><stop offset=".55" stop-color="#BD9549"/><stop offset="1" stop-color="#6E5122"/>
  </linearGradient>
  <radialGradient id="hhBall" cx=".35" cy=".3" r=".75">
    <stop offset="0" stop-color="#F7E7BA"/><stop offset=".45" stop-color="#C9A257"/><stop offset="1" stop-color="#6E5122"/>
  </radialGradient>
  <radialGradient id="hhBowl" cx=".38" cy=".05" r="1">
    <stop offset="0" stop-color="#EAD39A"/><stop offset=".5" stop-color="#B68D45"/><stop offset="1" stop-color="#5F451C"/>
  </radialGradient>
  <linearGradient id="hhRim" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F3E2B0"/><stop offset="1" stop-color="#9C7735"/>
  </linearGradient>
  <linearGradient id="hhInner" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6E5122"/><stop offset="1" stop-color="#A98443"/>
  </linearGradient>
  <radialGradient id="hhShadow" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#000" stop-opacity=".28"/><stop offset="1" stop-color="#000" stop-opacity="0"/>
  </radialGradient>
</defs>"""


def pan(cx: int, cls: str) -> str:
    return f"""
  <g class="{cls}">
    <circle cx="{cx}" cy="78" r="3.2" fill="none" stroke="#7E5F2A" stroke-width="1.6"/>
    <g stroke="#7A5B27" stroke-width="1.7" stroke-linecap="round" stroke-dasharray="3.2 1.8">
      <path d="M{cx} 81 L{cx - 34} 176"/><path d="M{cx} 81 L{cx} 172"/><path d="M{cx} 81 L{cx + 34} 176"/>
    </g>
    <path d="M{cx - 38} 178 Q{cx - 36} 207 {cx} 209 Q{cx + 36} 207 {cx + 38} 178 Z" fill="url(#hhBowl)"/>
    <path d="M{cx - 26} 186 Q{cx - 22} 200 {cx - 8} 203" fill="none" stroke="#F3E2B0" stroke-opacity=".45" stroke-width="2" stroke-linecap="round"/>
    <ellipse cx="{cx}" cy="178" rx="38" ry="6.5" fill="url(#hhRim)"/>
    <ellipse cx="{cx}" cy="178.6" rx="33" ry="4.4" fill="url(#hhInner)"/>
  </g>"""


main_scale = f"""
<svg viewBox="0 0 320 300" role="img" aria-label="Balanza de la justicia">
  {BRASS_DEFS}
  <ellipse cx="160" cy="286" rx="110" ry="9" fill="url(#hhShadow)"/>
  <rect x="78" y="264" width="164" height="16" rx="2" fill="url(#hhV)"/>
  <rect x="78" y="264" width="164" height="2" fill="#F3E2B0" opacity=".6"/>
  <path d="M100 264 L112 247 H208 L220 264 Z" fill="url(#hhV)"/>
  <rect x="136" y="238" width="48" height="10" rx="2" fill="url(#hhH)"/>
  <path d="M150 238 L153.5 92 H166.5 L170 238 Z" fill="url(#hhH)"/>
  <rect x="145" y="196" width="30" height="7" rx="2" fill="url(#hhH)"/>
  <rect x="147" y="130" width="26" height="6" rx="2" fill="url(#hhH)"/>
  <rect x="143" y="84" width="34" height="9" rx="2" fill="url(#hhH)"/>
  <rect x="156.5" y="50" width="7" height="34" fill="url(#hhH)"/>
  <circle cx="160" cy="44" r="9" fill="url(#hhBall)"/>
  <path d="M160 35 L157.5 24 L160 18 L162.5 24 Z" fill="url(#hhH)"/>
  <g class="beam">
    <path d="M38 66 Q160 57 282 66 L282 75 Q160 67 38 75 Z" fill="url(#hhV)"/>
    <path d="M42 67 Q160 59 278 67" fill="none" stroke="#F6E6B8" stroke-opacity=".55" stroke-width="1.2"/>
    <circle cx="34" cy="70.5" r="6.5" fill="url(#hhBall)"/>
    <circle cx="286" cy="70.5" r="6.5" fill="url(#hhBall)"/>
    <circle cx="160" cy="70" r="11" fill="url(#hhBall)"/>
    <circle cx="160" cy="70" r="3.4" fill="#5F451C"/>
    {pan(44, "pan-l")}
    {pan(276, "pan-r")}
  </g>
</svg>"""

fab_scale = """
<svg viewBox="0 0 48 48" aria-hidden="true">
  <defs>
    <linearGradient id="fbV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E8D19A"/><stop offset="1" stop-color="#8A6A2E"/></linearGradient>
    <linearGradient id="fbH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7A5B27"/><stop offset=".4" stop-color="#E4CB8C"/><stop offset="1" stop-color="#6E5122"/></linearGradient>
  </defs>
  <rect x="15" y="42" width="18" height="3" rx="1" fill="url(#fbV)"/>
  <path d="M22.6 42 L23.2 11 H24.8 L25.4 42 Z" fill="url(#fbH)"/>
  <circle cx="24" cy="8.5" r="2.2" fill="url(#fbV)"/>
  <g class="fab-beam">
    <path d="M4 11.2 Q24 9 44 11.2 L44 13 Q24 11 4 13 Z" fill="url(#fbV)"/>
    <circle cx="24" cy="12" r="2.4" fill="url(#fbV)"/>
    <g class="fab-pan-l"><path d="M6 13 L1 26 M6 13 L11 26" stroke="#7A5B27" stroke-width=".9"/>
      <path d="M0 26 Q.6 31 6 31.4 Q11.4 31 12 26 Z" fill="url(#fbV)"/><ellipse cx="6" cy="26" rx="6" ry="1.2" fill="#E8D19A"/></g>
    <g class="fab-pan-r"><path d="M42 13 L37 26 M42 13 L47 26" stroke="#7A5B27" stroke-width=".9"/>
      <path d="M36 26 Q36.6 31 42 31.4 Q47.4 31 48 26 Z" fill="url(#fbV)"/><ellipse cx="42" cy="26" rx="6" ry="1.2" fill="#E8D19A"/></g>
  </g>
</svg>"""

# =========================================================
# ALERTA, ENCABEZADO Y BOTONES FIJOS
# =========================================================
html(f"""
<div class="alert-bar" role="alert">
  <span><strong>¿Estás en peligro inminente?</strong> <span class="hide-sm">Llama de inmediato al</span></span>
  <a href="tel:149">149 Fono Familia Carabineros</a>
  <span class="sep hide-sm">·</span><a class="hide-sm" href="tel:133">133 Carabineros</a>
  <span class="sep hide-sm">·</span><a class="hide-sm" href="tel:1455">1455 SernamEG</a>
  <button class="alert-close" type="button" data-close-alert aria-label="Cerrar aviso">×</button>
</div>
<header class="site-header t">
  <div class="wrap">
    <a class="brand" href="#inicio" data-scroll="inicio" aria-label="{BRAND}, ir al inicio">{logo}
      <span><span class="brand-name">{BRAND}</span><span class="brand-sub">Estudio jurídico de la mujer</span></span></a>
    <nav class="nav" aria-label="Navegación principal">
      <a class="nl" href="#areas" data-scroll="areas">Áreas de práctica</a>
      <a class="nl" href="#equipo" data-scroll="equipo">Equipo</a>
      <a class="nl" href="#casos" data-scroll="casos">Casos</a>
      <a class="btn" href="#contacto" data-scroll="contacto">Agendar consulta</a>
    </nav>
  </div>
</header>
<button class="theme-fab" type="button" data-theme-toggle aria-label="Cambiar entre tema claro y oscuro" aria-pressed="false">
  {fab_scale}<span class="tip"><span class="tip-light">Tema oscuro</span><span class="tip-dark">Tema claro</span></span>
</button>
<a class="wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}</a>
""")

# =========================================================
# PORTADA
# =========================================================
html(f"""
<section class="hero t" id="inicio">
  <div class="wrap">
    <div class="scale-wrap">{main_scale}</div>
    <div class="rule"></div>
    <h1>Defensa legal especializada, <em>humana y sin prejuicios.</em></h1>
    <p class="lead">Representamos a mujeres en violencia intrafamiliar, derecho de familia y acoso laboral, con rigor técnico, absoluta confidencialidad y explicaciones claras en cada etapa del proceso.</p>
    <div class="actions">
      <a class="btn" href="#contacto" data-scroll="contacto">Agendar consulta confidencial</a>
      <a class="btn ghost" href="tel:{PHONE_TEL}">{icon_phone}<span>{PHONE_DISPLAY}</span></a>
    </div>
  </div>
  <div class="facts t">
    <div><b>Confidencialidad</b>Protegida por secreto profesional</div>
    <div><b>Medidas urgentes</b>Tramitación prioritaria en casos VIF</div>
    <div><b>Atención</b>Online y presencial en todo Chile</div>
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
     "Representación en los procesos que definen el bienestar de tus hijos y la estabilidad de tu hogar.",
     ["Pensión de alimentos", "Retención de fondos AFP", "Cuidado personal y visitas", "Divorcio"]),
    (icon_work, "Acoso laboral y Ley Karin",
     "Intervención estratégica ante acoso laboral o sexual y vulneración de derechos fundamentales en el trabajo.",
     ["Tutela de derechos", "Despido indirecto", "Despido por maternidad"]),
]
rows = "".join(
    f"""<div class="row">{ic}<div><h3>{t}</h3><p>{d}</p><div class="items">{''.join(f'<span>{x}</span>' for x in items)}</div></div></div>"""
    for ic, t, d, items in areas
)
steps = [
    ("Primera reunión", "Nos cuentas tu situación con total reserva. Evaluamos riesgos, plazos y alternativas reales."),
    ("Estrategia", "Te proponemos un plan de acción concreto, con etapas y honorarios explicados con claridad."),
    ("Representación", "Llevamos tu causa ante tribunales y te informamos de cada avance relevante."),
]
steps_html = "".join(
    f'<div class="step"><div class="n">{i + 1:02d}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(steps)
)
html(f"""
<section class="section t" id="areas">
  <div class="wrap split">
    <div class="sec-title reveal">
      <span class="eyebrow">Áreas de práctica</span>
      <h2>Especialización en los derechos de la mujer</h2>
      <p>Tres áreas de ejercicio con un mismo método: estrategia jurídica precisa y acompañamiento cercano durante todo el proceso.</p>
    </div>
    <div class="rows reveal">{rows}</div>
  </div>
</section>
<section class="section alt t" id="proceso">
  <div class="wrap">
    <div class="sec-title center reveal">
      <span class="eyebrow">Cómo trabajamos</span>
      <h2>Un proceso claro desde el primer día</h2>
      <p>Sabrás en todo momento en qué etapa está tu causa y cuál es el siguiente paso.</p>
    </div>
    <div class="steps reveal">{steps_html}</div>
  </div>
</section>
""")

# =========================================================
# EQUIPO
# =========================================================
photo = image_to_data_uri("fran.jpg")
portrait = (f'<img src="{photo}" alt="Retrato de María-Francisca Valentina" />'
            if photo else '<div class="monogram">MF</div>')
html(f"""
<section class="section t" id="equipo">
  <div class="wrap team">
    <div class="portrait t reveal">{portrait}</div>
    <div class="reveal">
      <span class="role">Abogada fundadora</span>
      <h3>María-Francisca Valentina</h3>
      <p class="bio">Especialista en violencia de género, derecho de familia, penal y laboral. Combina litigación técnica con un acompañamiento humano para la protección integral de los derechos de sus clientas.</p>
      <blockquote class="quote">Ninguna mujer debería enfrentar sola un proceso judicial. Mi trabajo es que tengas claridad y respaldo en cada decisión.</blockquote>
      <div class="areas-list"><div>Violencia de género</div><div>Derecho de familia</div><div>Derecho penal</div><div>Derecho laboral</div></div>
      <div class="contact-line">
        <a href="mailto:{EMAIL}">{icon_mail}<span>{EMAIL}</span></a>
        <a href="tel:{PHONE_TEL}">{icon_phone}<span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </div>
</section>
""")

# =========================================================
# CASOS Y FORMACIÓN
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
cases_html = "".join(
    f'<div class="case"><span class="cat">{c}</span><h4>{t}</h4><p>{d}</p></div>' for c, t, d in cases
)
creds = [
    ("Universidad de Chile", "Diplomado en Derecho de Familia", "Litigación oral y medidas cautelares en tribunales de familia."),
    ("Pontificia Universidad Católica", "Certificación en Ley Karin y género", "Prevención, tutela de derechos fundamentales y acoso laboral."),
    ("Academia Judicial / UDP", "Postítulo en Derecho Penal y VIF", "Estrategia penal y querellas por agresiones graves."),
]
creds_html = "".join(
    f'<div class="cred">{icon_cap}<small>{inst}</small><h4>{t}</h4><p>{d}</p></div>' for inst, t, d in creds
)
html(f"""
<section class="section alt t" id="casos">
  <div class="wrap split">
    <div class="sec-title reveal">
      <span class="eyebrow">Resultados</span>
      <h2>Casos destacados</h2>
      <p>Algunas resoluciones obtenidas para nuestras clientas, presentadas de forma anónima.</p>
    </div>
    <div class="reveal">
      <div class="cases">{cases_html}</div>
      <p class="note">Los resultados anteriores no garantizan resultados futuros. Cada caso se evalúa de forma individual.</p>
    </div>
  </div>
</section>
<section class="section t" id="formacion">
  <div class="wrap">
    <div class="sec-title center reveal">
      <span class="eyebrow">Formación académica</span>
      <h2>Preparación que respalda tu defensa</h2>
      <p>Especialización continua en las materias que defendemos ante tribunales.</p>
    </div>
    <div class="creds t reveal">{creds_html}</div>
  </div>
</section>
<section class="contact-section" id="contacto">
  <div class="wrap">
    <div class="sec-title center reveal">
      <span class="eyebrow">Contacto</span>
      <h2>Agenda tu consulta confidencial</h2>
      <p>Cuéntanos lo esencial. Te respondemos personalmente por el medio que prefieras.</p>
    </div>
  </div>
</section>
""")

# =========================================================
# CONTACTO
# =========================================================
col_info, col_form = st.columns([1, 1.5])

with col_info:
    html(f"""
    <div class="contact-panel t">
      <h3>Hablemos con reserva</h3>
      <p>La primera conversación sirve para entender tu situación y explicarte tus opciones, sin compromiso.</p>
      <a class="c-item" href="tel:{PHONE_TEL}"><small>Teléfono y WhatsApp</small><b>{PHONE_DISPLAY}</b></a>
      <a class="c-item" href="mailto:{EMAIL}"><small>Correo electrónico</small><b>{EMAIL}</b></a>
      <a class="c-item" href="tel:149"><small>Emergencias VIF</small><b>149 Fono Familia · 1455 SernamEG</b></a>
      <p class="c-note">Todo lo que compartas está protegido por secreto profesional y no se comparte con terceros.</p>
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
                html('<div class="success">Consulta enviada. Te contactaremos a la brevedad.</div>')
            else:
                st.error("Indica tu nombre y al menos un medio de contacto (teléfono o correo) para poder responderte.")

# =========================================================
# PIE DE PÁGINA
# =========================================================
html(f"""
<div style="height:72px"></div>
<footer class="site-footer">
  <div class="wrap">
    <div><b>{BRAND}</b><div>Estudio jurídico de la mujer en Chile.</div></div>
    <div><div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div><div><a href="#areas" data-scroll="areas">Áreas de práctica</a></div><div><a href="#equipo" data-scroll="equipo">Equipo</a></div><div><a href="#contacto" data-scroll="contacto">Agendar consulta</a></div></div>
  </div>
  <div class="legal">© 2026 {BRAND}. Todos los derechos reservados.</div>
</footer>
""")

# =========================================================
# INTERACCIONES (tema, aviso, scroll suave y aparición sutil)
# =========================================================
components.html("""
<script>
(function () {
  const win = window.parent, doc = win.document, root = doc.documentElement;
  const reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const get = (s, k) => { try { return win[s].getItem(k); } catch (e) { return null; } };
  const set = (s, k, v) => { try { win[s].setItem(k, v); } catch (e) {} };

  if (!root.getAttribute('data-theme')) root.setAttribute('data-theme', get('localStorage', 'hh-theme') || 'light');
  doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark'));
  if (get('sessionStorage', 'hh-alert') === 'closed') root.classList.add('alert-closed');
  root.classList.add('js');

  if (!win.__hhIO) {
    win.__hhIO = new win.IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); win.__hhIO.unobserve(e.target); }
    }), { threshold: 0.12 });
  }
  const observe = () => doc.querySelectorAll('.reveal:not(.in)').forEach(el => reduce ? el.classList.add('in') : win.__hhIO.observe(el));
  observe();
  if (!win.__hhMO) { win.__hhMO = new win.MutationObserver(observe); win.__hhMO.observe(doc.body, { childList: true, subtree: true }); }

  if (win.__hhInit) return;
  win.__hhInit = true;

  function setTheme(next) {
    const apply = () => {
      root.setAttribute('data-theme', next);
      doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', next === 'dark'));
      set('localStorage', 'hh-theme', next);
    };
    if (doc.startViewTransition && !reduce) doc.startViewTransition(apply); else apply();
  }

  doc.addEventListener('click', (e) => {
    if (e.target.closest('[data-theme-toggle]')) {
      e.preventDefault();
      setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
      return;
    }
    if (e.target.closest('[data-close-alert]')) {
      root.classList.add('alert-closed');
      set('sessionStorage', 'hh-alert', 'closed');
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
})();
</script>
""", height=0, width=0)
