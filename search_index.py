import meilisearch as ms

client = ms.Client('http://localhost:7700', 'aSampleMasterKey')

# 서치하기
def search_company(symbol):
    # nasdaq : index 이름
    return client.index('nasdaq').search(symbol)

# 자료 서칭을 위한 클래스
class SearchResult():
    # 객체 생성자, 클래스를 객체화 할때 무조건 실행
    def __init__(self, item):
        self.item = item
    # 심볼값 가져오기
    # @property : 파이썬 데코레이터
    @property
    def symbol(self):
        return self.item['Symbol']
    @property
    def name(self):
        return self.item['Name']

    # print() 또는 str()문을 만났을 때 출력형태
    def __str__(self):
        # return f"AAPL: Apple Inc"
        return f"{self.symbol}: {self.name}"

if __name__ == "__main__":
    # 서치 키워드
    # symbol = "AAPL"
    symbol = "Apple"
    company_info = search_company(symbol)
    # print(company_info)
    # print(company_info['hits'])
    hits = company_info['hits']
    # print(hits)
    # result = []
    # for hit in hits:
    #     print(SearchResult(hit))
    #     print("-" * 20)
    #     result.append(SearchResult(hit))
    # 리스트 컴프리렌션으로 변경
    result = [SearchResult(hit) for hit in hits]
    print(result[0].name)
    print(result[0].symbol)

    # print(result)
    # company_symbol = company_info['hits'][0]['Symbol']
    # company_name = company_info['hits'][0]['Name']
    # company_sector = company_info['hits'][0]['Sector']
    # company_industry = company_info['hits'][0]['Industry']
    # company_mkcap = company_info['hits'][0]['Market Cap']
    # print(f"{company_symbol} : {company_name}")
    # 섹터, 인더스트리, Market Cap
    # print(f"Sector : {company_sector}")
    # print(f"Industry : {company_industry}")
    # print(f"Market Cap : {company_mkcap}")
