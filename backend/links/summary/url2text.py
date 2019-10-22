import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request

from urllib import parse #인코딩용 임포트

from bs4 import BeautifulSoup
from textrankr import TextRank

def urlparse(url):
    img_url = ""
    title = ""
    parse_text = ""    
    #주소 형식이 아닌경우 에러 후 종료
    if "http://" not in url and "https://" not in url:
        return "url형식 오류"

    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    # print(soup)
    # 대표 이미지 추출
    img_tag = soup.find("meta",{"property":"og:image"})
    if len(img_tag)>1:
        img_url = img_tag.get("content",None)
    #타이틀 추출
    title = soup.find("title")
    
    # print(soup.find("meta",{"property":"og:image"}))
    if "naver" in url:
        # naver 관련주소 처리
        for tag in soup.find_all("meta",{"property":"nv:news:contents"}):
            # if tag.get("property", None) == "nv:news:contents":
            parse_text = parse_text+tag.get("content",None)

        if len(parse_text)<=1:
            #메타 태그 없는거
            parse_text= "none"

        
        return parse_text
        
        # meta_d = soup.find("meta",{"property":"nv:news:contents"})
        # parse_text= meta_d.get("content",None)

        
    # elif "tistory" in url:
        
    #     for line in all_p:
    #         parse_text = parse_text + line.get_text().strip() +"\n"

    return img_url, title, parse_text
    

