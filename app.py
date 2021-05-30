# app.py
# -- coding: utf-8 --
from flask import Flask, render_template, jsonify, request

#Flask 객체 인스턴스 생성
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')

@app.route('/board')
def board():
    return render_template('board.html', title='게시판')

#회원가입 페이지
@app.route("/signup")
def signup():
    return render_template('membership.html', title='회원가입')

@app.route("/user_info", methods=['POST'])
def user_info():
    user_id = request.form['user_id']
    user_pw = request.form['user_pw']
    user_pw2 = request.form['user_pw2']
    user_name = request.form['user_name']
    user_date = request.form['user_date']
    user_phone = request.form['user_phone']
    user_sms = request.form['sms']
    user_email = request.form['user_email']
    user_info = request.form

    return user_info

if __name__ =="__main__":
    app.run(debug=True)