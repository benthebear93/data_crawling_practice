import urllib.request
from bs4 import BeautifulSoup
import os

week_path = []
basic_path = "/home/benlee/Desktop/crawling_img/"
week = ['mon','tue','wed','thu','fri','sat','sun']

def make_dir():
	for i in range(len(week)):
		a = week[i]
		week_path.append(basic_path + a) 
		os.mkdir(week_path[i])

def save_file(day, title):
	f = open(basic_path + day + '/' + str(title) +".jpg", 'wb')
	img_file = urllib.request.urlopen(img_link)
	f.write(img_file.read())
	f.close()


make_dir()
req = urllib.request.Request('https://comic.naver.com/webtoon/weekday.nhn')
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

link = soup.find_all("div", {"class" : "thumb"})
for m in link:
	week_check = m.a.get("href")
	week_check  = week_check[-3:]
	imgUrl = m.find_all("img")
	for j in imgUrl:
		img_link = j.get('src')
		title = j.get('alt')
		idx = 1
		save_file(week_check, title)