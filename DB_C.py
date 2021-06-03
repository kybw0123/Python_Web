# 파이썬으로 DB에 데이터를 넣는 코드를 짜야함
import pymysql
import pandas as pd
'''
user = 'user name'
passwd = 'password'
host = DB의 IP 주소
db = 연결할 db 이름
charset = 인코딩 설정
'''
def db(sql):
    db_connect = pymysql.connect(
    user = 'root',
    passwd = '1',
    host = '127.0.0.1',
    db = 'python_web',
    charset = 'utf8'
    )
    cur = db_connect.cursor()
#    cursor.commit()
    #sql = 'SELECT * FROM `EPL`;'
    cur.execute(sql)
    result = cur.fetchall()
    result = pd.DataFrame(result)
    print(result)
    db_connect.commit()
    cur.close()
if __name__ == '__main__':
    #sql = "insert into epl(team_id, team_name, player_backnumber,player_position,player_country,player_name) values ('21', '테스트', '5', 'K', '대한민국', '테스트2');"
    sql = 'SELECT * FROM EPL;'
    db(sql)