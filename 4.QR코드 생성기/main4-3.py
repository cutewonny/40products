import qrcode
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
file_path = os.path.join(BASE_DIR, "qr코드모음") +".txt"

# file_path = r'save_path2'
# r: 모든 Escape 문자를 그대로 출력해 준다.

print(file_path) #save_path2

with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()
    for line in read_lines:
        line = line.strip()
        print(line)
        
        qr_data= line
        qr_image = qrcode.make(qr_data)
        save_path = os.path.join(BASE_DIR, qr_data) +".png"
        qr_image.save(save_path)
        
# www.naver.com
# www.google.com
# www.daum.net
        
