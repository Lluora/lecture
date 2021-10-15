from datetime import datetime

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/article', methods=['POST'])
def save_post():
    title = request.form.get('title')
    content = request.form.get('content')
    article_count = db.article.count()
    if article_count == 0: # 저장된 db가 없으면
        max_value = 1 # index 1
    else:
        max_value = db.article.find_one(sort=[("idx", -1)])['idx'] + 1
        # 최근 날짜 순으로 정렬하고 가장 마지막 INDEX 번호에서 +1로 저장하기

    post = {
        'idx': max_value, # 번호
        'title': title, # 타이틀
        'content': content, # 내용
        'read_count': 0, # 조회수
        'reg_date': datetime.now() # 저장 날짜
    }
    db.article.insert_one(post)
    return {"result": "success"}


@app.route('/articles', methods=['GET'])
def get_posts():
    order = request.args.get('order') # order를 받아서
    if order == "desc": # order가 desc이면
        articles = list(db.article.find({}, {'_id': False}).sort([("read_count", -1)])) # 조회수가 많은 데이터 순
    else:
        articles = list(db.article.find({}, {'_id': False}).sort([("reg_date", -1)])) # 최신 작성된 데이터 순

    for a in articles:
        a['reg_date'] = a['reg_date'].strftime('%Y.%m.%d %H:%M:%S') # #2021.10.03 23:00:00 형식으로 출력

    return jsonify({"articles": articles})


@app.route('/article', methods=['DELETE'])
def delete_post(): # 데이터의 유니크한 번호인 idx 컬럼을 사용하여 삭제
    idx = request.args.get('idx')
    db.article.delete_one({'idx': int(idx)})
    return {"result": "success"}


@app.route('/article', methods=['GET'])
def get_post(): # 수정 버튼 눌렀을 때
    idx = request.args['idx'] # idx를 받음
    article = db.article.find_one({'idx': int(idx)}, {'_id': False})
    return jsonify({"article": article})


@app.route('/article', methods=['PUT'])
def update_post():
    idx = request.form.get('idx')
    title = request.form.get('title')
    content = request.form.get('content')
    db.article.update_one({'idx': int(idx)}, {'$set': {'title': title, 'content': content}})
    # idx가 int(해당 idx 번호)에 해당하는 title, content를 수정
    return {"result": "success"}


@app.route('/article/<idx>', methods=['PUT'])
def update_read_count(idx):
    db.article.update_one({'idx': int(idx)}, {'$inc': {'read_count': 1}})
    article = db.article.find_one({'idx': int(idx)}, {'_id': False})
    return jsonify({"article": article})

# update에서 $set은 필드 추가 및 필드 값 수정을 말하고
# $inc는 게시글 조회수 증가 같은 것을 할 때 사용
# 참고 사이트 >> https://loveiskey.tistory.com/135


@app.route('/article/input', methods=['GET'])
def get_inputbox(): # 수정 버튼 눌렀을 때
    text = request.args['box'] # idx를 받음
    article = db.article.find_one({'title': text}, {'_id': False})
    return jsonify({"article": article})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
