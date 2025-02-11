import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
tb_servo = kit.servo[0]
rl_servo = kit.servo[1]

# Set an initial pulse width that you suspect to be close to center
# Set the servo to a reasonable default position (center)
tb_servo.angle = 180  # Adjust as needed
rl_servo.angle = 180
time.sleep(0.15)  # Adjust as needed
rl_servo.angle = 90# Adjust as needed
time.sleep(1)  







