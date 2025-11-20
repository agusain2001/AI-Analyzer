import json
import os
import sys
from datetime import datetime
from typing import Dict
from pdf_extractor import PDFExtractor
from gemini_analyzer import GeminiAnalyzer
from config import Config

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

class UniversalCreditAIAgent:
    def __init__(self):
        self.config = Config()
        self.pdf_extractor = PDFExtractor(self.config.PDF_PATH)
        self.analyzer = GeminiAnalyzer(api_key=self.config.GEMINI_API_KEY, model=self.config.GEMINI_MODEL)

    def run_analysis(self) -> Dict:
        print('Starting Analysis...')
        extraction = self.pdf_extractor.extract()
        print(f'Extracted {extraction['length']} chars')
        summary = self.analyzer.summarize_act(extraction['cleaned_text'])
        print('Summary generated')
        key_sections = self.analyzer.extract_key_sections(extraction['cleaned_text'])
        print('Key sections extracted')
        rule_checks = self.analyzer.check_rules(extraction['cleaned_text'], key_sections)
        print('Rules checked')
        
        results = {
            'metadata': {
                'act_title': 'Universal Credit Act 2025',
                'chapter': '22',
                'analyzer': 'Gemini 2.5 Flash',
                'extracted_text_length': extraction['length']
            },
            'task_1_extraction': {
                'text': extraction['cleaned_text'],
                'length': extraction['length']
            },
            'task_2_summary': summary,
            'task_3_key_sections': key_sections,
            'task_4_rule_checks': rule_checks
        }
        self._save_json(results)
        return results

    def _save_json(self, results: Dict):
        os.makedirs(self.config.OUTPUT_DIR, exist_ok=True)
        path = os.path.join(self.config.OUTPUT_DIR, self.config.JSON_OUTPUT_FILE)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    UniversalCreditAIAgent().run_analysis()