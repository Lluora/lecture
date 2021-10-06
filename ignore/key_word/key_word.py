##### 연관검색어 ########

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.practice # db이름 dbhomework


from bs4 import BeautifulSoup
import urllib.parse as par
import requests

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('key_word.html')



# 검색하기
@app.route('/order', methods=['POST'])
def order():
    name_receive = request.form['name_give']
    # search_receive = request.form['search_give']
    input = par.quote(name_receive)  # 한글 -> 특수한 문자로 변환
    code = requests.get(
        "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}".format(input))

    # HTML 코드 정리
    soup = BeautifulSoup(code.text, "html.parser")

    title = soup.select("ul.lst_related_srch._list_box >li.item")  # 요소 여러개 한번에

    # 요소의 내용 출력하기
    search_receive = []
    for i in title:
        search_receive.append(i.text)
    # print(search_receive)
    search_receive = "  ".join(search_receive).replace("     ", ",")
    search_receive = str(search_receive.lstrip(" "))


    ## db에 저장하기
    doc = {
        'name': name_receive,
        'search' : search_receive
    }
    db.practice.insert_one(doc)
    return jsonify({'msg': '검색 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def listing():
    orders = list(db.practice.find({}, {'_id': False})) # 모두 불러오기
    return jsonify({'msg': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)