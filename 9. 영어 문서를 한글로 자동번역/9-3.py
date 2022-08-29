from os import linesep
from unittest import result
import googletrans

translator = googletrans.Translator()

read_file_path = r"/Users/devwonny/Documents/40products/9. 영어 문서를 한글로 자동번역/english.txt"
write_file_path = r"/Users/devwonny/Documents/40products/9. 영어 문서를 한글로 자동번역/korea.txt"


with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f: #a 옵션은 마지막에 추가한다
        f.write(result1.text + '\n')