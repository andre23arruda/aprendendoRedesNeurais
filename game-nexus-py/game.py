# importando módulos
import RPi.GPIO as GPIO # leitura GPIO
import time # para dar sleep
import pyautogui # comandos no pc 
import webbrowser
import psutil    


PIN_JUMP = 12
PIN_START = 10

path = r"\path\t-rex-runner-add-game-timeout\index.html"
webbrowser.open(path, new = 0, autoraise=False)
time.sleep(0.5)
pyautogui.press('f11')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('-')
pyautogui.keyUp('-')
pyautogui.keyUp('ctrl')
time.sleep(0.5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('+')
pyautogui.keyUp('+')
pyautogui.keyUp('ctrl')
time.sleep(0.5)

## inicializando GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_JUMP, GPIO.IN, pull_up_down = GPIO.PUD_UP) # pino 10 -> dino pula
GPIO.setup(PIN_START, GPIO.IN, pull_up_down = GPIO.PUD_UP) # pino 11 -> start game

def jump_callback(channel):
    pyautogui.keyDown('space')
    time.sleep(0.025)
    pyautogui.keyUp('space')  
    print("Dino pula")

def start_callback(channel):
    pyautogui.keyDown('left')
    time.sleep(0.025)
    pyautogui.keyUp('left')  
    print("Começa o jogo")
    return 1

GPIO.add_event_detect(PIN_JUMP, GPIO.RISING, callback = jump_callback) # Setup event on PIN_JUMP rising edge
GPIO.add_event_detect(PIN_START, GPIO.RISING, callback = start_callback) # Setup event on PIN_START rising edge

while "chrome.exe" in (p.name() for p in psutil.process_iter()):  
    pass

print('finish')
GPIO.cleanup() # Clean up
