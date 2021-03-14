# 필요한거 임포트
from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)    # 변수 설정

@app.route('/')
@app.route('/<int:num>')
# 함수 설정
def post(num=None):
    return render_template('main.html', num=num)

# 구구단 불러오기
@app.route('/calculate',methods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('post', num=temp))


if __name__ == "__main__":
    app.run()


