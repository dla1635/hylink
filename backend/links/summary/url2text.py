import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request
from urllib.error import HTTPError
import requests

from urllib import parse #인코딩용 임포트
import html

headers = {'User-Agent': 'Chrome/66.0.3359.181'}

from bs4 import BeautifulSoup
from textrankr import TextRank

def urlparse(url):
    print("parsing : {}".format(url))
    img_url = "None"
    title = "None"
    parse_text = ""  
    meta_tag = [] 
    # 1. 주소의 html정보 파싱
    try:
        # if "http://" not in url and "https://" not in url:
        #     return "None","None","None"
        res = requests.get(url, headers=headers)
        # soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
        soup = BeautifulSoup(res.text,"html.parser")
    except HTTPError as e:
        # 주소에서 404 혹은 500등 에러 발생
        print(e)
        return "None","None","None","None"

    # 2. 대표 이미지가 있는 경우 대표 이미지 추출
    img_tag = soup.find("meta",{"property":"og:image"})
    if str(img_tag) != "None":
        img_url = img_tag.get("content",None)

    # 3. 타이틀 추출
    title = soup.find("title").get_text()
    
    # 4. 본문 및 태그 추출
    if "naver" in url:
        # naver 관련주소 처리
        # 네이버는 크롤링 방지가 되있어서 본문 추출 어려움으로 meta태그에서 최대한 뽑음
        for tag in soup.find_all("meta",{"property":"nv:news:contents"}):
            tag_text = html.unescape(tag.get("content",None).strip()) +"\n" #html unescape문자 처리
            parse_text += tag_text 
        if len(parse_text)<=1:
            #메타 태그에 본문 없는거
            parse_text= "None"

        # print("after parsing naver :\n img_url : {}\n title : {}\n parse_text : {}".format(img_url,title,parse_text))
        return img_url, title, parse_text, meta_tag
        
    if "tistory" in url:
        all_p = soup.find_all("p")
        for line in all_p:
            parse_text += line.get_text().strip() +"\n"

        return img_url, title, parse_text,meta_tag

    if "youtube" in url:
        parse_text="None"
        for tag in soup.find_all("meta",{"property":"og:video:tag"}):
            tag_text = html.unescape(tag.get("content",None).strip()) #html unescape문자 처리
            meta_tag.append(tag_text)
        return img_url, title, parse_text, meta_tag
    
    if "stackoverflow" in url:
        for main_text in soup.find(class_="post-layout").find_all("p"):
            parse_text += main_text.get_text() #html unescape문자 처리
            
        return img_url, title, parse_text, meta_tag
   
   
    #나머지 주소들
    all_p = soup.find_all("p")
    for line in all_p:
        parse_text += line.get_text().strip() +"\n"

    # print("return",img_url,title,parse_text)
    return img_url, title, parse_text, meta_tag
    

