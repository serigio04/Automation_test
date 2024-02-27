import pyautogui as p
import webbrowser as web
import time

web.open("https://web.whatsapp.com/send?phone=+50256248191")
time.sleep(5) 

for i in range(100):
    p.typewrite("te amo musho pinshe morra hermosa")
    p.press("Enter")