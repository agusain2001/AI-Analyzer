import streamlit as st
import json
import os
from ai_agent_new import UniversalCreditAIAgent
from config_new import Config

st.set_page_config(
    page_title="Universal Credit Act 2025 AI Analyzer",
    page_icon="📄",
    layout="wide"
)

def main():
    st.title("🤖 Universal Credit Act 2025 AI Analyzer")
    st.markdown("### NIYAMR AI - 48-Hour Internship Assignment")
    
    st.markdown("""
    **Objective:** AI Agent that reads, summarizes, and analyzes the Universal Credit Act 2025
    
    **Technology Stack:**
    - 🧠 LLM: Google Gemini 2.5 Flash
    - 📄 PDF Extraction: pdfplumber + PyPDF2
    - 🎨 UI: Streamlit
    """)
    
    st.divider()
    
    # Configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input("Gemini API Key", type="password", value=Config.GEMINI_API_KEY)
        
        if st.button("Update API Key"):
            os.environ["GEMINI_API_KEY"] = api_key
            st.success("API Key updated!")
        
        st.divider()
        st.markdown("**Tasks:**")
        st.markdown("""
        ✅ Task 1: Extract Text  
        ✅ Task 2: Summarize Act  
        ✅ Task 3: Extract Key Sections  
        ✅ Task 4: Apply 6 Rule Checks
        """)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📋 Analysis Controls")
        
        if st.button("🚀 Run Complete Analysis", type="primary", use_container_width=True):
            if not api_key:
                st.error("Please provide a Gemini API Key in the sidebar!")
                return
            
            with st.spinner("Running AI analysis... This may take 2-3 minutes..."):
                try:
                    # Update config with API key from sidebar if needed
                    os.environ["GEMINI_API_KEY"] = api_key
                    
                    agent = UniversalCreditAIAgent()
                    results = agent.run_analysis()
                    
                    st.success("✅ Analysis completed successfully!")
                    
                    # Store in session state
                    st.session_state['results'] = results
                    
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
                    return
    
    with col2:
        st.header("📊 Status")
        if 'results' in st.session_state:
            st.success("Analysis Complete")
            st.metric("Text Length", f"{st.session_state['results']['metadata']['extracted_text_length']:,}")
        else:
            st.info("Ready to analyze")
    
    if 'results' in st.session_state:
        results = st.session_state['results']
        
        st.divider()
        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "Metadata", "Executive Summary", "Key Sections", "Rule Checks", "JSON Report", "Extracted Text"
        ])
        
        with tab1:
            st.header("Analysis Metadata")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Document Title", results['metadata']['act_title'])
            with col2:
                st.metric("Chapter", results['metadata']['chapter'])
            with col3:
                st.metric("Analyzer", results['metadata']['analyzer'])
        
        with tab2:
            st.header("Executive Summary (Task 2)")
            for i, point in enumerate(results['task_2_summary'], 1):
                st.markdown(f"{i}. {point}")
        
        with tab3:
            st.header("Key Legislative Sections (Task 3)")
            for section, content in results['task_3_key_sections'].items():
                with st.expander(f"📌 {section.replace('_', ' ').title()}"):
                    st.write(content)
        
        with tab4:
            st.header("Rule Validation Checks (Task 4)")
            for check in results['task_4_rule_checks']:
                status_icon = "✅" if check['status'] == 'pass' else "❌"
                with st.expander(f"{status_icon} {check['rule']}"):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**Evidence:** {check['evidence']}")
                    with col2:
                        st.metric("Confidence", f"{check['confidence']}%")
        
        with tab5:
            st.header("Download JSON Report")
            st.download_button(
                label="📥 Download Complete Analysis (JSON)",
                data=json.dumps(results, indent=2),
                file_name="universal_credit_act_analysis.json",
                mime="application/json",
                use_container_width=True
            )
            
            st.code(json.dumps(results, indent=2), language="json")
            
        with tab6:
            st.header("Extracted Text (Task 1)")
            st.text_area("Raw Text Content", results['task_1_extraction'].get('text', 'Text not available'), height=600)

if __name__ == "__main__":
    main()
