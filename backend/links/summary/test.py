import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request

from urllib import parse #인코딩용 임포트

from bs4 import BeautifulSoup
from textrankr import TextRank

url =""

url = input("url을 입력하세요(http://혹은 https://로 시작하는 주소) :")
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
# print("origin html text")
# print(soup)
# print("======= all tag ==========")
# all_div = soup.find_all("div")

# input_text = ""
# for line in all_div:
#     print(line.get_text().strip())
#     input_text+= line.get_text().strip()


all_p = soup.find_all("p",class_="")
# print("======= all p ==========")
# for line in all_p:
#     print(line.get_text().strip() +"\n")

input_text = ""
for line in all_p:
    input_text = input_text + line.get_text().strip() +"\n"

textrank = TextRank(input_text)
# print(textrank.summarize())  # gives you some text
# print(textrank.summarize(3, verbose=False))  # up to 3 sentences, returned as list
print("===============    title   ============")
title = soup.find("title")
print(title.get_text().strip())
print("=============== summarized ============")
sentences = textrank.summarize(3, verbose=False)
print("1 : {}".format(sentences[0]))
print("2 : {}".format(sentences[1]))
print("3 : {}".format(sentences[2]))
print("=============== keywords ==============")
keywords = textrank.keywords(3)
print("{} , {} , {}".format(keywords[0],keywords[1],keywords[2]))
