from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://finance.naver.com/")
soup = BeautifulSoup(target, "html.parser", from_encoding='cp949')
tbody = soup.select("#_topItems1 > tr")

for item in tbody:
    name = item.select_one("th > a").string
    curr = item.select_one("td:nth-child(2)").string
    updown = item.select_one("td:nth-child(3) > em").string
    if name == "삼부토건" or name == "세종메디칼":
        print(name, curr, updown)

