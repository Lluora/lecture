from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

####### 저장하고 삭제 기능 추가 ###########
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://test:test@localhost', 27017)
# id(첫번째 test)와 password(두번째 test)를 입력한 상태로 실행

db = client.shopping # db이름 dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
## 이름, 수량, 주소, 전화번호 받아서 db에 넣어준다.
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    ## db에 저장하기
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문 완료!'})


@app.route('/api/delete', methods=['POST'])
def delete_name():
    name_received = request.form["name_give"] # 이름을 받는다.
    db.orders.delete_one({'name':name_received}) # 받은 이름으로 삭제하기
    return jsonify({'msg': '삭제되었습니다!'})

# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False})) # 모두 불러오기
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)