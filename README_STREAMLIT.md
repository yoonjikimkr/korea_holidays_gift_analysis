# Run the Streamlit report

This file explains how to run the Streamlit report included in this repository.

Prerequisites
- Python 3.8+ installed

Install dependencies
```bash
pip install -r requirements.txt
```

Run the app
```bash
streamlit run streamlit_report.py
```

Notes
- The app reads `Comprehensive_Full_Report.md` and expects visualization images (e.g., `시각화_1_선그래프.png`) to be present in the repository root. If images are missing, the app shows a placeholder message.
- To export a PDF or HTML, use the generated `Comprehensive_Full_Report.html` or a browser print-to-PDF of the Streamlit page.
