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