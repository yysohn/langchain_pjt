import yfinance as yf
import pandas as pd

class Stock:
    # 생성자 : 기본값 설정
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
    # 회사 기본 정보
    def get_basic_info(self):
        basic_info = pd.DataFrame.from_dict(
            self.ticker.info,
            orient='index',
            columns=['Value']
        )
        basic_info = basic_info.loc[['longName', 'marketCap', 'industry', 'sector', 'fullTimeEmployees', 'currentPrice', 'enterpriseValue']]
        return basic_info

    # 재무재포 수집
    def get_financial_statement(self):
        
        # 손익계산서
        income_stmt = self.ticker.income_stmt.loc[['Total Revenue', 'Gross Profit','Operating Income', 'Net Income']].iloc[:, :4].to_markdown()
        # 대차대조표를 마크다운 형식으로 변환
        balance_sheet = self.ticker.balance_sheet.loc[['Total Assets', 
                                                       'Total Liabilities Net Minority Interest',
                                                       'Stockholders Equity']].iloc[:, :4].to_markdown()
        # 현금 흐름표를 마크다운 형식으로 변환
        cash_flow = self.ticker.cashflow.loc[['Operating Cash Flow', 
                                              'Investing Cash Flow',
                                              'Financing Cash Flow']].iloc[:, :4].to_markdown() 
        financial_state = f"""
        # 손익계산서
        {income_stmt} 
        # 대차대조표
        {balance_sheet} 
        # 현금흐름표
        {cash_flow} 
        """
        print(financial_state)
        return financial_state

    # 주식거래량
    def get_stock_volume(self):
        # 최근 3개월간의 거래량을 가져옴
        volume_data = self.ticker.history(period='6mo')['Volume']
        volume_data_desc = volume_data.sort_index(ascending=False)
        # print(volume_data_desc)   
        return volume_data_desc
    
if __name__ == "__main__":
    # 회사 이름
    company_name = "AAPL"
    # Stock 객체 생성
    stock = Stock(company_name)
    print("회사심볼", stock.symbol)
    print("회사티커", stock.ticker)
    print(stock.get_basic_info())
    print(stock.get_financial_statement())
    print(stock.get_stock_volume())
