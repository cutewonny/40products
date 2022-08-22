import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attemp = itertools.product(passwd_string, repeat=len)
        print("to_attemp>> ", to_attemp)
        print("len>>>> ", len)
        for attempt in to_attemp:
            passwd = ''.join(attempt)
            # print(passwd) 
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f"password is {passwd}")
                return 1
            except:
                pass
        

passwd_string = "abcdefgh0123456789"
zFile = zipfile.ZipFile(r'/Users/devwonny/Documents/40products/6.압축파일 암호 추는 프로그램/ddd.zip')

min_len = 1
max_len = 5
unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result ==1:
    print("password find")
else:
    print("cant find password")