# langchain_pjt
langchain_pjt

# 기본 환경 셋팅
```
- 콘다 가상환경 만들고, 활성화 하기
conda create -n lc_env python=3.12
conda activate lc_env

- 작업디렉토리 이동
cd langchain_pjt
```

# 기본 설치 라이브러리
```
pip install -Uq python-dotenv
pip install -U langchain 
pip instlla -U langchain_community

- openai 
pip install -U langchain-openai 
```

# 데이터 수집 및 표현
```
- 주식 데이터
pip install yfinance

- 검색 엔진
pip install meilisearch

- 마크다운
pip install tabulate
```

- 웹 Backend, frontend 개발
pip install streamlit
```

# 실행방법
```
streamlit run main_app.py
```