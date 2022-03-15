import requests
from bs4 import BeautifulSoup

url = 'https://dustink.tistory.com/152'
html = requests.get(url)
soup = BeautifulSoup(html.text)

# find_all 함수에 매개변수로 리스트를 전달합니다.
# 다음 코드는 HTML 문서의 모든 'script', 'style', 'header', 'footer', 'form' 태그를 반환합니다.
script_tag = soup.find_all(['script', 'style', 'header', 'footer', 'form'])

# extract 함수는 soup 객체에서 해당 태그를 제거합니다.
for script in script_tag:
    script.extract()

# 텍스트 단위 결합을 '\n'(줄바꿈)으로 합니다.
# 각 텍스트 단위의 시작과 끝에서 공백을 제거합니다.
content = soup.get_text('\n', strip=True)
print(content)