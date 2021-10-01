from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

now = datetime.now()
reg_date = "{}.{}.{} {}:{}:{}".format(now.year, now.month,  now.day,  now.hour,  now.minute, now.second)

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def save_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    for i in range(len(title_receive)):
        idxx = i
    ## db에 저장하기
    doc = {
        'idx' : idxx,
        'title': title_receive,
        'content': content_receive,
        'reg_date': reg_date,
    }
    db.memo.insert_one(doc)
    return jsonify({'result': 'success', 'msg': "포스팅 성공!"})

@app.route('/post', methods=['GET'])
def get_post():
    post = list(db.memo.find({}, {'_id': False}).sort("idx"))
    return {"result": post}

@app.route('/post', methods=['DELETE'])
def delete_post():
    name_received = request.form["idx"]
    db.memo.delete_one({'idx':name_received})
    return jsonify({'msg': '삭제되었습니다!'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)