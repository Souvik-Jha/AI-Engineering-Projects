# AI Engineering Playground 🚀

A collection of hands-on AI engineering projects built with Python and Large Language Models (LLMs). This repository explores practical applications of LLM APIs, web scraping, prompt engineering, and multi-model comparison.

## 📌 Projects

### 1. AI Website Summarizer 🔎

An AI-powered application that extracts content from a webpage and generates a concise summary using an LLM.

**Features**
- Accepts a webpage URL as input.
- Extracts webpage content using Requests and BeautifulSoup.
- Removes unnecessary HTML elements such as scripts, navigation, and footer sections.
- Uses OpenAI's GPT-4o-mini to generate a summary.
- Displays the generated summary in Markdown format.

**Workflow**

User URL → Web Scraper → Content Extraction → LLM → Generated Summary

### 2. LLM Arena 🥊

An interactive application that compares responses from two different LLM providers using the same user prompt.

**Features**
- Sends the same prompt to two different LLMs.
- Integrates OpenAI and Groq APIs.
- Displays model responses side by side.
- Allows users to vote for their preferred response.
- Uses the OpenAI-compatible API interface to communicate with different providers.

**Models**
- OpenAI: GPT-4o-mini
- Groq: GPT-OSS-120B

**Workflow**

User Prompt → OpenAI API → Model A Response

User Prompt → Groq API → Model B Response

Both responses → Side-by-side Comparison → User Vote

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Gradio | Web interface |
| OpenAI API | LLM integration |
| Groq API | LLM inference |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing and content extraction |
| Python-dotenv | Environment variable management |

## 📂 Project Structure

```text
AI-engg-scripts/
│
├── app.py                 # Website Summarizer UI
├── arena_app.py           # LLM Arena UI
├── scraper.py             # Webpage content extraction
├── summarizer.py          # LLM-based summarization
│
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .env.example           # Environment variable template
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Souvik-Jha/AI-engg-scripts.git

cd AI-engg-scripts
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

Add the API keys from:

- [OpenAI Platform](https://platform.openai.com/api-keys)
- [Groq Console](https://console.groq.com/keys)

Keep your `.env` file private. Never commit API keys to GitHub.

## ▶️ Running the Applications

### Run AI Website Summarizer

```bash
python app.py
```

### Run LLM Arena

```bash
python arena_app.py
```

Each application launches its own Gradio interface.

## 🎯 Learning Objectives

Through these projects, the following AI engineering concepts are explored:

- Integrating third-party LLM APIs.
- Working with OpenAI-compatible API interfaces.
- Prompt engineering and system prompts.
- Web scraping and preprocessing unstructured content.
- Building interactive LLM-powered applications.
- Comparing outputs from different LLM providers.
- Managing API credentials securely.

## 🚧 Future Improvements

- Add multiple summarization styles (short, detailed, bullet points).
- Add URL validation and improved error handling.
- Display token usage and response latency.
- Support additional LLM providers and models.
- Implement response evaluation and comparison metrics.
- Persist user votes and model comparison history.
- Deploy applications for public access.

---

**Author:** Souvik Jha

**GitHub:** [Souvik-Jha](https://github.com/Souvik-Jha)

*Learning by building practical AI engineering applications.*
