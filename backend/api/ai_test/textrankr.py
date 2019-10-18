# -*- coding: utf-8 -*-

from re import split
from networkx import Graph
from networkx import pagerank
from itertools import combinations
from sentence import Sentence


class TextRank(object):

    def __init__(self, text):
        self.text = text.strip()
        self.build()

    def build(self):
        self._build_sentences()
        self._build_graph()
        self.pageranks = pagerank(self.graph, weight='weight')
        self.reordered = sorted(self.pageranks, key=self.pageranks.get, reverse=True)

    def _build_sentences(self):
        dup = {}
        # 0.1같은 실수형식이랑 .txt같은 파일형식 안잘리게 정규식으로 split
        # 풀어쓰면 아래 주석과 같은 기능
        # candidates = split(r'(?<=[^0-9])(?<=[^a-z])[\.|\n]', self.text)
        candidates = []
        enters_split = split('\n', self.text)
        for enter_one in enters_split:
            dots_split = split(r'(?<=[^0-9])(?<=[^a-z])[\.]', enter_one)
            for dot_one in dots_split:
                candidates.append(dot_one)

        self.sentences = []
        index = 0
        for candidate in candidates:
            candidate = candidate.strip(' ').strip('.').strip('\t')
            
            if len(candidate) >= 1 and candidate not in dup:
                dup[candidate] = True
                self.sentences.append(Sentence(candidate + '.', index))
                index += 1
            
        del dup
        del candidates

    def _build_graph(self):
        self.graph = Graph()
        self.graph.add_nodes_from(self.sentences)
        for sent1, sent2 in combinations(self.sentences, 2):
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
        if verbose:
            return '\n'.join(results)
        else:
            return results
