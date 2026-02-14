import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="2024-2025 명절 선물 트렌드",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE ---
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
            color: #e2e8f0;
        }
        .stApp {
            background-color: #0f172a;
        }
        h1, h2, h3 {
            color: #ffffff !important;
        }
        div[data-testid="stMetricValue"] {
            color: #f472b6;
        }
        .css-1d391kg {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- DATA (Translated from constants.ts) ---

# 1. Rank
rank_df = pd.DataFrame([
    {'name': '1. 현금/상품권', 'value': 35, 'color': '#cbd5e1'},
    {'name': '2. 햄/통조림(스팸)', 'value': 28, 'color': '#f43f5e'},
    {'name': '3. 정육(한우)', 'value': 18, 'color': '#f472b6'},
    {'name': '4. 건강식품(홍삼)', 'value': 12, 'color': '#fbbf24'},
    {'name': '5. 과일', 'value': 7, 'color': '#94a3b8'},
])

# 2. Timing
timing_df = pd.DataFrame({
    'date': ['D-30', 'D-20', 'D-14', 'D-7', 'D-5', 'D-3', 'D-1'],
    '한우': [15, 25, 40, 85, 60, 30, 10],
    '스팸': [5, 10, 20, 50, 80, 95, 60],
    '홍삼': [20, 30, 45, 60, 50, 40, 20]
})

# 3. Age
age_df = pd.DataFrame({
    'subject': ['20대', '30대', '40대', '50대+'],
    '스팸': [85, 70, 40, 20],
    '한우': [20, 50, 80, 70],
    '홍삼': [30, 40, 60, 90]
})

# 4. Gender
gender_df = pd.DataFrame({
    'Item': ['스팸', '한우', '홍삼'],
    '남성': [60, 45, 52],
    '여성': [40, 55, 48]
})

# 6. YoY
yoy_df = pd.DataFrame([
    {'name': '스팸', '2024': 100, '2025': 115, 'growth': '+15%'},
    {'name': '한우', '2024': 100, '2025': 95, 'growth': '-5%'},
    {'name': '홍삼', '2024': 100, '2025': 102, 'growth': '+2%'}
])

# 7. Channel
channel_df = pd.DataFrame([
    {'name': '온라인', 'value': 55},
    {'name': '대형마트', 'value': 25},
    {'name': '백화점', 'value': 15},
    {'name': '편의점', 'value': 5},
])

# 8. Region
region_df = pd.DataFrame({
    'region': ['서울/경기', '경상권', '전라권', '충청/강원'],
    '스팸': [40, 30, 20, 10],
    '한우': [55, 25, 15, 5]
})

# 9. Price
price_df = pd.DataFrame([
    {'price': '3만원 미만', 'share': 45},
    {'price': '3~5만원', 'share': 25},
    {'price': '5~10만원', 'share': 20},
    {'price': '10만원+', 'share': 10},
])

# 10. Recipient
recipient_df = pd.DataFrame([
    {'target': '부모님', 'value': 40},
    {'target': '지인/회사', 'value': 35},
    {'target': '자녀/조카', 'value': 15},
    {'target': '본인', 'value': 10},
])

# 11. Sentiment
sentiment_df = pd.DataFrame({
    'week': ['W1', 'W2', 'W3', 'W4'],
    'positive': [60, 65, 70, 55],
    'negative': [10, 15, 20, 35]
})

# 12. Bundle
bundle_df = pd.DataFrame({
    'name': ['스팸', '한우', '홍삼'],
    'single': [20, 70, 40],
    'set': [80, 30, 60]
})


# --- SIDEBAR NAV ---
st.sidebar.title("📑 분석 목차")
page = st.sidebar.radio("Go to", [
    "1. 개요 (Intro)", 
    "2. 순위 검증 (Rank)", 
    "3. 시기 분석 (Timing)", 
    "4. 타겟 분석 (Target)", 
    "5. 성장률 (YoY)",
    "6. 채널 & 지역 (Channel)",
    "7. 가격 & 대상 (Price)",
    "8. 감성 & 구성 (Sentiment)"
])

st.sidebar.markdown("---")
st.sidebar.caption("Data Source: Naver Open API")
st.sidebar.caption("Dev: Streamlit & Plotly")

# --- COLORS ---
COLOR_MAP = {'한우': '#f472b6', '스팸': '#f43f5e', '홍삼': '#fbbf24', '남성': '#60a5fa', '여성': '#f472b6'}
DARK_TEMPLATE = "plotly_dark"

# --- MAIN CONTENT ---

if "1. 개요" in page:
    st.title("🎁 2024-2025 명절 선물 트렌드")
    st.subheader("스팸 vs 한우 vs 홍삼 대격돌")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("스팸 (Spam)", "+15% 성장", "불황형 소비")
    col2.metric("한우 (Hanwoo)", "-5% 하락", "가격 저항")
    col3.metric("홍삼 (Ginseng)", "+2% 보합", "고정 수요")

    st.markdown("### 📊 분석 요약")
    st.info("""
    본 대시보드는 **12개의 인터랙티브 차트**와 **11개의 상세 데이터 테이블**을 통해 
    명절 선물 시장의 주요 키워드 3종을 심층 분석합니다.
    """)
    
    st.markdown("#### 가설 검증 결과")
    ver_df = pd.DataFrame([
        {'가설': 'H1. 상위 1-3위 진입', '결과': '✅ 검증됨', '내용': '스팸(1위), 한우(2위)'},
        {'가설': 'H2. 구매 시점 차이', '결과': '✅ 검증됨', '내용': '한우 D-7, 스팸 D-3'},
        {'가설': 'H3. 타겟 차별성', '결과': '✅ 검증됨', '내용': '세대별/성별 타겟 명확'},
    ])
    st.table(ver_df)


elif "2. 순위" in page:
    st.title("🏆 카테고리별 점유율 (Rank)")
    st.write("현금/상품권을 제외한 실물 선물 중 스팸이 1위를 차지했습니다.")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(rank_df, x='value', y='name', orientation='h', 
                     text='value', color='name', 
                     color_discrete_sequence=rank_df['color'].tolist())
        fig.update_layout(template=DARK_TEMPLATE, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 💡 Insight")
        st.success("스팸(28%)은 가장 대중적인 선택지이며, 한우와 홍삼은 프리미엄 수요를 담당합니다.")
        st.markdown("#### 📝 Raw Data")
        st.dataframe(rank_df[['name', 'value']], hide_index=True)


elif "3. 시기" in page:
    st.title("📅 구매 시점 분석 (Timing)")
    st.write("신선식품(한우)은 배송 마감 전, 가공식품(스팸)은 임박해서 구매합니다.")

    tab1, tab2 = st.tabs(["📈 트렌드 차트", "🔢 데이터 테이블"])
    
    with tab1:
        fig = px.line(timing_df, x='date', y=['한우', '스팸', '홍삼'], markers=True,
                      color_discrete_map=COLOR_MAP)
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.dataframe(timing_df, use_container_width=True)


elif "4. 타겟" in page:
    st.title("👥 인구통계학적 분석")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("연령별 선호도")
        # Plotly Radar Chart
        categories = ['20대', '30대', '40대', '50대+']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=age_df['스팸'], theta=categories, fill='toself', name='스팸', line_color='#f43f5e'))
        fig.add_trace(go.Scatterpolar(r=age_df['한우'], theta=categories, fill='toself', name='한우', line_color='#f472b6'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("성별 구매 비중")
        fig = px.bar(gender_df, x='Item', y=['남성', '여성'], barmode='stack',
                     color_discrete_map=COLOR_MAP)
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔍 연관 키워드 분석")
    st.table(pd.DataFrame([
        {'품목': '스팸', '키워드': '가성비, 자취생, 회사선물'},
        {'품목': '한우', '키워드': '부모님, 프리미엄, 시댁'},
        {'품목': '홍삼', '키워드': '건강, 면역력, 효도'},
    ]))


elif "5. 성장률" in page:
    st.title("📈 전년 대비 성장률 (YoY)")
    
    fig = px.bar(yoy_df, x='name', y='2025', text='growth',
                 color='name', color_discrete_map=COLOR_MAP)
    fig.add_hline(y=100, line_dash="dot", line_color="white", annotation_text="2024년 기준(100)")
    fig.update_layout(template=DARK_TEMPLATE, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("스팸은 +15%로 급성장한 반면, 한우는 -5%로 유일하게 역성장했습니다.")


elif "6. 채널 & 지역" in page:
    st.title("🛒 판매 채널 및 지역 분석")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("채널별 점유율")
        fig = px.pie(channel_df, values='value', names='name', hole=0.4)
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("**채널별 성장률**")
        st.dataframe(pd.DataFrame([
            {'채널': '온라인', '성장': '+22%'},
            {'채널': '편의점', '성장': '+45%'},
            {'채널': '백화점', '성장': '-3%'}
        ]), use_container_width=True)

    with col2:
        st.subheader("지역별 관심도")
        fig = px.bar(region_df, x='region', y=['스팸', '한우'], barmode='group',
                     color_discrete_map=COLOR_MAP)
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("**지역별 지수**")
        st.dataframe(pd.DataFrame([
            {'지역': '서울/경기', '특징': '한우 강세'},
            {'지역': '지방권', '특징': '스팸 강세'}
        ]), use_container_width=True)


elif "7. 가격 & 대상" in page:
    st.title("💰 가격대 및 선물 대상")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("가격대별 비중")
        fig = px.area(price_df, x='price', y='share', markers=True)
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("선물 대상")
        fig = px.bar(recipient_df, x='target', y='value', color='target')
        fig.update_layout(template=DARK_TEMPLATE, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("💵 가격대별 추천 상품 및 전환율")
    st.table(pd.DataFrame([
        {'가격': '3만원 미만', '상품': '스팸 8호', '전환율': 'High'},
        {'가격': '3~5만원', '상품': '홍삼 스틱', '전환율': 'Mid'},
        {'가격': '10만원+', '상품': '한우 세트', '전환율': 'Low'},
    ]))


elif "8. 감성 & 구성" in page:
    st.title("💖 감성 분석 및 상품 구성")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("주차별 감성 추이")
        fig = px.line(sentiment_df, x='week', y=['positive', 'negative'], markers=True,
                      color_discrete_map={'positive': '#34d399', 'negative': '#f87171'})
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("W3부터 배송 지연 및 가격 관련 부정 여론 상승")

    with col2:
        st.subheader("단품 vs 세트 선호도")
        fig = px.bar(bundle_df, x='name', y=['single', 'set'], barmode='stack')
        fig.update_layout(template=DARK_TEMPLATE)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("스팸은 세트 구성이 80%로 압도적입니다.")

    st.markdown("### 📋 심층 데이터")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**기기별 트래픽**")
        st.dataframe(pd.DataFrame([{'Device': 'Mobile', 'Rate': '72%'}, {'Device': 'PC', 'Rate': '28%'}]), use_container_width=True)
    with col_b:
        st.markdown("**시간대별 구매**")
        st.dataframe(pd.DataFrame([{'Time': '09-12 (Office)', 'Rate': 'High'}, {'Time': '19-23 (Home)', 'Rate': 'Peak'}]), use_container_width=True)

