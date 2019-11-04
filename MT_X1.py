import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(4, 1300) #アーム全体　中央1300
time.sleep(3)
pi.set_servo_pulsewidth(13, 1500) #アーム高さ　1500
time.sleep(3)
