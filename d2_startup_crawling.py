from selenium import webdriver
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
driver = webdriver.Chrome('C:/Users/UNIST/Desktop/chromedriver')
driver.implicitly_wait(3)

driver.get('http://www.d2startup.com/portfolio')
#req = driver.page_source
#soup=BeautifulSoup(req, 'html.parser')
listOFLinks =driver.find_elements_by_xpath("//li[@class='card']")

#print(listOFLinks[1].text)
area = []
for link in listOFLinks:
    #a = link.find_elements_by_xpath("//div[@class='card_tag']")
    a = link.find_elements_by_xpath("//a[@class='label_tag']")
for i in range(int(len(a)/2), len(a)):
    print(a[i].text)
    print(len(a[i].text))
    area.append(a[i].text)
basic_area = list(set(area))
group = {}
for lst in area:
    try: group[lst] += 1
    except: group[lst] = 1

group_data = list(group.values())
group_name = list(group.keys())

plt.pie(group_data, labels=group_name, autopct='%0.1f%%')
plt.legend(group_name)
plt.axis('equal')
plt.title('Naver D2 Startup Distribution', fontsize=20)
plt.show()

