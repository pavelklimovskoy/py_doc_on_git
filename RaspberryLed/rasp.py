import RPi.GPIO as GPIO
from gpiozero import CPUTemperature

cpu = CPUTemperature()


LED = 14

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)


while(true):
    if(int(cpu.temperature) > 40):
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
    
    sleep(100)




