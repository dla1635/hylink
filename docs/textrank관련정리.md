## 3줄요약 관련정리

- backend/links/ 아래 textrankr.py, sentence.py, url2text.py 동작에 필요한 설치목록

- textrank 알고리즘 요약



> requirements

- beautifulsoup4 (v4.8.1 / 크롤링 할때 필요) pip install bs4
- networkx (v2.4 ) 키워드 뽑을때 쓴건데 Counter로 바꿔서 현재는 불필요
- pip 업데이트 (v19.3 $python -m pip install --upgrade pip) python -m pip install --upgrade pip
- Jpype 설치 ($pip install backend/links/summary/JPype1-0.6.3-cp36-cp36m-win_amd64.whl)
- konlpy (v0.5.1) pip install konlpy (한국어 처리)
- numpy (v1.17.2) pip install numpy
- requests
- nltk (영어 처리)
  - nltk import관련 오류 생길시 python 인터프리터 열고 설치하란거 설치하면됨
  - \>\>\> import nltk
  - \>\>\> nltk.download("뭐시기")



> textrank 알고리즘

각 문장을 node로 문장간 유사도를 edge로 해서 가장 중요한 문장 3개를 추출

참고 링크

textrank설명 https://bab2min.tistory.com/552 

구글 검색의 기본 알고리즘인 pagerank설명 https://sungmooncho.com/2012/08/26/pagerank/ 

textrank로 3줄요약 구현 설명 https://blog.theeluwin.kr/post/146188165713/summariz3 



키워드는 명사 빈도수 기반으로 상위 3개 추출

Bag of Words(BoW)설명  https://wikidocs.net/22650 