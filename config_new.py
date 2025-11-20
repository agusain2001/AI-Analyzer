import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the AI Agent"""
    
    # API Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = "gemini-2.5-flash"
    
    # PDF Configuration
    PDF_PATH = "data/ukpga_20250022_en.pdf"
    
    # Output Configuration
    OUTPUT_DIR = "output"
    JSON_OUTPUT_FILE = "universal_credit_act_analysis.json"
    
    # LLM Configuration
    TEMPERATURE = 0.3
    MAX_OUTPUT_TOKENS = 8192
    TOP_P = 0.95
    TOP_K = 40
