import RPi.GPIO as GPIO
import time

def move_servo(pino, angulo):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pino, GPIO.OUT)

    pwm = GPIO.PWM(pino, 50)  # Frequência de 50Hz (servo motor padrão)
    pwm.start(0)

    duty = angulo / 18 + 2
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)

    pwm.stop()
    GPIO.cleanup()
