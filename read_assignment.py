import pdfplumber
import os

pdf_path = "d:/Intern_project/NIYAMR_48_Hour_Intern_Assignment.pdf"

if os.path.exists(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            print(text)
    except Exception as e:
        print(f"Error reading PDF: {e}")
else:
    print(f"File not found: {pdf_path}")
