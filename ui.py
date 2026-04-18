import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube video analyzer",
    layout="centered",
)

st.title("AI YouTube video analyzer")

# cache: Fast access for the agent
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# input box
video_url = st.text_input(
    "Enter YouTube video link",
    placeholder="https://www.youtube.com/watch?v=..."
    )
button = st.button("Analyze video")

# analysis
if button:
    cleaned_url = video_url.strip()

    if not cleaned_url:
        st.warning("Please enter a YouTube video link.")
    else:
        with st.spinner("Analyzing video..."):
            try:
                response = agent.run(f"Analyze this video: {cleaned_url}")
                st.success("Analysis Complete !")
                st.markdown("### Report")
                st.markdown(response.content)
            except Exception as exc:
                st.error(f"Could not analyze the video: {exc}")
            