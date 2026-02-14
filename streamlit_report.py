import streamlit as st
from pathlib import Path

ROOT = Path(__file__).parent
MD_PATH = ROOT / "Comprehensive_Full_Report.md"

st.set_page_config(page_title="명절 선물 데이터 리포트", layout="wide")

def load_markdown(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "# Report not found\nPlease ensure Comprehensive_Full_Report.md exists in workspace."

md_text = load_markdown(MD_PATH)

st.title("명절 선물 데이터 종합 리포트 (2024–2025)")

section = st.sidebar.selectbox("섹션 선택", ["Full Report", "Images", "원본 마크다운 다운로드"])

if section == "Full Report":
    st.markdown(md_text, unsafe_allow_html=True)

elif section == "Images":
    st.header("Included Visualizations")
    images = [
        "시각화_1_선그래프.png",
        "시각화_2_막대그래프.png",
        "시각화_3_히트맵.png",
        "3_trend_vs_clicks_scatter.png",
        "11_moving_average.png",
        "12_bollinger_bands.png",
        "comparison_스팸세트.png",
        "comparison_한우세트.png",
        "comparison_홍삼세트.png",
    ]
    cols = st.columns(2)
    for i, img in enumerate(images):
        p = ROOT / img
        with cols[i % 2]:
            if p.exists():
                st.image(str(p), caption=img)
            else:
                st.info(f"Image not found: {img}")

else:
    st.header("원본 마크다운 다운로드")
    st.download_button("마크다운 파일 다운로드", data=md_text, file_name="Comprehensive_Full_Report.md", mime="text/markdown")

st.sidebar.markdown("---")
st.sidebar.markdown("`streamlit run streamlit_report.py` 로 앱 실행")
