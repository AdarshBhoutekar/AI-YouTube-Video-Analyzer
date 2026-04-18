# AI YouTube Video Analyzer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered web application that analyzes YouTube videos, extracts meaningful timestamps, and generates structured content summaries using the Groq API (Llama 3) and Agno agents.

## Features

- **Comprehensive Video Analysis:** Get instant overviews, identify video types (tutorials, reviews, etc.), and understand the core content structure.
- **Smart Timestamping:** Automatically generates precise and meaningful timestamps highlighting key topic transitions.
- **Advanced AI Engine:** Powered by Groq's lightning-fast `llama-3.3-70b-versatile` model via the Agno Agent framework.
- **Interactive UI:** Clean, user-friendly interface built with Streamlit.

## Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Framework:** [Agno](https://github.com/agno-ai/agno)
- **LLM Provider:** [Groq](https://groq.com/)
- **Language:** Python 3

## Repository Structure

```text
├── ui.py                  # Main Streamlit application and UI
├── youtube_analyzer.py    # Configures the Agno agent and Groq model
├── requirements.txt       # Project dependencies
├── .env                   # API keys (Not tracked by Git)
└── .gitignore             # Files/folders to ignore in Git
```

## Installation & Run Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AdarshBhoutekar/AI-YouTube-Video-Analyzer.git
   cd AI-YouTube-Video-Analyzer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # On Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

5. **Run the application:**
   ```bash
   streamlit run ui.py
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
