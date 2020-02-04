from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

driver = webdriver.Chrome()
driver.implicitly_wait(3)
base_url = " https://m.cafe.naver.com/ArticleSearchListAjax.nhn?search.query=%EA%B0%80%EB%A1%9C%EC%88%98%EA%B8%B8%EB%A7%9B%EC%A7%91&search.menuid=0&search.searchBy=0&search.sortBy=date&search.clubid=11262350&search.option=0&search.defaultValue=&search.page=1"

driver.get(base_url)

contentSource = driver.page_source
#print(contentSource)
soup = bs(contentSource, 'html.parser')
#title = soup.find_all("div", {"class" : "tit"})
title = soup.find_all('h3')
print(len(title))
title_list = []
for tit_num in range(len(title)):
	title2 = soup.select('h3')[tit_num].get_text()
	title_list.append({'title' : title2})

print(title_list)
cafe_df = pd.DataFrame(title_list)
cafe_df.to_csv('cafe_crawling.csv', index=False)
# keyword = "가로수길맛집"
# driver.find_element_by_xpath('//*[id="topLayerQueryInput"]').