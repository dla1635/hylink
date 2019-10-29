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
        if len(results) < count:
            for i in range(len(results),count):
                results.append("None")
                i += 1
        
        if verbose:
            return '\n'.join(results)
        else:
            return results

    def keywords(self, word_num=3):
        keywords = []
        
        keywords = self.word_rank_collections.most_common(word_num)
        results = []
        for keyword in keywords:
            results.append(keyword[0])
        if len(results) < word_num:    
            for i in range(len(results),word_num):
                    results.append("None")
                    i += 1

        return results

if __name__ == "__main__":
    input_text = ''''''
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