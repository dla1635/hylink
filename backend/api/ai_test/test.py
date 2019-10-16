import sys

import io



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



import urllib.request

from urllib import parse #인코딩용 임포트

from bs4 import BeautifulSoup
from textrankr import TextRank

url = "https://dailyoscar.tistory.com/49"

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
    print(line.get_text().strip())
    input_text+= line.get_text().strip()

# print(input_text)
print("===============    title   ============")
title = soup.find("title")
print(title.get_text().strip())

print("===============    h1     ============")
head = soup.find_all("h1")
for line in head:
    print(line.get_text().strip())
    
print("===============    h2     ============")
head = soup.find_all("h2")
for line in head:
    print(line.get_text().strip())
    
print("===============    h3     ============")
head = soup.find_all("h3")
for line in head:
    print(line.get_text().strip())

print("===============    h4     ============")
head = soup.find_all("h4")
for line in head:
    print(line.get_text().strip())
    

print("=============== summarized ============")
textrank = TextRank(input_text)
# print(textrank.summarize())  # gives you some text
# print(textrank.summarize(3, verbose=False))  # up to 3 sentences, returned as list
idx = 0
for line in textrank.summarize(3, verbose=False):
    idx+=1
    print("{} : {}".format(idx,line))
    
# print(soup)