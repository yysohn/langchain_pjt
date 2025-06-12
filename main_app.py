import streamlit as st
from report_service import investment_report
# from search_index import SearchResult, search_compay
from search_index import SearchResult, search_company
from stock_info import Stock

st.title("AI 투자 보고서 생성 서비스")
search_symbol = st.text_input("회사 심볼")
company_list = search_company(search_symbol)
hits = company_list['hits']
result = [SearchResult(hit) for hit in hits]

company_selected = st.selectbox("회사 선택", result, index=0)

search_symbol = company_selected.symbol
company_selected = company_selected.name

tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식거래량 차트로 시각화
with tab1:
    st.header(f"{company_selected} 주식거래량")
    stock = Stock(search_symbol)
    # stock = Stock(company_selected.symbol)
    volume = stock.get_stock_volume()
    st.line_chart(volume, use_container_width=True)

# LLM이 만든 투자 보고서 출력
with tab2:
    st.header(f"{company_selected} AI투자보고서")

    if st.button("투자 보고서 생성"):
        with st.spinner(text="투자 보고서 생성 중..."):
            report = investment_report(search_symbol, company_selected)
            st.success("투자 보고서 생성 완료!")            
        st.write(report)