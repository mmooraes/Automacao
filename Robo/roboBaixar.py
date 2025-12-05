import pyautogui
import pyautogui
from time import sleep

repeticoes = 2                                                                                   

pyautogui.PAUSE = 0.5

pyautogui.hotkey('alt', 'tab') 
sleep(1) 
for i in range(repeticoes):
    print(f"Executando ciclo {i + 1}...")

    if i == 0:
        tabs_iniciais = 41                                  
    else:
        tabs_iniciais = 42
    
    pyautogui.press('tab', presses=41, interval=0.01) 
    pyautogui.press('enter')

    sleep(1)

    pyautogui.press('tab', presses=14, interval=0.01)
    pyautogui.press('enter')

    sleep(1)

    pyautogui.press('tab', presses=3, interval=0.02)
    sleep(0.2)
    pyautogui.press('enter')

    sleep(2) 
    
    """

    pyautogui.press('tab', presses=41, interval=0.01) 
    pyautogui.press('enter')

    sleep(1) 

    pyautogui.press('tab', presses=20, interval=0.01)
    pyautogui.press('enter')

    sleep(1) 
    pyautogui.press('tab', presses=15, interval=0.01)
    pyautogui.press('enter')

    sleep(1)

    pyautogui.press('tab', presses=3, interval=0.01)
    pyautogui.press('enter')"""

print("Automação finalizada!")