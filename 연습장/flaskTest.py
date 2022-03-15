from flask import Flask
from urllib import request
from bs4 import BeautifulSoup as bs

target = request.urlopen("https://finance.naver.com/")
soup = BeautifulSoup(target, "html.parser", from_encoding='cp949')
tbody = soup.select("#_topItems1 > tr")
app = Flask(__name__)

@app.route("/")
def hello():
    html = """<h1>Hello World!</h1>
    <p>파이썬 웹프로젝트</p>
    <a href='https://www.naver.com'>네이버</a>"""
    html += tbody

    return html