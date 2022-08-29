import pyautogui
import time
import pyperclip

pyautogui.moveTo(847, 247, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("안경 남자")
pyautogui.hotkey("command","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)