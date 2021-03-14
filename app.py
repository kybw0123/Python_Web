# app.py
from flask import Flask, render_template, jsonify, request

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')

@app.route('/board')
def getboard():
    return render_template('board.html', title='게시판')

if __name__ =="__main__":
    app.run(debug=True)