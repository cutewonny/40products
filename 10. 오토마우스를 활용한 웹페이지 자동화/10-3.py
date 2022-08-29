import pyautogui
import time
import pyperclip

# while True:
#     print(pyautogui.position())
#     time.sleep(0.5)

pyautogui.moveTo(682,182, 0.2)
pyautogui.click()
time.sleep(0.5)

start_x = 685
start_y = 211

end_x = 1004
end_y = 712

pyautogui.screenshot(r'/Users/devwonny/Documents/40products/10. 오토마우스를 활용한 웹페이지 자동화/seoulWeather.png', region=(start_x, start_y, end_x, end_y))