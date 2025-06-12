# 레포팅 모듈
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from stock_info import Stock

load_dotenv(override=True)

api_key = os.getenv('OPENAI_API_KEY')

# gpt model 객체 생성
# llm = ChatOpenAI(model="gpt-4o", api_key=api_key, temperature=0)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key, temperature=0)

def investment_report(symbol, company):
    
    system_prompt = """
    Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely! First statement contains following content- “Can you tell us what future stock market looks like based upon current conditions ?".
    """
    user_prompt = """
        {company}에 주식을 투자해도 될까요? 마크다운 형식의 투자보고서를 한글로 작성해 주세요.
        야래의 기본 정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성해 주세요.

        기본정보:
        {basic_info}

        재무제표:
        {finacial_statement}
    """
    # 프롬프트 객체 생성
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])

    # 아웃풋 파서 객체생성
    output_parser = StrOutputParser()

        # chain 구성 : LCEL(LangChain Expression Language)
    chain = prompt | llm | output_parser

    # 회사 이름
    # company = "MicroSoft"
    # symbol = "MSFT"  # stock의 symbol 정보

    company = company
    symbol = symbol
    # 기본정보 :  basic_info
    # 재무제표: finacial_statement

    # stock 정보를 객체로 모듈화해서 불러오기
    stock = Stock(symbol)
    req_value = {
        "company":company,
        # 기본정보 :  basic_info
        "basic_info": stock.get_basic_info(),
        # 재무제표: finacial_statement
        "finacial_statement" : stock.get_financial_statement()
    }

    response = chain.invoke(req_value)

    return response

if __name__ == "__main__":
    # 회사 이름
    company = "Apple Inc"
    symbol = "AAPL"  # stock의 symbol 정보

    report = investment_report(symbol, company)
    print(report)