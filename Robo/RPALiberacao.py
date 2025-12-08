import pyautogui
from time import sleep

#Colocar a quantidade de reptições
repeticoes = 7                                                                                    

pyautogui.PAUSE = 0.5 

pyautogui.hotkey('alt', 'tab') 
sleep(1) 
for i in range(repeticoes):
    print(f"Executando ciclo {i + 1}...")

    if i == 0:
        tabs_iniciais = 38
    else:
        tabs_iniciais = 39
    
    pyautogui.press('tab', presses=tabs_iniciais, interval=0.01) 
    pyautogui.press('enter')

    sleep(1)

    pyautogui.press('tab', presses=14, interval=0.01)
    pyautogui.press('enter')

    sleep(1)

    pyautogui.press('tab', presses=3, interval=0.1)
    sleep(0.1)
    pyautogui.press('enter')
    
    sleep(1) 

print("Automação finalizada!")