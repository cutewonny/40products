import qrcode
import os


qr_data = 'www.google.com'
qr_image = qrcode.make(qr_data)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
print(BASE_DIR)
print(os.getcwd())
#/Users/devwonny/Documents/40products/4.QR코드 생성기

# 윈도우에선 백슬래시(\)를 사용하지만, Mac os에서는 슬래시(/)를 사용합니다.
save_path = "/Users/devwonny/Documents/40products/4.QR코드 생성기/"+qr_data+".png"
print(os.path.join('user','Desktop','Python'))

save_path2 = os.path.join(BASE_DIR, qr_data) +".png"
print(save_path2)#/Users/devwonny/Documents/40products/4.QR코드 생성기/www.google.com.png

qr_image.save(save_path)