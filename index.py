#!/opt/anaconda3/bin/python3

# 파일 권한 설정 하는 방법
# 터미널을 이용해 실행 파일의 위치로 이동
# ls -al 로 파일별 권한 확인
# sudo chmod a+x 파일이름
# 비밀번호 입력
# ls -al 로 변경된 권한 확인

# 실행 안되면 error_log 확인
# errorcode 검색
# 실행할 python의 위치를 최상단에 주석을 ! + 파이썬 위치추가

# 그다음에 뜨는 error_log 확인
# print("Content-Type: text/html")    # HTML is following
# print()                             # blank line, end of headers
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
print('hello world')
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li><a href="1.html">HTML</a></li>
    <li><a href="2.html">CSS</a></li>
    <li><a href="3.html">JavaScript</a></li>
  </ol>
  <h2>WEB</h2>
  <p>The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.
  </p>
</body>
</html>
''')