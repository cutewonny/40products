import socket
import requests
import re

SIZE = 1024
in_addr =  socket.gethostbyname(socket.gethostname())
print(in_addr)#127.0.0.1  172.30.1.22

in_addr2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr2.connect(("www.google.com", 443))
print(in_addr2)
print("내부 아이피>> ",in_addr2.getsockname())#('172.30.1.22', 62817) ('172.30.1.22', 62821)
#내 아이피 주소(IP Address): 218.154.15.224

in_addr2.send('hi'.encode())  # 서버에 메시지 전송
msg = in_addr2.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
print("resp from server : {}".format(msg))


req = requests.get("http://ipconfig.kr")
# print(req.text)
out_addr = re.search(r'IP Address: \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', req.text)[0]
print("외부 아이피>> ",out_addr)