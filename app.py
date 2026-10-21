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
# UTILIDADES
# =========================================================
def html(markup: str) -> None:
    """Renderiza HTML limpiando sangrías (evita que Markdown lo convierta en bloque de código)."""
    clean = "\n".join(line.strip() for line in markup.splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


def image_to_data_uri(path: str):
    if not os.path.exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().replace(".", "") or "jpeg"
    ext = "jpeg" if ext == "jpg" else ext
    with open(path, "rb") as f:
        return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"


# =========================================================
# ESTADO DEL TEMA
# =========================================================
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "light"


def toggle_theme():
    st.session_state.theme_mode = "dark" if st.session_state.theme_mode == "light" else "light"


is_dark = st.session_state.theme_mode == "dark"

# =========================================================
# TOKENS DE DISEÑO
# =========================================================
if is_dark:
    tokens = dict(
        bg="#14120F", surface="#1C1915", surface2="#25211B", line="#3A332A",
        ink="#F5F1E8", muted="#B3AA9A", gold="#E2BE62", gold_ink="#E8C774",
        gold_soft="rgba(226,190,98,0.14)", wine="#E08AA2", wine_soft="rgba(224,138,162,0.10)",
        nav="rgba(20,18,15,0.72)", shadow="rgba(0,0,0,0.45)",
    )
    toggle_label = "☀  Modo claro"
else:
    tokens = dict(
        bg="#FBF8F1", surface="#FFFFFF", surface2="#F4EEE0", line="#E7DDC4",
        ink="#1F1B16", muted="#6A6155", gold="#C9A23A", gold_ink="#8C6B12",
        gold_soft="rgba(201,162,58,0.12)", wine="#7A2440", wine_soft="rgba(122,36,64,0.06)",
        nav="rgba(251,248,241,0.78)", shadow="rgba(60,45,20,0.10)",
    )
    toggle_label = "☾  Modo oscuro"

css_vars = ":root{" + "".join(f"--{k.replace('_', '-')}:{v};" for k, v in tokens.items()) + "}"

# =========================================================
# ESTILOS (CSS plano con variables: sin llaves duplicadas)
# =========================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@400;500;600;700&display=swap');

html, body, .stApp, [data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
  color: var(--ink) !important;
  font-family: 'Manrope', system-ui, sans-serif !important;
  transition: background-color .5s ease, color .5s ease;
}
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
.block-container { padding-top: 5.5rem !important; padding-bottom: 3rem !important; max-width: 1120px !important; }
::selection { background: var(--gold); color: #1F1B16; }

h1, h2, h3, h4 { font-family: 'Cormorant Garamond', Georgia, serif !important; color: var(--ink) !important; letter-spacing: -0.01em; }
p, label, span, li { color: var(--ink); }
a { text-decoration: none !important; }

/* ---------- Barra de progreso de lectura ---------- */
.scroll-progress {
  position: fixed; top: 0; left: 0; height: 2px; width: 100%;
  transform-origin: 0 50%; transform: scaleX(var(--progress, 0));
  background: linear-gradient(90deg, var(--gold), var(--gold-ink));
  z-index: 1000001; transition: transform .08s linear;
}

/* ---------- Navbar ---------- */
.custom-navbar {
  position: fixed; top: 0; left: 0; right: 0; height: 74px;
  display: flex; justify-content: space-between; align-items: center;
  padding: 0 5%; z-index: 1000000;
  background: var(--nav);
  backdrop-filter: saturate(160%) blur(14px); -webkit-backdrop-filter: saturate(160%) blur(14px);
  border-bottom: 1px solid transparent;
  transition: height .35s ease, border-color .35s ease, box-shadow .35s ease, background-color .5s ease;
}
.custom-navbar.is-scrolled { height: 60px; border-color: var(--line); box-shadow: 0 8px 30px var(--shadow); }
.nav-brand { display: flex; align-items: center; gap: 12px; font-family: 'Cormorant Garamond', serif;
  font-size: 1.45rem; font-weight: 700; color: var(--ink); letter-spacing: .02em; }
.nav-brand svg { transition: transform .8s cubic-bezier(.34,1.56,.64,1); }
.nav-brand:hover svg { transform: rotate(-12deg); }
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a { position: relative; font-size: .9rem; font-weight: 600; color: var(--ink) !important; padding: 6px 0; }
.nav-links a::after { content: ""; position: absolute; left: 0; bottom: 0; height: 1.5px; width: 100%;
  background: var(--gold); transform: scaleX(0); transform-origin: right; transition: transform .35s ease; }
.nav-links a:hover::after, .nav-links a.active::after { transform: scaleX(1); transform-origin: left; }
.nav-cta { padding: 9px 18px !important; border-radius: 999px; border: 1px solid var(--gold);
  color: var(--gold-ink) !important; transition: background-color .3s, color .3s; }
.nav-cta::after { display: none; }
.nav-cta:hover { background: var(--gold); color: #1F1B16 !important; }

/* ---------- Hero ---------- */
.hero { display: grid; grid-template-columns: 1.35fr 1fr; gap: 3rem; align-items: center; padding: 3.5rem 0 2.5rem; }
.hero-kicker { display: inline-flex; align-items: center; gap: 10px; font-size: .92rem; font-weight: 600;
  color: var(--gold-ink); margin-bottom: 1.4rem; }
.hero-kicker::before { content: ""; width: 34px; height: 1.5px; background: var(--gold); }
.hero-title { font-family: 'Cormorant Garamond', serif; font-weight: 600; color: var(--ink);
  font-size: clamp(2.6rem, 5.4vw, 4.4rem); line-height: 1.02; margin: 0 0 1.6rem; }
.hero-title .line { display: block; overflow: hidden; padding-bottom: .08em; }
.hero-title .line > span { display: block; color: var(--ink); transform: translateY(105%);
  animation: lineUp 1s cubic-bezier(.2,.8,.2,1) forwards; }
.hero-title .line:nth-child(2) > span { animation-delay: .12s; }
.hero-title .line:nth-child(3) > span { animation-delay: .24s; font-style: italic; color: var(--gold-ink); }
@keyframes lineUp { to { transform: translateY(0); } }
.hero-sub { font-size: 1.08rem; color: var(--muted); line-height: 1.75; max-width: 34rem; margin-bottom: 2.2rem;
  opacity: 0; animation: fadeIn .9s ease .5s forwards; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 14px; opacity: 0; animation: fadeIn .9s ease .7s forwards; }
@keyframes fadeIn { to { opacity: 1; } }

.btn-solid, .btn-ghost { display: inline-flex; align-items: center; gap: 10px; padding: 14px 26px;
  border-radius: 999px; font-weight: 700; font-size: .95rem; transition: transform .3s, box-shadow .3s, background-color .3s; }
.btn-solid { background: var(--ink); color: var(--bg) !important; position: relative; overflow: hidden; }
.btn-solid span { color: var(--bg) !important; position: relative; z-index: 1; }
.btn-solid::before { content: ""; position: absolute; inset: 0; background: var(--gold);
  transform: translateY(101%); transition: transform .45s cubic-bezier(.2,.8,.2,1); }
.btn-solid:hover::before { transform: translateY(0); }
.btn-solid:hover span { color: #1F1B16 !important; }
.btn-solid:hover { box-shadow: 0 14px 34px var(--shadow); transform: translateY(-2px); }
.btn-ghost { border: 1px solid var(--line); color: var(--ink) !important; background: var(--surface); }
.btn-ghost span { color: var(--ink) !important; }
.btn-ghost:hover { border-color: var(--gold); transform: translateY(-2px); }

/* Balanza: oscila y se equilibra al cargar */
.scale-stage { position: relative; display: grid; place-items: center; aspect-ratio: 1; max-width: 400px; margin-left: auto; width: 100%; }
.scale-stage::before { content: ""; position: absolute; inset: 8%; border-radius: 50%;
  background: radial-gradient(circle, var(--gold-soft) 0%, transparent 68%);
  animation: breathe 6s ease-in-out infinite; }
.scale-stage::after { content: ""; position: absolute; inset: 2%; border-radius: 50%;
  border: 1px dashed var(--line); animation: spin 60s linear infinite; }
@keyframes breathe { 50% { transform: scale(1.08); opacity: .75; } }
@keyframes spin { to { transform: rotate(360deg); } }
.scale-svg { position: relative; z-index: 1; width: 78%; height: auto; overflow: visible; }
.scale-beam { transform-origin: 160px 70px; animation: settle 3.2s cubic-bezier(.3,.7,.4,1) .3s both; }
.scale-pan-l { transform-origin: 50px 72px; animation: counter 3.2s cubic-bezier(.3,.7,.4,1) .3s both; }
.scale-pan-r { transform-origin: 270px 72px; animation: counter 3.2s cubic-bezier(.3,.7,.4,1) .3s both; }
@keyframes settle { 0%{transform:rotate(-14deg)} 22%{transform:rotate(10deg)} 42%{transform:rotate(-6deg)}
  60%{transform:rotate(3.5deg)} 78%{transform:rotate(-1.5deg)} 100%{transform:rotate(0)} }
@keyframes counter { 0%{transform:rotate(14deg)} 22%{transform:rotate(-10deg)} 42%{transform:rotate(6deg)}
  60%{transform:rotate(-3.5deg)} 78%{transform:rotate(1.5deg)} 100%{transform:rotate(0)} }

/* ---------- Botón de tema (flotante) ---------- */
.st-key-theme_btn { position: fixed !important; left: 22px; bottom: 22px; z-index: 1000000; width: auto !important; }
div[data-testid="stButton"] > button {
  background: var(--surface) !important; color: var(--ink) !important; border: 1px solid var(--line) !important;
  border-radius: 999px !important; padding: .6rem 1.2rem !important; font-weight: 600 !important; font-size: .85rem !important;
  box-shadow: 0 8px 24px var(--shadow) !important; transition: transform .3s, border-color .3s !important;
}
div[data-testid="stButton"] > button p { color: var(--ink) !important; }
div[data-testid="stButton"] > button:hover { border-color: var(--gold) !important; transform: translateY(-2px); }
div[data-testid="stButton"] > button:focus-visible { outline: 2px solid var(--gold) !important; outline-offset: 3px; }

/* ---------- Franja de urgencia ---------- */
.urgent { display: grid; grid-template-columns: auto 1fr auto; gap: 1.5rem; align-items: center;
  background: var(--wine-soft); border: 1px solid var(--line); border-left: 3px solid var(--wine);
  border-radius: 14px; padding: 1.4rem 1.8rem; margin: 1rem 0 2rem; }
.urgent-dot { width: 12px; height: 12px; border-radius: 50%; background: var(--wine); position: relative; }
.urgent-dot::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--wine);
  animation: ping 1.8s cubic-bezier(0,0,.2,1) infinite; }
@keyframes ping { 75%, 100% { transform: scale(2.6); opacity: 0; } }
.urgent h4 { font-family: 'Manrope', sans-serif !important; font-size: 1.02rem !important; margin: 0 0 .25rem !important; font-weight: 700; }
.urgent p { margin: 0; color: var(--muted); font-size: .93rem; line-height: 1.6; }
.urgent-phones { display: flex; gap: 10px; }
.phone-chip { display: flex; flex-direction: column; align-items: center; min-width: 86px; padding: 8px 14px;
  border-radius: 12px; background: var(--surface); border: 1px solid var(--line); transition: border-color .3s, transform .3s; }
.phone-chip:hover { border-color: var(--wine); transform: translateY(-2px); }
.phone-chip b { font-size: 1.3rem; color: var(--wine) !important; font-family: 'Cormorant Garamond', serif; }
.phone-chip small { font-size: .72rem; color: var(--muted) !important; }

/* ---------- Encabezados de sección ---------- */
.section { padding: 4.5rem 0 1rem; scroll-margin-top: 80px; }
.section-head { display: flex; justify-content: space-between; align-items: flex-end; gap: 2rem; margin-bottom: 2.4rem; }
.section-head h2 { font-size: clamp(2.1rem, 3.6vw, 3rem) !important; margin: 0 !important; line-height: 1.05; font-weight: 600; }
.section-head p { color: var(--muted); max-width: 26rem; margin: 0; line-height: 1.65; font-size: .97rem; }

/* ---------- Áreas: tarjetas con foco de luz que sigue al cursor ---------- */
.areas { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2rem; }
.service-card { position: relative; overflow: hidden; background: var(--surface); border: 1px solid var(--line);
  border-radius: 18px; padding: 2.2rem 1.9rem 2rem; transition: border-color .4s, transform .4s; }
.service-card::before { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: 0;
  background: radial-gradient(380px circle at var(--mx, 50%) var(--my, 50%), var(--gold-soft), transparent 60%);
  transition: opacity .4s; }
.service-card:hover::before { opacity: 1; }
.service-card:hover { border-color: var(--gold); transform: translateY(-4px); }
.service-icon { width: 56px; height: 56px; border-radius: 14px; display: grid; place-items: center;
  background: var(--gold-soft); margin-bottom: 1.5rem; position: relative; }
.service-card h3 { font-size: 1.65rem !important; margin: 0 0 .7rem !important; font-weight: 600; position: relative; }
.service-card p { color: var(--muted); font-size: .94rem; line-height: 1.7; margin: 0 0 1.4rem; position: relative; }
.service-card ul { list-style: none; padding: 0; margin: 0; border-top: 1px solid var(--line); padding-top: 1rem; position: relative; }
.service-card li { font-size: .86rem; color: var(--ink); padding: 5px 0 5px 20px; position: relative; }
.service-card li::before { content: ""; position: absolute; left: 0; top: 13px; width: 10px; height: 1.5px; background: var(--gold); }

/* ---------- Proceso ---------- */
.steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; border-top: 1px solid var(--line); position: relative; }
.steps::before { content: ""; position: absolute; top: -1px; left: 0; height: 2px; width: 100%; background: var(--gold);
  transform: scaleX(0); transform-origin: left; transition: transform 1.6s cubic-bezier(.2,.8,.2,1); }
.steps.in::before { transform: scaleX(1); }
.step { padding: 2rem 2rem 0 0; }
.step-n { font-family: 'Cormorant Garamond', serif; font-size: 3.2rem; line-height: 1; color: var(--gold-ink); font-weight: 600; }
.step h4 { font-family: 'Manrope', sans-serif !important; font-size: 1.05rem !important; margin: .8rem 0 .5rem !important; font-weight: 700; }
.step p { color: var(--muted); font-size: .92rem; line-height: 1.7; margin: 0; }

/* ---------- Equipo ---------- */
.team { display: grid; grid-template-columns: 0.9fr 1.3fr; gap: 3rem; align-items: center; }
.portrait { position: relative; border-radius: 22px; overflow: hidden; aspect-ratio: 4/5; background: var(--surface2); }
.portrait img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s cubic-bezier(.2,.8,.2,1); }
.portrait:hover img { transform: scale(1.05); }
.portrait::after { content: ""; position: absolute; inset: 12px; border: 1px solid rgba(255,255,255,.45); border-radius: 14px; pointer-events: none; }
.monogram { width: 100%; height: 100%; display: grid; place-items: center; font-family: 'Cormorant Garamond', serif;
  font-size: 6rem; color: var(--gold-ink); }
