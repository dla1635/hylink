# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request

from urllib import parse #인코딩용 임포트


from re import split
from networkx import Graph
from networkx import pagerank
from itertools import combinations
from summary.sentence import Sentence

from konlpy.tag import Okt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np

from collections import Counter


class TextRank(object):
    stopwords = ["만약","대한","아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가",]
    
    def __init__(self, text):
        self.text = text.strip()
        self.build()

    def build(self):
        self._build_sentences()

        # self.test_word()
        #self.has_nouns = self._extract_nouns()
        
        # 문장 처리
        self._build_graph()        
        self.pageranks = pagerank(self.graph, weight='weight')
        self.reordered = sorted(self.pageranks, key=self.pageranks.get, reverse=True)
        

        # 단어 처리
        if self.has_noun:
            self.word_rank_collections = Counter(self.nouns)
            # self._build_word_graph()
            # word_rank_idx = self.get_word_ranks(self.words_graph)
            # self.sorted_word_rank_idx = sorted(word_rank_idx, key=lambda k: word_rank_idx[k], reverse=True)


    def test_word(self):
        
        okt = Okt()
        word2index={}  
        bow=[]  
        for sentence in self.sentences:
            token = okt.nouns(sentence.text)
            for voca in token:  
                    if voca not in word2index.keys():  
                        word2index[voca]=len(word2index)  
            # token을 읽으면서, word2index에 없는 (not in) 단어는 새로 추가하고, 이미 있는 단어는 넘깁니다.   
                        bow.insert(len(word2index)-1,1)
            # BoW 전체에 전부 기본값 1을 넣어줍니다. 단어의 개수는 최소 1개 이상이기 때문입니다.  
                    else:
                        index=word2index.get(voca)
            # 재등장하는 단어의 인덱스를 받아옵니다.
                        bow[index]=bow[index]+1
            # 재등장한 단어는 해당하는 인덱스의 위치에 1을 더해줍니다. (단어의 개수를 세는 것입니다.)  
        

    def _build_sentences(self):
        okt= Okt()
        dup = {}
        candidates = []
        
        #candidates = split(r'(?:(?<=[^0-9])\.|\n)', self.text)
        #전체 text를 문장단위로 split한다
        #   전체 문장 text를 \n으로 split
        #   나눈 한 line에서 .으로 split 파일명 안잘리게 정규식적용
        #   line에서 앞 뒤 공백 제거후 append        
        for enter_line in split('\n', self.text): 
            for line in split(r'(?<=[^0-9])(?<=[^a-z])[\.]', enter_line):
                candidates.append(line.strip(' ').strip('.').strip('\t'))

        self.sentences = []
        self.nouns = []
        self.has_noun = False
        index = 0

        for candidate in candidates:
            if len(candidate) >= 1 and candidate not in dup:
                dup[candidate] = True
                # 문장 추가
                self.sentences.append(Sentence(candidate + '.', index))
                index += 1
                # 문장의 명사들 추가
                for noun in okt.nouns(str(candidate)):
                    if noun not in self.stopwords and len(noun) > 1:
                        self.nouns.append(noun)
        if len(self.nouns) > 0:
            self.has_noun = True
                
        del dup
        del candidates

    def _extract_nouns(self):
        okt = Okt()
        self.nouns = []
        
        for sentence in self.sentences:
            if sentence.text is not '':
                self.nouns.append(' '.join([noun for noun in okt.nouns(str(sentence.text))
                if noun not in self.stopwords and len(noun) > 1]))

        # noun이 하나도 안뽑혔는지 재확인
        # noun이 하나라도 있으면 true리턴
        # 하나도 없으면 false리턴
        for noun in self.nouns:
            if noun:
                return True
        
        return False


    def _build_graph(self):
        
        #문장 그래프 처리
        self.graph = Graph()
        self.graph.add_nodes_from(self.sentences)
        #문장간의 모든 경우에서 유사도 탐색
        for sent1, sent2 in combinations(self.sentences, 2):
            # print(sent1,sent2)
            weight = self._jaccard(sent1, sent2)
            if weight:
                self.graph.add_edge(sent1, sent2, weight=weight)
        
    def _build_word_graph(self):
        #단어 그래프 처리
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(self.nouns).toarray().astype(float), axis=0)
        
        vocab = self.cnt_vec.vocabulary_

        self.words_graph = np.dot(cnt_vec_mat.T, cnt_vec_mat)
        
        self.idx2word = {vocab[word] : word for word in vocab}
        

    def _jaccard(self, sent1, sent2):
        p = sum((sent1.bow & sent2.bow).values())
        q = sum((sent1.bow | sent2.bow).values())
        return p / q if q else 0

    def get_word_ranks(self, graph, d=0.85):
        A = graph
        matrix_size = A.shape[0]
        for id in range(matrix_size):
            A[id, id] = 0 # diagonal 부분을 0으로
            link_sum = np.sum(A[:,id]) # A[:, id] = A[:][id]
            if link_sum != 0:
                A[:, id] /= link_sum
            A[:, id] *= -d
            A[id, id] = 1
            
        B = (1-d) * np.ones((matrix_size, 1))

        ranks = np.linalg.solve(A, B) # 연립방정식 Ax = b

        
        return {idx: r[0] for idx, r in enumerate(ranks)}


    def summarize(self, count=3, verbose=True):
        results = sorted(self.reordered[:count], key=lambda sentence: sentence.index)
        results = [result.text for result in results]
    
        if verbose:
            return '\n'.join(results)
        else:
            return results

    def keywords(self, word_num=3):
        keywords = []
        # if self.has_nouns == False:
        #     return "None"

        # for idx in self.sorted_word_rank_idx[:word_num]:
        #         keywords.append(self.idx2word[idx])
        keywords = self.word_rank_collections.most_common(word_num)
       
        return keywords

