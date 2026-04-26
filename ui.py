"""
ui.py — All Streamlit UI components for YouTube Video Summarizer.

This module contains ONLY presentation logic:
  • Page configuration & custom CSS
  • Sidebar, header/hero, input section
  • Output cards & download section
  • Footer

No API calls, no data processing, no business logic.
"""
import re
import streamlit as st

ICONS = {
    "film": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>',
    "zap": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "target": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    "list": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>',
    "clock": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "message": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>',
}

# CSS (private constant)

_CUSTOM_CSS = """
<style>
    /* ─── FONTS ─── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* ─── HIDE STREAMLIT CHROME ─── */
    #MainMenu, footer {visibility: hidden;}
    header {background: transparent !important;}

    /* ─── GLOBAL BACKGROUND ─── */
    .stApp {
        background-color: #0F1117;
    }

    /* ─── SIDEBAR ─── */
    section[data-testid="stSidebar"] {
        background: #161B22 !important;
        border-right: 1px solid #21262D !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: #C9D1D9 !important;
    }

    /* ─── PILLS / BADGES ─── */
    .pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .pill-blue   { background:#1c3a5f; color:#58a6ff; }
    .pill-purple { background:#2d1b69; color:#bc8cff; }
    .pill-green  { background:#0d3b26; color:#3fb950; }
    .pill-orange { background:#3d2200; color:#f0883e; }
    .pill-red    { background:#3b1116; color:#f85149; }

    /* ─── HERO BANNER ─── */
    .hero {
        background: linear-gradient(135deg, #161B22 0%, #0D1117 100%);
        border: 1px solid #21262D;
        border-radius: 16px;
        padding: 48px 40px 40px;
        margin-bottom: 32px;
    }
    .hero h1 {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin-bottom: 8px !important;
        letter-spacing: -0.03em;
    }
    .hero p {
        font-size: 1.15rem;
        color: #8B949E;
        max-width: 520px;
    }
    .hero-accent {
        background: linear-gradient(90deg, #FF6B6B, #FFA94D, #FFD43B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ─── INPUT ─── */
    .stTextInput input {
        background: #161B22 !important;
        border: 1px solid #30363D !important;
        color: #C9D1D9 !important;
        border-radius: 10px !important;
        padding: 14px 18px !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        transition: border-color .2s, box-shadow .2s;
    }
    .stTextInput input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 0 3px rgba(88,166,255,.25) !important;
    }
    .stTextInput label {
        color: #8B949E !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
    }

    /* ─── BUTTON ─── */
    .stButton > button {
        background: linear-gradient(135deg, #FF6B6B, #FFA94D) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 0 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        width: 100% !important;
        transition: transform .15s, box-shadow .25s !important;
        box-shadow: 0 4px 14px rgba(255,107,107,.35) !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(255,107,107,.55) !important;
        color: #fff !important;
    }

    /* ─── DOWNLOAD BUTTON ─── */
    .stDownloadButton > button {
        background: transparent !important;
        border: 1px solid #30363D !important;
        color: #C9D1D9 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: border-color .2s, background .2s !important;
    }
    .stDownloadButton > button:hover {
        border-color: #58a6ff !important;
        background: rgba(88,166,255,.08) !important;
        color: #58a6ff !important;
    }

    /* ─── CARD ─── */
    .card {
        background: #161B22;
        border: 1px solid #21262D;
        border-radius: 14px;
        padding: 28px 28px 24px;
        margin-bottom: 20px;
        transition: border-color .25s;
    }
    .card:hover {
        border-color: #30363D;
    }
    .card-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 14px;
    }
    .card-icon {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
    }
    .card-icon-orange { background: #3d2200; }
    .card-icon-blue   { background: #1c3a5f; }
    .card-icon-green  { background: #0d3b26; }
    .card-icon-purple { background: #2d1b69; }
    .card-icon-red    { background: #3b1116; }
    .card-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #8B949E;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    .card-body {
        color: #C9D1D9;
        font-size: 1rem;
        line-height: 1.7;
    }
    .card-body strong { color: #FFFFFF; }
    .card-body li { margin-bottom: 6px; }

    /* ─── THUMBNAIL ─── */
    .thumb-wrapper {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid #21262D;
        margin-bottom: 20px;
    }
    .thumb-wrapper img {
        width: 100%;
        display: block;
    }

    /* ─── FOOTER ─── */
    .app-footer {
        text-align: center;
        padding: 32px 0 18px;
        color: #484F58;
        font-size: 0.85rem;
        border-top: 1px solid #21262D;
        margin-top: 48px;
    }
    .app-footer a {
        color: #58a6ff;
        text-decoration: none;
    }

    /* ─── ALERTS ─── */
    .stAlert { border-radius: 10px !important; }
</style>
"""

# PUBLIC API — importable functions

