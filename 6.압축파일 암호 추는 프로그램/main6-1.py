import itertools
import zipfile

passwd_string = "01234"
zFile = zipfile.ZipFile(r'/Users/devwonny/Documents/40products/6.압축파일 암호 추는 프로그램/ddd.zip')

for len in range(1,6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    print("to_attempt",to_attempt)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        # print(passwd) 
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"password is {passwd}")
            break
        except:
            pass
        
# 40products/6.압축파일 암호 추는 프로그램