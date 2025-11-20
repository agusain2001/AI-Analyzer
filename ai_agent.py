import json
import os
import sys
from datetime import datetime
from typing import Dict
from pdf_extractor import PDFExtractor
from gemini_analyzer import GeminiAnalyzer
from config import Config

# Force UTF-8 encoding for stdout/stderr to handle checkmarks and other symbols
# This fixes the UnicodeEncodeError: 'ascii' codec can't encode character '\u2713'
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

class UniversalCreditAIAgent:
    """Main AI Agent orchestrating the analysis"""
    
    def __init__(self):
        self.config = Config()
        self.pdf_extractor = PDFExtractor(self.config.PDF_PATH)
        self.analyzer = GeminiAnalyzer(
            api_key=self.config.GEMINI_API_KEY,
            model=self.config.GEMINI_MODEL
        )
        
    def run_analysis(self) -> Dict:
        """Run complete analysis pipeline"""
        print("\n" + "="*70)
        print("NIYAMR AI - Universal Credit Act 2025 Analysis")
        print("="*70 + "\n")
        
        # Task 1: Extract Text
        print("Task 1: Extracting text from PDF...")
        extraction_result = self.pdf_extractor.extract()
        print(f" Extracted {extraction_result['length']} characters\n")
        
        # Task 2: Summarize
        print("Task 2: Generating summary...")
        summary = self.analyzer.summarize_act(extraction_result['cleaned_text'])
        print(f" Generated {len(summary)} bullet points\n")
        
        # Task 3: Extract Key Sections
        print("Task 3: Extracting key legislative sections...")
        key_sections = self.analyzer.extract_key_sections(extraction_result['cleaned_text'])
        print(f" Extracted {len(key_sections)} key sections\n")
        
        # Task 4: Rule Checks
        print("Task 4: Applying 6 rule checks...")
        rule_checks = self.analyzer.check_rules(
            extraction_result['cleaned_text'],
            key_sections
        )
        print(f" Completed {len(rule_checks)} rule checks\n")
        
        # Compile results
        results = {
            "metadata": {
                "act_title": "Universal Credit Act 2025",
                "chapter": "22",
                "analysis_date": datetime.now().isoformat(),
                "analyzer": "Gemini 2.5 Flash",
                "extracted_text_length": extraction_result['length']
            },
            "task_1_extraction": {
                "status": "completed",
                "text_length": extraction_result['length'],
                "extraction_method": "pdfplumber + PyPDF2",
                "text": extraction_result['cleaned_text']
            },
            "task_2_summary": summary,
            "task_3_key_sections": key_sections,
            "task_4_rule_checks": rule_checks
        }
        
        # Save to JSON
        self._save_json(results)
        
        print("="*70)
        print("Analysis Complete!")
        print(f"Results saved to: {self.config.OUTPUT_DIR}/{self.config.JSON_OUTPUT_FILE}")
        print("="*70 + "\n")
        
        return results
    
    def _save_json(self, results: Dict):
        """Save results to JSON file"""
        os.makedirs(self.config.OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(self.config.OUTPUT_DIR, self.config.JSON_OUTPUT_FILE)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    agent = UniversalCreditAIAgent()
    agent.run_analysis()
