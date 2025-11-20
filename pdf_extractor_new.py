import PyPDF2
import pdfplumber
import re
from typing import Dict, List

class PDFExtractor:
    """Extracts and cleans text from PDF documents"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        
    def extract(self) -> Dict[str, any]:
        """Extract text using dual method (pdfplumber + PyPDF2 fallback)"""
        text = ""
        method = "pdfplumber"
        
        try:
            # Primary method: pdfplumber (better for layout)
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            print(f"pdfplumber failed: {e}. Falling back to PyPDF2.")
            method = "PyPDF2"
            try:
                # Fallback method: PyPDF2
                with open(self.pdf_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    for page in reader.pages:
                        text += page.extract_text() or ""
            except Exception as e2:
                print(f"PyPDF2 also failed: {e2}")
                return {"raw_text": "", "cleaned_text": "", "length": 0}
        
        cleaned_text = self.clean_text(text)
        
        return {
            "raw_text": text,
            "cleaned_text": cleaned_text,
            "length": len(cleaned_text)
        }
    
    def clean_text(self, text: str) -> str:
        """Clean extracted text"""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove page numbers (simple heuristic)
        text = re.sub(r'\n\d+\n', '\n', text)
        # Fix broken words (hyphenation)
        text = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', text)
        # Normalize paragraphs
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text.strip()
