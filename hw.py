'''
<post>
client가 sever한테 url과 comment를 주면
server는 url과 comment를 가지고 title, image, description 크롤링 진행

<get>
크롤링 한 것을 가지고 db의 저장된 length만큼 for문을 돌려서
title, image, description, url, comment를 카드에 저장

'''

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test12

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('hw.html')


@app.route('/stock', methods = ['POST'])
def save_info():
    info = request.json
    stocks = info({"market":"market-1","sector":"sector-1","tag":"tag-1"})
    return jsonify(stocks)

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)