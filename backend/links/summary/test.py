import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request

from urllib import parse #인코딩용 임포트

from bs4 import BeautifulSoup
from textrankr import TextRank

url = "https://ellun.tistory.com/46"

soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
print("origin html text")
# print(soup)
# print("======= all tag ==========")
# all_div = soup.find_all("div")

# input_text = ""
# for line in all_div:
#     print(line.get_text().strip())
#     input_text+= line.get_text().strip()

print("======= all p tag ==========")
all_p = soup.find_all("p",class_="")

input_text = ""
for line in all_p:
    input_text = input_text+line.get_text().strip() +"\n"

textrank = TextRank(input_text)
# print(textrank.summarize())  # gives you some text
# print(textrank.summarize(3, verbose=False))  # up to 3 sentences, returned as list
idx = 0
print("===============    title   ============")
title = soup.find("title")
print(title.get_text().strip())
print("=============== summarized ============")
for line in textrank.summarize(3, verbose=False):
    idx+=1
    print("{} : {}".format(idx,line))
    
# print(soup)