import pymysql # pymysql 임포트
import csv
# 전역변수 선언부
conn = None
cur = None

data1 = "fdfaf"
data2 = "asdff"
data3 = ""
data4 = ""

sql=""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='test', charset='utf8')
cur = conn.cursor()
conn.commit()
# 파일 불러오기 모드는 읽기만
f = open('C:/Users/kybw0/Downloads/EPL.csv','r')

# csv읽기
csvReader = csv.reader(f)

# for문으로 insert into 반복하기 각각의 값은 row의 지정한 변수에 저장
# sql문에 넣을 쿼리문 작성
# 미리 지정해놓은 변수를 마지막 spl문에서 설정
for row in csvReader:
    team_id = (row[0])
    team_name = (row[1])
    player_backnumber = (row[2])
    player_position = (row[3])
    player_country = (row[4])
    player_name = (row[5])

    sql = '''insert into epl(team_id, team_name, player_backnumber,player_position,player_country,player_name) values (%s, %s, %s, %s, %s, %s)'''# sql변수에 SQL문 입력
    cur.execute(sql,(team_id,team_name,player_backnumber,player_position,player_country,player_name))
#sql = "INSERT INTO 챔스 VALUES ('변수1', '변수2')"
# 커서로sql 실행

# while (True) : # 반복실행
#      row = cur.fetchone() # row에 커서(테이블 셀렉트)를 한줄 입력하고 다음줄로 넘어감
#      if row== None : # 커서(테이블 셀렉트)에 더이상 값이 없으면
#          break # while문을 빠져나감
#      data3 = row[0]
#      data4 = row[1]
#      print("%5s %5s" % (data3, data4))

conn.commit() #값을 넣을때 추가해야됨

f.close()
conn.close() # 접속 종료
print('실행완료')