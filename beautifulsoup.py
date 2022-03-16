from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://dustink.tistory.com/159")
soup = BeautifulSoup(target, "html.parser", from_encoding='cp949')
all = soup.find_all(['body'])


for item in all:
    content = soup.get_text('\n', strip=True)
    print(content)
