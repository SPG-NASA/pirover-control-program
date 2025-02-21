# (running on raspberry pi)
import socket
import RPi.GPIO as GPIO
import time

# Pin Definitions
IN1 = 17
IN2 = 22
ENA = 5
IN3 = 23
IN4 = 24
ENB = 6

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([IN1, IN2, ENA, IN3, IN4, ENB], GPIO.OUT)

# Initialize PWM
pwm_a = GPIO.PWM(ENA, 1000)  # 1 kHz frequency
pwm_b = GPIO.PWM(ENB, 1000)  # 1 kHz frequency
pwm_a.start(0)
pwm_b.start(0)

def set_motor_a(forward, speed):
    GPIO.output(IN1, forward)
    GPIO.output(IN2, not forward)
    pwm_a.ChangeDutyCycle(speed)

def set_motor_b(forward, speed):
    GPIO.output(IN3, forward)
    GPIO.output(IN4, not forward)
    pwm_b.ChangeDutyCycle(speed)



HOST = "192.168.1.104" 
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            match data.decode('utf-8'):
                case "s":
                    set_motor_a(True, 100)  
                    set_motor_b(True, 100)  
                    time.sleep(0.2)
                    set_motor_a(True, 0)
                    set_motor_b(True, 0)
                case "w":
                    set_motor_a(False, 100)  
                    set_motor_b(False, 100) 
                    time.sleep(0.2)
                    set_motor_a(False, 0)
                    set_motor_b(False, 0)
                case "a":
                    set_motor_a(True, 100)
                    time.sleep(0.2)
                    set_motor_a(True, 0)
                case "d":
                    set_motor_b(True, 100)
                    time.sleep(0.2)
                    set_motor_b(True, 0)
            
