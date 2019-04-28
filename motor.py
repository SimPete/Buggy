# Script pour contrôler deux moteurs en Python. 

# Import required modules
import time
import RPi.GPIO as GPIO
import sys
import stdin

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB

# Set all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(13, GPIO.LOW) # Set STBY
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB

# def getch(): #FONCTION À VÉRIFIER (https://www.instructables.com/id/Controlling-a-Raspberry-Pi-RC-Car-With-a-Keyboard/)
#    fd = sys.stdin.fileno()
#    ch = sys.stdin.read(1)
#    return ch

def MotorA_FWD():
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	
def MotorB_FWD():
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)
	
def MotorA_BWD():
	GPIO.output(12, GPIO.LOW)
	GPIO.output(11, GPIO.HIGH)
	
def MotorB_BWD():
	GPIO.output(15, GPIO.LOW)
	GPIO.output(16, GPIO.HIGH)

def Handbrakes():
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)

# def # MotorA_PWM(MotorA_DutyCycle)
	# Modulation du moteur A #TODO

# def #TODO MotorB_PWM

def cleanup():
	# Reset all the GPIO pins by setting them to LOW
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(13, GPIO.LOW) # Set STBY
	GPIO.output(15, GPIO.LOW) # Set BIN1
	GPIO.output(16, GPIO.LOW) # Set BIN2
	GPIO.output(18, GPIO.LOW) # Set PWMB
	GPIO.cleanup()
	print "GPIO are clean!"

def #main()
#TODO MainFunction with keyboard controls, add exit criteria
	try:  
		# Drive the motor clockwise
		# Motor A:
		GPIO.output(12, GPIO.HIGH) # Set AIN1
		GPIO.output(11, GPIO.LOW) # Set AIN2
		# Motor B:
		GPIO.output(15, GPIO.HIGH) # Set BIN1
		GPIO.output(16, GPIO.LOW) # Set BIN2
		
		# Set the motor speed
		# Motor A:
		GPIO.output(7, GPIO.HIGH) # Set PWMA
		# Motor B:
		GPIO.output(18, GPIO.HIGH) # Set PWMB
		
		# Disable STBY (standby)
		GPIO.output(13, GPIO.HIGH)
		
		# Wait 5 seconds
		time.sleep(5)
		
		# Drive the motor counterclockwise
		# Motor A:
		GPIO.output(12, GPIO.LOW) # Set AIN1
		GPIO.output(11, GPIO.HIGH) # Set AIN2
		# Motor B:
		GPIO.output(15, GPIO.LOW) # Set BIN1
		GPIO.output(16, GPIO.HIGH) # Set BIN2
		
		# Set the motor speed
		# Motor A:
		GPIO.output(7, GPIO.HIGH) # Set PWMA
		# Motor B:
		GPIO.output(18, GPIO.HIGH) # Set PWMB
	
		# Disable STBY (standby)
		GPIO.output(13, GPIO.HIGH)
		
		# Wait 5 seconds
		time.sleep(5)
  
	except KeyboardInterrupt:  
		# here you put any code you want to run before the program   
		# exits when you press CTRL+C  
		print "The dreaded Ctrl+C was pressed. Exiting now..." 
  
	except:  
		# this catches ALL other exceptions including errors.  
		# You won't get any error messages for debugging  
		# so only use it once your code is working  
		print "Other error or exception occurred!"  

	finally:  
		cleanup() # GPIO cleanup on exit

		

if __name__ == '__main__'
	main()
  
GPIO.cleanup() # Second cleanup... just in case
print "Cleaned up a second time... without the function... just in case! The program is done now!" 
print "Job's done!"