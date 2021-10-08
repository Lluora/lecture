from datetime import datetime

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    title = request.form.get('title')
    content = request.form.get('content')
    view = 0
    post_count = db.post.count()
    if post_count == 0:
        max_value = 1
    else:
        max_value = db.post.find_one(sort=[("idx", -1)])['idx'] + 1

    post = {
        'idx': max_value,
        'title': title,
        'content': content,
        'reg_date': datetime.now(),
        'view' : view
    }
    db.post.insert_one(post)
    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    posts = list(db.post.find({}, {'_id': False}).sort([("view", -1)]))
    return jsonify({"posts": posts})

@app.route('/post/get', methods=['GET'])
def update_post():
    title = request.args.get('title')
    title = list(db.post.find_one({"title":title}, {'_id': False}))
    return {"result": "success", "title" : title}


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx = request.args.get('idx')
    db.post.delete_one({'idx': int(idx)}).sort([("view", -1)])
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)