.team-role { color: var(--gold-ink); font-weight: 700; font-size: .95rem; margin-bottom: .4rem; }
.team h3 { font-size: clamp(2.2rem, 4vw, 3.1rem) !important; margin: 0 0 1.2rem !important; line-height: 1.05; font-weight: 600; }
.team-bio { color: var(--muted); line-height: 1.8; font-size: 1.02rem; margin-bottom: 1.6rem; }
.quote { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.45rem; line-height: 1.4;
  color: var(--ink); border-left: 2px solid var(--gold); padding-left: 1.2rem; margin: 0 0 2rem; }
.contact-row { display: flex; flex-wrap: wrap; gap: 12px; }
.contact-pill { display: inline-flex; align-items: center; gap: 10px; padding: 11px 18px; border-radius: 999px;
  border: 1px solid var(--line); background: var(--surface); color: var(--ink) !important; font-weight: 600; font-size: .92rem;
  transition: border-color .3s, transform .3s; }
.contact-pill span { color: var(--ink) !important; }
.contact-pill:hover { border-color: var(--gold); transform: translateY(-2px); }

/* ---------- Carrusel de casos ---------- */
.marquee { overflow: hidden; padding: .8rem 0 1.4rem;
  mask-image: linear-gradient(90deg, transparent, #000 7%, #000 93%, transparent);
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 7%, #000 93%, transparent); }
.marquee-track { display: flex; gap: 1.2rem; width: max-content; animation: marquee 45s linear infinite; }
.marquee:hover .marquee-track { animation-play-state: paused; }
@keyframes marquee { to { transform: translateX(calc(-50% - .6rem)); } }
.case-card { width: 330px; flex-shrink: 0; white-space: normal; background: var(--surface); border: 1px solid var(--line);
  border-radius: 18px; padding: 1.7rem; transition: border-color .3s, transform .3s; }
.case-card:hover { border-color: var(--gold); transform: translateY(-4px); }
.case-badge { display: inline-block; font-size: .76rem; font-weight: 700; color: var(--gold-ink) !important;
  background: var(--gold-soft); padding: 5px 12px; border-radius: 999px; margin-bottom: 1rem; }
.case-card h4 { font-size: 1.4rem !important; margin: 0 0 .5rem !important; font-weight: 600; }
.case-card p { color: var(--muted); font-size: .88rem; line-height: 1.65; margin: 0; }
.disclaimer { text-align: center; font-size: .8rem; color: var(--muted); margin-top: .4rem; }

/* ---------- Diplomas ---------- */
.diplomas { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2rem; }
.diploma-card { background: var(--surface); border: 1px solid var(--line); border-radius: 18px; overflow: hidden; transition: border-color .4s; }
.diploma-card:hover { border-color: var(--gold); }
.diploma-img { height: 190px; overflow: hidden; }
.diploma-img img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(35%) sepia(15%);
  transition: transform 1s cubic-bezier(.2,.8,.2,1), filter .6s; }
.diploma-card:hover .diploma-img img { transform: scale(1.07); filter: none; }
.diploma-body { padding: 1.4rem 1.5rem 1.6rem; }
.diploma-body small { color: var(--gold-ink) !important; font-weight: 700; font-size: .8rem; }
.diploma-body h4 { font-size: 1.4rem !important; margin: .35rem 0 .5rem !important; font-weight: 600; line-height: 1.15; }
.diploma-body p { color: var(--muted); font-size: .88rem; line-height: 1.65; margin: 0; }

/* ---------- Formulario ---------- */
[data-testid="stForm"] { background: var(--surface) !important; border: 1px solid var(--line) !important;
  border-radius: 22px !important; padding: 2.2rem 2.2rem 1.6rem !important; box-shadow: 0 24px 60px var(--shadow); }
[data-testid="stForm"] label p { font-weight: 600 !important; font-size: .88rem !important; color: var(--ink) !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div {
  background: var(--bg) !important; color: var(--ink) !important; border-radius: 12px !important;
  border: 1px solid var(--line) !important; transition: border-color .3s, box-shadow .3s; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color: var(--ink) !important; }
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus {
  border-color: var(--gold) !important; box-shadow: 0 0 0 3px var(--gold-soft) !important; }
[data-testid="stTextInput"] > div > div, [data-testid="stTextArea"] > div > div { border: none !important; background: transparent !important; }
[data-testid="stFormSubmitButton"] > button {
  background: var(--ink) !important; color: var(--bg) !important; border: none !important; border-radius: 999px !important;
  padding: .85rem 2.2rem !important; font-weight: 700 !important; transition: transform .3s, box-shadow .3s, background-color .3s !important; }
[data-testid="stFormSubmitButton"] > button p { color: var(--bg) !important; }
[data-testid="stFormSubmitButton"] > button:hover { background: var(--gold) !important; transform: translateY(-2px); box-shadow: 0 14px 34px var(--shadow) !important; }
[data-testid="stFormSubmitButton"] > button:hover p { color: #1F1B16 !important; }
.form-note { display: flex; gap: 10px; align-items: center; justify-content: center; color: var(--muted); font-size: .88rem; margin-top: 1rem; }
.success { display: flex; gap: 12px; align-items: center; padding: 1rem 1.2rem; border-radius: 12px; margin-top: 1rem;
  background: rgba(46,139,87,.10); border: 1px solid rgba(46,139,87,.35); color: #2E8B57; font-weight: 600;
  animation: pop .5s cubic-bezier(.34,1.56,.64,1); }
.success span { color: #2E8B57 !important; }
@keyframes pop { from { transform: scale(.94); opacity: 0; } }

/* ---------- Footer ---------- */
.site-footer { margin-top: 5rem; padding: 2.5rem 0 1rem; border-top: 1px solid var(--line);
  display: flex; justify-content: space-between; flex-wrap: wrap; gap: 1rem; color: var(--muted); font-size: .88rem; }
.site-footer b { color: var(--ink); font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; }
.site-footer span { color: var(--muted); }

/* ---------- WhatsApp flotante ---------- */
.wa-float { position: fixed; right: 22px; bottom: 22px; z-index: 1000000; width: 58px; height: 58px; border-radius: 50%;
  background: #25D366; display: grid; place-items: center; box-shadow: 0 12px 30px rgba(37,211,102,.35);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1); }
.wa-float:hover { transform: scale(1.1) rotate(-6deg); }
.wa-float::before { content: ""; position: absolute; inset: 0; border-radius: 50%; border: 2px solid #25D366;
  animation: ping 2.4s cubic-bezier(0,0,.2,1) infinite; }

/* ---------- Revelado al hacer scroll (solo si JS está activo) ---------- */
.js-reveal .reveal { opacity: 0; transform: translateY(28px); transition: opacity .9s ease, transform .9s cubic-bezier(.2,.8,.2,1); }
.js-reveal .reveal.in { opacity: 1; transform: none; }

/* ---------- Responsive ---------- */
@media (max-width: 900px) {
  .hero, .team { grid-template-columns: 1fr; gap: 2rem; }
  .scale-stage { max-width: 260px; margin: 0 auto; order: -1; }
  .areas, .diplomas, .steps { grid-template-columns: 1fr; }
  .nav-links a:not(.nav-cta) { display: none; }
  .urgent { grid-template-columns: auto 1fr; }
  .urgent-phones { grid-column: 1 / -1; }
  .section-head { flex-direction: column; align-items: flex-start; gap: .8rem; }
  .step { padding-right: 0; }
}

/* ---------- Accesibilidad: movimiento reducido ---------- */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  .hero-title .line > span { transform: none; }
  .hero-sub, .hero-actions { opacity: 1; }
  .js-reveal .reveal { opacity: 1; transform: none; }
}
"""

st.markdown(f"<style>{css_vars}{CSS}</style>", unsafe_allow_html=True)

# =========================================================
# ÍCONOS
# =========================================================
G = tokens["gold"]
GI = tokens["gold_ink"]

nav_logo_svg = f"""<svg width="32" height="32" viewBox="0 0 36 36" fill="none" stroke="{G}" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="18" r="16" stroke-width="1.5"/><path d="M18 9v18M12 27h12M11 14h14M11 14l-3 8h6l-3-8zM25 14l-3 8h6l-3-8z" stroke-width="1.5"/></svg>"""

hero_scale_svg = f"""
<svg class="scale-svg" viewBox="0 0 320 300" fill="none" stroke="{G}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
<path d="M160 60v190" stroke-width="4"/>
<path d="M110 262h100M130 262l30-14 30 14" stroke-width="4"/>
<circle cx="160" cy="52" r="9" fill="{G}" stroke="none"/>
<g class="scale-beam">
<path d="M40 70h240" stroke-width="5"/>
<g class="scale-pan-l">
<path d="M50 72l-30 82M50 72l30 82" stroke-width="2"/>
<path d="M14 154h72c0 18-16 30-36 30s-36-12-36-30z" fill="{G}" fill-opacity=".22" stroke-width="2.5"/>
</g>
<g class="scale-pan-r">
<path d="M270 72l-30 82M270 72l30 82" stroke-width="2"/>
<path d="M234 154h72c0 18-16 30-36 30s-36-12-36-30z" fill="{G}" fill-opacity=".22" stroke-width="2.5"/>
</g>
</g>
</svg>"""

def icon(path_d: str) -> str:
    return f"""<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{GI}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{path_d}</svg>"""

icon_shield = icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>')
icon_family = icon('<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M3 20v-1a5 5 0 0 1 10 0v1"/><path d="M14 20v-.5a3.5 3.5 0 0 1 7 0v.5"/>')
icon_work = icon('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M16 7V4a1 1 0 0 0-1-1h-6a1 1 0 0 0-1 1v3"/><path d="M3 13h18"/>')

icon_mail = f"""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{GI}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,6 12,13 2,6"/></svg>"""
icon_phone = f"""<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{GI}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>"""
icon_lock = f"""<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{GI}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>"""
icon_check = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>"""
icon_wa = """<svg width="28" height="28" viewBox="0 0 24 24" fill="#FFFFFF"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5h-.01a9.45 9.45 0 0 1-4.82-1.32l-.35-.21-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.47 9.48-9.47a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.7c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.53A11.32 11.32 0 0 0 12.04.64C5.76.64.65 5.75.65 12.03c0 2.01.52 3.97 1.52 5.7L.55 23.6l6.02-1.58a11.36 11.36 0 0 0 5.47 1.39h.01c6.28 0 11.39-5.11 11.39-11.39 0-3.04-1.18-5.9-3.34-8.05z"/></svg>"""

PHONE_DISPLAY = "+56 9 5492 2730"
PHONE_TEL = "+56954922730"
EMAIL = "Lex.Mfrancisca@gmail.com"
WA_LINK = "https://wa.me/56954922730?text=Hola%2C%20quisiera%20agendar%20una%20consulta%20confidencial."

# =========================================================
# NAVBAR + PROGRESO + WHATSAPP
# =========================================================
html(f"""
<div class="scroll-progress"></div>
<nav class="custom-navbar" aria-label="Navegación principal">
  <a href="#inicio" class="nav-brand" data-scroll="inicio">{nav_logo_svg}<span style="color:var(--ink)">Abogadas Hermandad</span></a>
  <div class="nav-links">
    <a href="#areas" data-scroll="areas">Áreas</a>
    <a href="#proceso" data-scroll="proceso">Cómo trabajamos</a>
    <a href="#equipo" data-scroll="equipo">Equipo</a>
    <a href="#casos" data-scroll="casos">Casos</a>
    <a href="#contacto" data-scroll="contacto" class="nav-cta">Agendar consulta</a>
  </div>
</nav>
<a class="wa-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}</a>
""")

# Botón de tema (fijo abajo a la izquierda)
st.button(toggle_label, on_click=toggle_theme, key="theme_btn")

# =========================================================
# HERO
# =========================================================
html(f"""
<section class="hero" id="inicio">
  <div>
    <div class="hero-kicker">Estudio jurídico de la mujer · Chile</div>
    <h1 class="hero-title">
      <span class="line"><span>Defensa legal</span></span>
      <span class="line"><span>especializada, humana</span></span>
      <span class="line"><span>y sin prejuicios.</span></span>
    </h1>
    <p class="hero-sub">Te acompañamos con rigor técnico y absoluta confidencialidad en violencia intrafamiliar, derecho de familia y acoso laboral. Te explicamos cada paso en lenguaje claro.</p>
    <div class="hero-actions">
      <a class="btn-solid" href="#contacto" data-scroll="contacto"><span>Agendar consulta confidencial</span></a>
      <a class="btn-ghost" href="tel:{PHONE_TEL}">{icon_phone}<span>Llamar ahora</span></a>
    </div>
  </div>
  <div class="scale-stage">{hero_scale_svg}</div>
</section>
""")

# =========================================================
# URGENCIA
# =========================================================
html(f"""
<div class="urgent reveal" role="note">
  <div class="urgent-dot"></div>
  <div>
    <h4>¿Estás en riesgo ahora?</h4>
    <p>Ante violencia intrafamiliar aguda, llama de inmediato a Carabineros o SernamEG. Después, nosotras gestionamos con urgencia las medidas de protección y alejamiento.</p>
  </div>
  <div class="urgent-phones">
    <a class="phone-chip" href="tel:149"><b>149</b><small>Fono Familia</small></a>
    <a class="phone-chip" href="tel:1455"><b>1455</b><small>SernamEG</small></a>
  </div>
</div>
""")

# =========================================================
# ÁREAS DE PRÁCTICA
# =========================================================
areas = [
    (icon_shield, "Protección y VIF",
     "Tramitación prioritaria de medidas cautelares y querellas criminales por agresiones.",
     ["Prohibición de acercamiento", "Salida del agresor del hogar común", "Querellas por lesiones"]),
    (icon_family, "Derecho de familia",
     "Representación completa en los procesos que definen el bienestar de tus hijos y tu patrimonio.",
     ["Pensión de alimentos y retención AFP", "Cuidado personal y visitas", "Divorcios"]),
    (icon_work, "Acoso laboral · Ley Karin",
     "Intervención estratégica ante acoso laboral o sexual y vulneración de derechos en el trabajo.",
     ["Tutela de derechos fundamentales", "Despido indirecto", "Despido por maternidad"]),
]
cards = "".join(
    f"""<article class="service-card reveal" style="transition-delay:{i*0.1}s">
    <div class="service-icon">{ic}</div><h3>{t}</h3><p>{d}</p>
    <ul>{''.join(f'<li>{x}</li>' for x in items)}</ul></article>"""
    for i, (ic, t, d, items) in enumerate(areas)
)
html(f"""
<section class="section" id="areas">
  <div class="section-head reveal">
    <h2>Áreas de especialización</h2>
    <p>Tres áreas, un mismo enfoque: proteger tus derechos con estrategia y con la contención que cada caso necesita.</p>
  </div>
  <div class="areas">{cards}</div>
</section>
""")

# =========================================================
# CÓMO TRABAJAMOS
# =========================================================
steps = [
    ("Primera conversación", "Nos cuentas tu situación con total confidencialidad. Evaluamos riesgos y opciones reales."),
    ("Estrategia clara", "Te proponemos un plan de acción, plazos y costos, explicado sin tecnicismos."),
    ("Representación", "Llevamos tu causa ante tribunales y te mantenemos informada en cada etapa."),
]
steps_html = "".join(
    f"""<div class="step reveal" style="transition-delay:{i*0.15}s"><div class="step-n">{i+1}</div><h4>{t}</h4><p>{d}</p></div>"""
    for i, (t, d) in enumerate(steps)
)
html(f"""
<section class="section" id="proceso">
  <div class="section-head reveal">
    <h2>Cómo trabajamos</h2>
    <p>Un proceso simple para que sepas siempre en qué punto está tu caso.</p>
  </div>
  <div class="steps reveal">{steps_html}</div>
</section>
""")

# =========================================================
# EQUIPO
# =========================================================
photo = image_to_data_uri("fran.jpg")
portrait = (
    f'<img src="{photo}" alt="Retrato de María-Francisca Valentina" />'
    if photo else '<div class="monogram">MF</div>'
)
html(f"""
<section class="section" id="equipo">
  <div class="team">
    <div class="portrait reveal">{portrait}</div>
    <div class="reveal" style="transition-delay:.15s">
      <div class="team-role">Abogada fundadora</div>
      <h3>María-Francisca Valentina</h3>
      <p class="team-bio">Abogada especialista en violencia de género, familia, penal y laboral. Combina litigación técnica con un acompañamiento cercano para la protección integral de tus derechos.</p>
      <blockquote class="quote">Ninguna mujer debería enfrentar sola un proceso judicial. Mi trabajo es que tengas claridad y respaldo en cada decisión.</blockquote>
      <div class="contact-row">
        <a class="contact-pill" href="mailto:{EMAIL}">{icon_mail}<span>{EMAIL}</span></a>
        <a class="contact-pill" href="tel:{PHONE_TEL}">{icon_phone}<span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </div>
</section>
""")

# =========================================================
# CASOS DESTACADOS (CARRUSEL)
# =========================================================
cases = [
    ("Protección y VIF", "Medida cautelar en 24 horas",
     "Prohibición de acercamiento y salida del agresor del hogar común, otorgadas por el Juzgado de Familia de Santiago."),
    ("Pensión de alimentos", "Retención de fondos AFP",
     "Cobro efectivo de una deuda histórica superior a $14.000.000 mediante retención judicial de fondos previsionales."),
    ("Tutela laboral", "Acoso laboral · Ley Karin",
     "Sentencia favorable con indemnización por vulneración de derechos fundamentales y despido indirecto."),
    ("Derecho de familia", "Cuidado personal definitivo",
     "Resolución que resguarda el interés superior del niño, con régimen de visitas estructurado y evaluación psicológica."),
    ("Derecho penal", "Querella por lesiones VIF",
     "Condena firme del Tribunal de Juicio Oral en lo Penal con prohibición absoluta de contacto."),
]
case_cards = "".join(
    f"""<div class="case-card"><span class="case-badge">{b}</span><h4>{t}</h4><p>{d}</p></div>"""
    for b, t, d in cases
)
html(f"""
<section class="section" id="casos">
  <div class="section-head reveal">
    <h2>Casos destacados</h2>
    <p>Resoluciones obtenidas para nuestras clientas. Pasa el cursor sobre el carrusel para leer con calma.</p>
  </div>
  <div class="marquee reveal"><div class="marquee-track">{case_cards}{case_cards}</div></div>
  <p class="disclaimer">Casos anonimizados. Los resultados anteriores no garantizan resultados futuros.</p>
</section>
""")

# =========================================================
# DIPLOMAS Y CERTIFICACIONES
# =========================================================
diplomas = [
    ("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=800&auto=format&fit=crop",
     "Universidad de Chile", "Diplomado en Derecho de Familia",
     "Litigación oral y medidas cautelares en tribunales de familia."),
    ("https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=800&auto=format&fit=crop",
     "Pontificia Universidad Católica", "Certificación Ley Karin y género",
     "Prevención, tutela de derechos fundamentales y acoso laboral en Chile."),
    ("https://images.unsplash.com/photo-1450133064473-71024230f91b?q=80&w=800&auto=format&fit=crop",
     "Academia Judicial / UDP", "Postítulo en Derecho Penal y VIF",
     "Estrategia penal e interposición de querellas por agresiones graves."),
]
dip_html = "".join(
    f"""<article class="diploma-card reveal" style="transition-delay:{i*0.1}s">
    <div class="diploma-img"><img src="{img}" alt="{t}" loading="lazy"/></div>
    <div class="diploma-body"><small>{inst}</small><h4>{t}</h4><p>{d}</p></div></article>"""
    for i, (img, inst, t, d) in enumerate(diplomas)
)
html(f"""
<section class="section" id="formacion">
  <div class="section-head reveal">
    <h2>Formación académica</h2>
    <p>Especialización continua en las materias que defendemos.</p>
  </div>
  <div class="diplomas">{dip_html}</div>
</section>
""")

# =========================================================
# FORMULARIO DE CONSULTA
# =========================================================
html("""
<section class="section" id="contacto" style="padding-bottom:1.5rem">
  <div class="section-head reveal">
    <h2>Agenda tu consulta confidencial</h2>
    <p>Cuéntanos lo esencial. Te respondemos personalmente por el medio que prefieras.</p>
  </div>
</section>
""")

with st.form("contact_form", clear_on_submit=True):
    fc1, fc2 = st.columns(2)
    with fc1:
        nombre = st.text_input("Nombre completo", placeholder="Tu nombre")
        telefono = st.text_input("Teléfono o WhatsApp", placeholder="+56 9 ...")
    with fc2:
        correo = st.text_input("Correo electrónico", placeholder="nombre@correo.cl")
        materia = st.selectbox("Materia de la consulta", [
            "Violencia intrafamiliar (VIF) / Alejamiento",
            "Pensión de alimentos / Retención de fondos",
            "Cuidado personal / Visitas",
            "Acoso laboral / Ley Karin",
            "Otra consulta legal",
        ])
    mensaje = st.text_area("Cuéntanos brevemente tu caso", placeholder="No necesitas usar términos legales.", height=130)

    submitted = st.form_submit_button("Enviar consulta confidencial")

    if submitted:
        if nombre and (telefono or correo):
            html(f"""<div class="success">{icon_check}<span>Consulta enviada. Te contactaremos a la brevedad.</span></div>""")
        else:
            st.error("Completa tu nombre y al menos un medio de contacto (teléfono o correo) para poder responderte.")

    html(f"""<div class="form-note">{icon_lock}<span style="color:var(--muted)">Protegido por secreto profesional. Tus datos no se comparten con terceros.</span></div>""")

# =========================================================
# FOOTER
# =========================================================
html(f"""
<footer class="site-footer">
  <div><b>Abogadas Hermandad</b><br><span>Estudio jurídico de la mujer en Chile</span></div>
  <div style="text-align:right"><span>{EMAIL} · {PHONE_DISPLAY}</span><br><span>© 2026 Todos los derechos reservados</span></div>
</footer>
""")

# =========================================================
# INTERACCIONES: scroll suave, navbar, progreso, revelado,
# foco de luz en tarjetas y sonido de clic en madera
# =========================================================
components.html("""
<script>
(function () {
  const win = window.parent;
  const doc = win.document;
  const reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Revelado al hacer scroll ----------
  doc.documentElement.classList.add('js-reveal');
  if (!win.__hermandadIO) {
    win.__hermandadIO = new win.IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); win.__hermandadIO.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  }
  const observeAll = () => doc.querySelectorAll('.reveal:not(.in), .steps:not(.in)').forEach(el => {
    if (reduce) { el.classList.add('in'); } else { win.__hermandadIO.observe(el); }
  });
  observeAll();
  if (!win.__hermandadMO) {
    win.__hermandadMO = new win.MutationObserver(() => observeAll());
    win.__hermandadMO.observe(doc.body, { childList: true, subtree: true });
  }

  if (win.__hermandadInit) return;
  win.__hermandadInit = true;

  // ---------- Scroll suave para enlaces internos ----------
  doc.addEventListener('click', (e) => {
    const link = e.target.closest('[data-scroll]');
    if (!link) return;
    const target = doc.getElementById(link.dataset.scroll);
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
  });

  // ---------- Navbar compacta, barra de progreso y enlace activo ----------
  const ids = ['areas', 'proceso', 'equipo', 'casos', 'contacto'];
  doc.addEventListener('scroll', (e) => {
    const el = e.target === doc ? doc.scrollingElement : e.target;
    if (!el || !el.scrollHeight) return;
    const max = el.scrollHeight - el.clientHeight;
    const y = el.scrollTop;
    const nav = doc.querySelector('.custom-navbar');
    const bar = doc.querySelector('.scroll-progress');
    if (nav) nav.classList.toggle('is-scrolled', y > 30);
    if (bar && max > 0) bar.style.setProperty('--progress', Math.min(y / max, 1));
    let current = null;
    ids.forEach(id => {
      const s = doc.getElementById(id);
      if (s && s.getBoundingClientRect().top < 160) current = id;
    });
    doc.querySelectorAll('.nav-links a').forEach(a => a.classList.toggle('active', a.dataset.scroll === current));
  }, true);

  // ---------- Foco de luz que sigue al cursor en tarjetas ----------
  doc.addEventListener('pointermove', (e) => {
    const card = e.target.closest && e.target.closest('.service-card');
    if (!card) return;
    const r = card.getBoundingClientRect();
    card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    card.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });

  // ---------- Sonido de clic en madera ----------
  let ctx = null;
  function playWoodClick() {
    const AC = win.AudioContext || win.webkitAudioContext;
    if (!AC) return;
    ctx = ctx || new AC();
    const t = ctx.currentTime;
    const tone = (f0, f1, g, dur) => {
      const o = ctx.createOscillator(), gn = ctx.createGain();
      o.type = 'sine';
      o.frequency.setValueAtTime(f0, t);
      o.frequency.exponentialRampToValueAtTime(f1, t + dur * 0.85);
      gn.gain.setValueAtTime(g, t);
      gn.gain.exponentialRampToValueAtTime(0.001, t + dur);
      o.connect(gn); gn.connect(ctx.destination);
      o.start(t); o.stop(t + dur + 0.01);
    };
    tone(1050, 400, 0.6, 0.04);
    tone(1600, 800, 0.25, 0.025);
    const size = Math.floor(ctx.sampleRate * 0.008);
    const buf = ctx.createBuffer(1, size, ctx.sampleRate);
    const d = buf.getChannelData(0);
    for (let i = 0; i < size; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (size * 0.25));
    const n = ctx.createBufferSource(); n.buffer = buf;
    const f = ctx.createBiquadFilter(); f.type = 'bandpass'; f.frequency.value = 1300; f.Q.value = 2.5;
    const g = ctx.createGain(); g.gain.setValueAtTime(0.35, t); g.gain.exponentialRampToValueAtTime(0.001, t + 0.012);
    n.connect(f); f.connect(g); g.connect(ctx.destination); n.start(t);
  }
  doc.addEventListener('mousedown', (e) => {
    if (e.target.closest('[data-testid="stButton"] button, [data-testid="stFormSubmitButton"] button, .btn-solid, .nav-cta')) {
      playWoodClick();
    }
  });
})();
</script>
""", height=0, width=0)
