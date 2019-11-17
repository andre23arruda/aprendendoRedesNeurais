# importando módulos
import RPi.GPIO as GPIO # leitura GPIO
import time # para dar sleep
import pyautogui # comandos no pc 

# inicializando GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # pino 10 -> dino pula
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # pino 11 -> start game

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

GPIO.add_event_detect(10, GPIO.RISING, callback = jump_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(11, GPIO.RISING, callback = start_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up

