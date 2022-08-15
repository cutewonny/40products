import qrcode
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
save_path2 = os.path.join(BASE_DIR, "qr코드모음") +".txt"

file_path = r'save_path2'
# r: 모든 Escape 문자를 그대로 출력해 준다.

print(file_path) #save_path2

with open(save_path2, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()
    for line in read_lines:
        line = line.strip()
        print(line)
# www.naver.com
# www.google.com
# www.daum.net
        
