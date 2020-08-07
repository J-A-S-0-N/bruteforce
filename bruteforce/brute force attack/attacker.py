import time 
import pyautogui

main = 0

pyautogui.FAILSAFE = False
print(pyautogui.position())
screenWidth, screenHight = pyautogui.size()
while True:
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(685, 24)
    pyautogui.click(button='left')
    pyautogui.typewrite(['f5', 'enter'], interval=0.7)
    pyautogui.moveTo(322, 1047)
    pyautogui.click(button='left')
    pyautogui.typewrite([str(main)], interval=0.7)
    pyautogui.typewrite(['enter'], interval=0.7)
    main = main + 1