if __name__ == "__main__":
    input_text = '''외계 행성(外界行星) 또는 계외 행성(系外行星)은 태양계 밖의 행성으로, 태양이 아닌 다른 항성 주위를 공전하고 있는 행성이다. 지금까지 3800여 개의 외계 행성이 발견되었으며(2018년 6월 23일 기준: 행성계 2840개에서 행성 3796개. 이 중 다중행성계는 632개) 모두 우리 은하 내에 있다.[1] 우리 은하에만 수십억 개의 행성이 존재하는 것으로 추측되며[2][3][4] 대부분 항성을 돌고 있으나 일부는 홀로 우주 공간을 움직이는 떠돌이 행성이기도 하다.[5] 발견된 외계 행성들 중 지구와 가장 비슷한 것은 프록시마 b이다.

수 세기에 걸쳐 많은 철학자와 과학자들은 외계 행성이 있으리라고 추측해 왔으나 이들이 얼마나 흔하게 있는지 또는 우리 태양계와 외계 행성계가 얼마나 비슷한지 알 방법이 없었다. 19세기부터 외계 행성을 찾았다는 발표가 여러 번 있었으나 천문학자들의 검증 결과 이 모든 주장들은 기각되었다. 1992년 펄서 PSR B1257+12 주위를 도는 암석 행성들의 존재가 최초로 검증, 발표되었다. 주계열성을 도는 행성 중 최초로 확인된 행성은 페가수스자리 51을 4일에 한 바퀴 도는 가스 행성 페가수스자리 51 b이다. 관측 기술의 향상 덕분에 이후 외계 행성의 발견 속도는 상승했다. 몇몇 외계 행성은 망원경으로 직접 사진을 찍었으나 대다수는 시선 속도와 같은 간접적인 방법으로 발견되었다.[1]

확인된 외계 행성 대부분은 목성 또는 해왕성 정도 덩치의 가스 행성으로 추측되나 가스 행성이 외계 행성들 중 대부분을 차지한다는 의미는 아니다. 단지 무거운 행성들은 쉽게 눈에 띄기 때문이며 선택 편향의 결과이다.[6] 상대적으로 가벼운 지구질량 수 배 정도의 외계 행성들도 많이 발견되었으며 통계적 연구결과 이들 암석형 외계 행성의 수는 가스 행성보다 많은 것으로 보인다.[7] 최근 지구와 비슷하거나 작은 질량의 행성들도 발견되고 있으며 이들 중 일부는 질량 외의 여러 속성이 지구와 비슷한 것도 있다.[8][9][10] 갈색 왜성을 도는 외계 행성들도 있으며 어떤 항성에도 속박되지 않고 우주를 떠도는 행성도 있다. 그러나 이런 특수한 상황에서 천체들에 '행성' 명칭이 항상 적용되는 것은 아니다.

일부 행성은 생명체 거주가능 영역 내를 돌고 있어 표면에 액체 물(또는 생명체)이 존재 가능할 것으로 보이며, 이런 행성들의 발견으로 외계 생명체의 존재 여부에 대한 관심은 증폭되고 있다.[11] 외계 행성이 생명체를 품기에 적합한지의 폭넓은 요소들을 고려하는 것을 행성 거주 가능성 연구라고 하며 이는 외계 행성 탐사에 포함된다.
'''
    textrank = TextRank(input_text)

    print("=============== summarized ============")
    sentences = textrank.summarize(3, verbose=False)
    idx = 1
    print("type : {}".format(type(sentences)))
    for sentence in sentences:
        print("{} : {}".format(idx,sentences[idx-1]))
        idx+=1

    max_keyword = 3
    print("=============== keywords ==============")
    keywords = textrank.keywords(max_keyword)
    idx = 1
    print("type : {}".format(type(keywords)))
    for keyword in keywords:
        print("{}".format(keywords[idx-1][0]))
        idx+=1