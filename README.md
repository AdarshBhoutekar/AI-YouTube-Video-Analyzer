<div align="center">
  <h1>AI YouTube Video Analyzer</h1>
  <p>
    <strong>A high-performance web application for extracting structured insights from YouTube content using Large Language Models.</strong>
  </p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
  [![Python version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat-square)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg?style=flat-square)](https://streamlit.io/)
</div>

<br />

### Live Demo : [Launch AI YouTube Video Analyzer](https://ai-youtube-video-analyzer.streamlit.app/)

---

## About the Project

The **AI YouTube Video Analyzer** is a robust analytical interface engineered to parse, process, and summarize long-form YouTube video transcripts. Utilizing Groq's high-speed inference engine alongside the Agno agent framework, the application delivers near-instantaneous contextual breakdowns of video content. 

This tool is designed to optimize time consumption for researchers, students, and professionals by converting extensive video dependencies into highly structured, actionable, and searchable text documents.

## Core Features

- **Automated Summarization:** Rapid assimilation of full video transcripts into executive summaries and detailed synopses.
- **Intelligent Timestamping:** Algorithmic identification of key topic transitions mapped to structural timestamps.
- **Sentiment Analysis:** Automated detection of the underlying communicative tone of the video subject matter.
- **Data Portability:** Seamless exportation of generated intelligence into locally saved, formatted `.txt` reports.
- **Glassmorphic UI Engine:** A bespoke, responsive interface utilizing custom DOM injection over Streamlit, optimized for desktop and mobile reading.

## Architecture

The system functions on a decoupled front-end and back-end integration:

```text
├── app.py                 # Core routing, error handling, and orchestrator 
├── ui.py                  # Custom UI component library and CSS injection
├── youtube_analyzer.py    # LLM configurations, prompt engineering, and Agno agent definitions
├── requirements.txt       # Version-locked environment dependencies
└── CODEBASE_EXPLANATION.md# Extensive developer documentation regarding data-flow
```

## Getting Started

To configure a local development environment, follow these technical guidelines.

### Prerequisites

You must have the following dependencies active on your local environment:
- **Python:** Version 3.10 or newer.
- **Groq API Key:** An active developer key from [Groq Console](https://console.groq.com/keys).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AdarshBhoutekar/AI-YouTube-Video-Analyzer.git
   cd AI-YouTube-Video-Analyzer
   ```

2. **Initialize a virtual environment:**
   ```bash
   # Windows environments
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # Unix/macOS environments
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install module dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and securely assign your API key:
   ```env
   GROQ_API_KEY="INSERT_YOUR_GROQ_API_KEY"
   ```

### Execution

Initialize the local server via the Streamlit CLI:
```bash
streamlit run app.py
```
*The local development server will deploy to `http://localhost:8501/`.*

## Troubleshooting

- **Invalid YouTube URL Exception:** Valid inputs must contain a standard YouTube video ID (e.g., standard `?v=`, `youtu.be/`, or `/shorts/` formats).
- **Rate Limit Constraints:** Submitting excessive queries against the Groq free-tier will yield a 429 Rate Limit error. The application gracefully catches this and alerts the user interface; wait for the bucket allocation to clear before resuming.

## License

This architecture is distributed under the MIT License. See `LICENSE` for complete documentation.

---
<div align="center">
  <p>Engineered and maintained by <a href="https://github.com/AdarshBhoutekar">Adarsh Bhoutekar</a></p>
</div>
