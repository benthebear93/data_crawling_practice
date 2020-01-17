import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.Request('https://comic.naver.com/webtoon/weekday.nhn')
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

# imgUrl = soup.select(
#     '#section_content > div > div:nth-child(1) > div.post_content.entry-content > div.hentry > div:nth-child(2) > div > img'
#     )
#soup = soup.find("div", class_="hentry")
imgUrl = soup.find_all("img")
print(imgUrl)
#urllib.request.urlretrieve(imgUrl, soup.select("img")["alt"]+'.jpg')
idx = 1
for m in imgUrl:
	#print(m.get('src'))
	img_link = m.get('src')
	img_file = urllib.request.urlopen(img_link)
# 	f = open("/home/benlee/Desktop" + str(idx) +".jpg", 'wb')
# 	f.write(img_file.read())
# 	idx +=1
# f.close()

# for title in my_titles:
#     print(title.text)

#     print(title.get('href'))

#body > div.body > div > div.header > h1 > a