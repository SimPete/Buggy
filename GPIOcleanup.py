# Script for GPIO cleanup after running motor.py

import RPi.GPIO as GPIO

# Declare the GPIO settings
print "Setting GPIO mode to BOARD"
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
print "Setting up GPIO pins to OUTPUT"
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB

# Set all the GPIO pins by setting them to LOW
print "Setting up GPIO pins to LOW"
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB
GPIO.cleanup()
print "GPIO are clean!"
print "Job's done!"
