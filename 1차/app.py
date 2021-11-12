from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

####### 저장하고 삭제 기능 추가 ###########
from pymongo import MongoClient
client = MongoClient('localhost', 27017)


db = client.spring # db이름 dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
## 이름, 수량, 주소, 전화번호 받아서 db에 넣어준다.
@app.route('/write', methods=['GET'])
def save_order():
    content = request.form['name_give']

    ## db에 저장하기
    doc = {
        'content': content
    }
    db.orders.insert_one(doc)
    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/write', methods=['GET'])
def view_orders():
    content = list(db.orders.find({}, {'_id': False})) # 모두 불러오기
    return jsonify({'result': 'success', 'content': content})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)