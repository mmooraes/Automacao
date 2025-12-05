import pyautogui
from time import sleep


pyautogui.PAUSE = 0.5 

pyautogui.hotkey('alt', 'tab') 
sleep(1) 

pyautogui.press('tab', presses=38, interval=0.01) 
pyautogui.press('enter')

sleep(1)

pyautogui.press('tab', presses=14, interval=0.01)
pyautogui.press('enter')

sleep(1.5)

pyautogui.press('tab', presses=3, interval=0.1)
sleep(1)
pyautogui.press('enter')
