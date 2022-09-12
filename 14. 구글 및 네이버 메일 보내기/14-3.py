from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

send_email = 
send_pwd = 
recv_email= "devwonny@gmail.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
메일 내용을 여기에 적습니다.
여러 줄을 입력하여도 됩니다.
"""
msg = MIMEMultipart()
contentPart = MIMEText(text)
msg.attach(contentPart)
etc_file_path = r'/Users/devwonny/Documents/40products/14. 구글 및 네이버 메일 보내기/첨부파일.txt'
with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition','attachment',filename="첨부파일.txt")
    msg.attach(etc_part)
    
msg['Subject'] = "메일 제목"
msg['From'] = send_email
msg['To'] = recv_email

print(msg.as_string())

s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