def setup_page():
    """Set page config and inject custom CSS. Must be called first."""
    st.set_page_config(
        page_title="YouTube Video Summarizer",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(_CUSTOM_CSS, unsafe_allow_html=True)


def render_sidebar():
    """Render the sidebar with project info and tech stack."""
    with st.sidebar:
        st.markdown("## About")
        st.markdown(
            "**YouTube Video Summarizer** uses Groq‑powered AI "
            "to instantly break down any YouTube video into structured "
            "summaries, key points, timestamps, and more."
        )

        st.markdown("---")
        st.markdown("### How it works")
        st.markdown(
            "1. Paste a YouTube link\n"
            "2. Hit **Generate Summary**\n"
            "3. Read or download your report"
        )

        st.markdown("---")
        st.markdown("### Tech Stack")
        st.markdown(
            '<span class="pill pill-orange">Groq · Llama 3</span>'
            '<span class="pill pill-blue">Agno Agents</span>'
            '<span class="pill pill-purple">Streamlit</span>'
            '<span class="pill pill-green">Python</span>',
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown(
            '<p style="color:#484F58;font-size:0.8rem;">v1.0 · MIT License</p>',
            unsafe_allow_html=True,
        )


def render_header():
    """Render the hero banner at the top of the page."""
    st.markdown(
        """
        <div class="hero">
            <h1>YouTube Video <span class="hero-accent">Summarizer</span></h1>
            <p>Drop a link, get an instant AI‑powered breakdown — key points,
            timestamps, sentiment, and a downloadable report.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_input_section():
    """Render the URL input box and the Generate button.

    Returns:
        tuple[str, bool]: (video_url, button_clicked)
    """
    input_col, btn_col = st.columns([4, 1], gap="medium")

    with input_col:
        video_url = st.text_input(
            "YOUTUBE URL",
            placeholder="https://www.youtube.com/watch?v=...",
        )

    with btn_col:
        st.markdown("<br>", unsafe_allow_html=True)
        clicked = st.button("Generate Summary")

    return video_url, clicked


def render_card(icon: str, label: str, body_md: str, icon_color: str = "orange", is_html: bool = False):
    """Render a styled card. Header is HTML; body uses native st.markdown
    so that markdown (bullets, tables, bold) actually renders."""
    if is_html:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header" style="margin-bottom: 20px;">
                    <div class="card-icon card-icon-{icon_color}">{icon}</div>
                    <span class="card-title">{label}</span>
                </div>
                <div class="card-body">
                    {body_md}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="card" style="padding-bottom: 15px; margin-bottom: 15px;">
                <div class="card-header" style="margin-bottom: 0;">
                    <div class="card-icon card-icon-{icon_color}">{icon}</div>
                    <span class="card-title">{label}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(body_md)


def render_error_rate_limit():
    """Show a user-friendly rate limit error."""
    st.error("**Groq Rate Limit Reached!**")
    st.info(
        "You've hit the free-tier daily token limit (100k tokens/day).  \n"
        "**Options:**\n"
        "- Wait a few minutes and try again\n"
        "- Upgrade at [console.groq.com](https://console.groq.com/settings/billing)\n"
    )


def render_output(sections: dict, vid_id: str | None, raw: str, download_text: str):
    """Render all output cards, thumbnail, and download button.

    Args:
        sections:      parsed {section_name: markdown_content} dict
        vid_id:        YouTube video ID (for thumbnail) or None
        raw:           raw AI response string (for debug expander)
        download_text: pre-built plain-text report for the download button
    """
    # Debug expander
    with st.expander("Show raw AI response (debug)"):
        st.code(raw, language="markdown")

    # ── Thumbnail + Title Row ──
    top_left, top_right = st.columns([1, 2], gap="large")

    with top_left:
        if vid_id:
            st.markdown(
                f'<div class="thumb-wrapper">'
                f'<img src="https://img.youtube.com/vi/{vid_id}/hqdefault.jpg" '
                f'alt="thumbnail">'
                f'</div>',
                unsafe_allow_html=True,
            )

    with top_right:
        title = sections.get("Video Title", "Untitled Video")
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">
                    <div class="card-icon card-icon-red">{ICONS['film']}</div>
                    <span class="card-title">Video Title</span>
                </div>
                <div class="card-body" style="font-size:1.4rem;font-weight:700;color:#fff;">
                    {title}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Keywords pills
        kw = sections.get("Keywords", "")
        if kw:
            pills = "".join(
                f'<span class="pill pill-blue">{k.strip()}</span>'
                for k in kw.split(",") if k.strip()
            )
            st.markdown(pills, unsafe_allow_html=True)

    # ── Short Summary ──
    short = sections.get("Short Summary", "")
    if short:
        render_card(ICONS['zap'], "Short Summary", short, "orange")

    # ── Key Points + Detailed Summary side-by-side ──
    left, right = st.columns(2, gap="medium")

    with left:
        kp = sections.get("Key Points", "")
        if kp:
            render_card(ICONS['target'], "Key Points", kp, "green")

    with right:
        detail = sections.get("Detailed Summary", "")
        if detail:
            render_card(ICONS['list'], "Detailed Summary", detail, "blue")

    # ── Timestamps ──
    ts = sections.get("Timestamps", "")
    if ts:
        render_card(ICONS['clock'], "Timestamps", ts, "purple")

    # ── Sentiment ──
    sent = sections.get("Sentiment", "")
    if sent:
        # Basic markdown to HTML subset for Sentiment text
        html_sent = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', sent)
        html_sent = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_sent)
        html_sent = html_sent.replace('\n', '<br>')
        
        styled_sent = f"<div style='font-size: 1.3rem; font-weight: 500; line-height: 1.6; color: #E5E7EB;'>{html_sent}</div>"
        render_card(ICONS['message'], "Sentiment & Tone", styled_sent, "red", is_html=True)

    # ── Download ──
    st.markdown("<br>", unsafe_allow_html=True)
    dl_col1, dl_col2, _ = st.columns([1, 2, 1])
    with dl_col2:
        st.download_button(
            label="Download Full Report (.txt)",
            data=download_text,
            file_name="video_summary_report.txt",
            mime="text/plain",
        )


def render_footer():
    """Render the page footer."""
    st.markdown(
        """
        <div class="app-footer">
            Built by <a href="https://github.com/AdarshBhoutekar" target="_blank">Adarsh Bhoutekar</a>
            &nbsp;·&nbsp; Powered by Groq &amp; Agno
        </div>
        """,
        unsafe_allow_html=True,
    )
