
#crawling naver cafe data
import dryscrape
import sys
import urllib.request
from bs4 import BeautifulSoup
import os

def get_list():
	#url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query="+ keyword +"&search.searchBy=0&search.sortBy=date&search.clubid=11262350&search.option=0&search.defaultValue=&search.page=1" 
	url = "https://m.cafe.naver.com/ArticleSearchListAjax.nhn?search.query=%EA%B0%80%EB%A1%9C%EC%88%98%EA%B8%B8%EB%A7%9B%EC%A7%91&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=11262350&search.option=0&search.defaultValue=&search.page=2"
	#str(page)
	type(url)
	req = urllib.request.Request(url)
	html = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(html, 'html.parser')
	return soup.select("a")

def get_link(dom) : 
    ls = []
    for i in range(0, len(dom)) :
        link = dom[i].get('href')
        if len(link) > 2 and "Comment" not in link and "javascript" not in link :
            link = "http://m.cafe.naver.com"+link
            ls.append(link)
    return ls

def goint_page(link) :
    headers = {
        "Referer"  : "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%EA%B0%80%EB%A1%9C%EC%88%98%EA%B8%B8%EB%A7%9B%EC%A7%91&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=11262350&search.option=0&search.defaultValue=1",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    }
    # req = urllib.request.Request(link, headers = headers)
    # #response = requests.get(link, headers = headers)
    # html = urllib.request.urlopen(req).read()
    session = dryscrape.Session()
    session.visit(link)
    response = session.body()
    soup = BeautifulSoup(html, "html.parser")
    text = soup.select_one("#postContent").text
    return text
#hangul = hangul.decode("가로수길").encode('utf-8')
# s = "가로수길"
# s3 = s.encode('cp949')
# s3 = str(s3)
#print(s.encode('utf-8'))
check = get_list()
ls = get_link(check)
text = goint_page(ls[0])

print(text)