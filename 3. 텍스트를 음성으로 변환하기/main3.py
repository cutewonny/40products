from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
text =  "안녕하세요 파이썬과 40개 작품입니다"
tts = gTTS(text=text, lang='ko')
# tts.save(r"텍스트를 음성으로 변환\hi.mp3")
tts.save("hi.mp3")
playsound("hi.mp3")