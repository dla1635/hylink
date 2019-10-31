# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# import urllib.request

# from urllib import parse #인코딩용 임포트

# from bs4 import BeautifulSoup
# from textrankr import TextRank
# from url2text import urlparse

# max_keyword = 3

# url ="https://ko.wikipedia.org/wiki/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
# img_url, title, input_text, meta_tag = urlparse(url)

# print("=============== title      ============")
# print("type: {}, value: {}".format(type(title),title))
# print("=============== img-url    ============")
# print("type: {}, value: {}".format(type(img_url),img_url))

# if input_text=="None":
#     #택스트 없으면 종료
#     print("추출된 텍스트 없음!")
#     print(title)
#     print(img_url)
#     idx = 0
#     for keyword in meta_tag[:max_keyword]:
#         print("{}".format(meta_tag[idx]))
#         idx+=1
#     sys.exit(1)


# textrank = TextRank(input_text)
# print("=============== summarized ============")
# sentences = textrank.summarize(3, verbose=False)
# idx = 1
# print("type : {}".format(type(sentences)))
# for sentence in sentences:
#     print("{} : {}".format(idx,sentences[idx-1]))
#     idx+=1

# print("=============== keywords ==============")
# keywords = textrank.keywords(3)
# idx = 1
# print("type : {}".format(type(keywords)))
# for keyword in keywords:
#     print("{}".format(keywords[idx-1]))
#     idx+=1
