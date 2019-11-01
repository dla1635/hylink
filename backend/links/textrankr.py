# -*- coding: utf-8 -*-

from re import split
from networkx import Graph
from networkx import pagerank
from itertools import combinations
from collections import Counter

import nltk
from konlpy.tag import Okt

from .sentence import Sentence

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.preprocessing import normalize
# import numpy as np



class TextRank(object):
    stopwords = [
        "이하","만약","대한","아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가",
    ]
    eng_stopwords=[
        "lot","day","way",
    ]
    def __init__(self, text):
        self.text = text.strip()
        self.build()

    def build(self):
        self._build_sentences()

        # self.has_nouns = self._extract_nouns()
        
        # 문장 처리
        self._build_graph()        
        self.pageranks = pagerank(self.graph, weight='weight')
        self.reordered = sorted(self.pageranks, key=self.pageranks.get, reverse=True)
        

        # 단어 처리
        self.word_rank_collections = Counter(self.nouns)
        #if self.has_noun:
            # self._build_word_graph()
            # word_rank_idx = self.get_word_ranks(self.words_graph)
            # self.sorted_word_rank_idx = sorted(word_rank_idx, key=lambda k: word_rank_idx[k], reverse=True)

    def _build_sentences(self):
        okt= Okt()
        dup = {}
        candidates = []
        
        #candidates = split(r'(?:(?<=[^0-9])\.|\n)', self.text)
        #전체 text를 문장단위로 split한다
        #   전체 문장 text를 \n으로 split
        #   나눈 한 line에서 .으로 split 파일명 안잘리게 정규식적용
        #   line에서 앞 뒤 공백 제거후 append     

        for enter_line in re.split('\n|! |\? ', self.text): 
            for line in split(r'[\.](?=[^0-9])(?=[^a-z])', enter_line):
                candidates.append(line.strip(' ').strip('.').strip('\t'))

        self.sentences = []
        self.nouns = []
        self.has_noun = False
        index = 0
        eng_list = []
        eng_nouns = []
        for candidate in candidates:
            if len(candidate) >= 1 and candidate not in dup:
                dup[candidate] = True
                # 문장 추가
                self.sentences.append(Sentence(candidate + '.', index))
                index += 1
                # 문장의 명사들 추가
                for pos in okt.pos(str(candidate)):
                    if pos[0] not in self.stopwords and len(pos[0]) > 1 and pos[1]=="Noun":
                        self.nouns.append(pos[0])
                    elif pos[1]=="Alpha":
                        eng_list.append(pos[0])

                # 영어 문자열 
                for pos in nltk.pos_tag(eng_list):
                    if pos[1]=="NN" and pos[0].lower() not in self.eng_stopwords and len(pos[0]) > 1:        
                        eng_nouns.append(pos[0].lower())

        if len(self.nouns) > 0:
            self.has_noun = True
        else:
            if(len(eng_nouns) > 0):
                self.nouns.extend(eng_nouns)
                self.has_noun = True


        del dup
        del candidates

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

    def _jaccard(self, sent1, sent2):
        p = sum((sent1.bow & sent2.bow).values())
        q = sum((sent1.bow | sent2.bow).values())
        return p / q if q else 0

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
        #리턴값 3개 보장
        if len(results) < word_num:    
            for i in range(len(results),word_num):
                    results.append("None")
                    i += 1

        return results

    # def _extract_nouns(self):
    #     okt = Okt()
    #     self.nouns = []
        
    #     for sentence in self.sentences:
    #         if sentence.text is not '':
    #             self.nouns.append(' '.join([noun for noun in okt.nouns(str(sentence.text))
    #             if noun not in self.stopwords and len(noun) > 1]))

    #     # noun이 하나도 안뽑혔는지 재확인
    #     # noun이 하나라도 있으면 true리턴
    #     # 하나도 없으면 false리턴
    #     for noun in self.nouns:
    #         if noun:
    #             return True
        
    #     return False

            
    # def _build_word_graph(self):
    #     #단어 그래프 처리
    #     self.tfidf = TfidfVectorizer()
    #     self.cnt_vec = CountVectorizer()
    #     cnt_vec_mat = normalize(self.cnt_vec.fit_transform(self.nouns).toarray().astype(float), axis=0)
        
    #     vocab = self.cnt_vec.vocabulary_

    #     self.words_graph = np.dot(cnt_vec_mat.T, cnt_vec_mat)
        
    #     self.idx2word = {vocab[word] : word for word in vocab}
        
    
    # def get_word_ranks(self, graph, d=0.85):
    #     A = graph
    #     matrix_size = A.shape[0]
    #     for id in range(matrix_size):
    #         A[id, id] = 0 # diagonal 부분을 0으로
    #         link_sum = np.sum(A[:,id]) # A[:, id] = A[:][id]
    #         if link_sum != 0:
    #             A[:, id] /= link_sum
    #         A[:, id] *= -d
    #         A[id, id] = 1
            
    #     B = (1-d) * np.ones((matrix_size, 1))

    #     ranks = np.linalg.solve(A, B) # 연립방정식 Ax = b

        
    #     return {idx: r[0] for idx, r in enumerate(ranks)}