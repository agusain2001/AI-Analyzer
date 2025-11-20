# Universal Credit Act 2025 AI Analyzer

## NIYAMR AI - 48-Hour Internship Assignment

### 🎯 Objective
Build a mini AI agent that can read, summarize, and analyse the Universal Credit Act 2025 and return a structured JSON report.

### ✨ Features
- ✅ **Task 1**: Extract full text from PDF using pdfplumber + PyPDF2
- ✅ **Task 2**: Summarize the Act in 5-10 bullet points
- ✅ **Task 3**: Extract key legislative sections (definitions, obligations, etc.)
- ✅ **Task 4**: Apply 6 rule validation checks with evidence and confidence scores

### 🛠️ Technology Stack
- **LLM**: Google Gemini 2.5 Flash (state-of-the-art reasoning model)
- **PDF Processing**: pdfplumber, PyPDF2
- **UI**: Streamlit
- **Language**: Python 3.9+

### 📁 Project Structure
```
universal-credit-ai-agent/
├── data/
│   └── ukpga_20250022_en.pdf        # Input PDF
├── output/
│   └── universal_credit_act_analysis.json  # Generated analysis
├── config.py                         # Configuration settings
├── pdf_extractor.py                  # PDF text extraction
├── gemini_analyzer.py                # Gemini AI integration
├── ai_agent.py                       # Main orchestration logic
├── streamlit_app.py                  # Streamlit UI
├── requirements.txt                  # Python dependencies
├── .env.example                      # Environment variables template
└── README.md                         # This file
```

### 🚀 Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd universal-credit-ai-agent
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

5. **Get Gemini API Key**
- Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create a new API key
- Add it to your `.env` file

### 💻 Usage

#### Option 1: Command Line Interface
```bash
python ai_agent.py
```

#### Option 2: Streamlit Web App
```bash
streamlit run streamlit_app.py
```

Then open your browser to `http://localhost:8501`

### 📊 Output Format

The AI agent generates a comprehensive JSON report with:

```json
{
  "metadata": {
    "act_title": "Universal Credit Act 2025",
    "chapter": "22",
    "analysis_date": "2025-01-15T10:30:00",
    "analyzer": "Gemini 2.5 Flash"
  },
  "task_2_summary": [...],
  "task_3_key_sections": {
    "definitions": "...",
    "obligations": "...",
    "responsibilities": "...",
    "eligibility": "...",
    "payments": "...",
    "penalties": "...",
    "record_keeping": "..."
  },
  "task_4_rule_checks": [
    {
      "rule": "Act must define key terms",
      "status": "pass",
      "evidence": "...",
      "confidence": 95
    }
  ]
}
```

### 🎥 Video Demonstration

A 2-minute video demonstration is available explaining:
1. Project architecture and design decisions
2. How Gemini 2.5 Flash is used for analysis
3. Demo of the Streamlit interface
4. Results interpretation

### 🏗️ Architecture

```
┌─────────────────┐
│   Streamlit UI  │
└────────┬────────┘
         │
┌────────▼────────┐
│   AI Agent      │
│  (Orchestrator) │
└────┬───────┬────┘
     │       │
┌────▼───┐ ┌▼──────────────┐
│  PDF   │ │ Gemini 2.5    │
│Extractor│ │   Analyzer    │
└────────┘ └───────────────┘
```

### 🤖 Why Gemini 2.5 Flash?

- **State-of-the-art reasoning**: Advanced capabilities for legal document analysis
- **Cost-effective**: Best price-performance ratio in the Gemini family
- **Fast**: 2x faster than Gemini 1.5 Pro
- **Large context**: 1M token context window
- **Built-in tools**: Native code execution and search capabilities

### 📝 Implementation Highlights

1. **Robust PDF Extraction**: Dual-method approach (pdfplumber + PyPDF2) with fallback
2. **Intelligent Text Cleaning**: Regex-based cleaning for optimal LLM processing
3. **Structured Prompting**: Carefully crafted prompts for accurate JSON extraction
4. **Error Handling**: Comprehensive try-catch blocks with fallback mechanisms
5. **Modular Design**: Separation of concerns for maintainability

### 📦 Dependencies

- `google-genai==1.0.0` - Official Gemini API client
- `PyPDF2==3.0.1` - PDF text extraction
- `pdfplumber==0.11.0` - Advanced PDF parsing
- `streamlit==1.32.0` - Web interface
- `python-dotenv==1.0.1` - Environment variable management

### 🔒 Security

- API keys stored in `.env` (not committed to git)
- `.gitignore` configured to exclude sensitive files
- Environment variables for configuration

### 🧪 Testing

Run the complete analysis:
```bash
python ai_agent.py
```

Expected output:
- Clean text extraction from PDF
- 5-10 bullet point summary
- 7 key section extractions
- 6 rule check validations with evidence

### 📈 Future Enhancements

- [ ] Batch processing for multiple acts
- [ ] Comparative analysis between different acts
- [ ] Export to additional formats (Word, HTML)
- [ ] Integration with legal databases
- [ ] Multi-language support

### 👨‍💻 Author

**NIYAMR AI Internship Candidate**
- Submission Date: [Your submission date]
- Completion Time: 48 hours
- Technology: Python + Gemini 2.5 Flash + Streamlit