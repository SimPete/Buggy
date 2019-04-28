# Script pour controler deux moteurs en Python. 

# Import required modules
import time
import RPi.GPIO as GPIO
import sys
# import stdin

# Initializing variables
print "Initializing variables..."
MotorA_PWM_Activation = 0
MotorB_PWM_Activation = 0

# Declare the GPIO settings
print "Setting GPIO mode to BOARD..."
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
print "Setting up GPIO pins to OUTPUT..."
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB

# Set all the GPIO pins by setting them to LOW
print "Setting up GPIO pins to LOW..."
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB

# def getch(): #FONCTION A VERIFIER (https://www.instructables.com/id/Controlling-a-Raspberry-Pi-RC-Car-With-a-Keyboard/)
#    fd = sys.stdin.fileno()
#    ch = sys.stdin.read(1)
#    return ch

print "Entering the DEF zone..."

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

def MotorA_PWM(MotorA_DutyCycle):
	if MotorA_PWM_Activation = 0:
		print "Activating PWM on motor A..."
		MotorA_PWM = GPIO.PWM(7, 50) 		#Start PWM on Pin 7 with a frequency of 50Hz 
		MotorA_PWM.start(MotorA_DutyCycle)  # start the PWM on 50 percent duty cycle  
		MotorA_PWM_Activation = 1
	else: 
		print "Updating Motor A duty cycle"
		MotorA_PWM.ChangeDutyCycle(MotorA_DutyCycle)
	
	# duty cycle value can be 0.0 to 100.0%, floats are OK  
	# p.ChangeDutyCycle(90)      # change the duty cycle to 90%  
	# p.ChangeFrequency(100)     # change the frequency to 100 Hz (floats also work)  
							     # e.g. 100.5, 5.2  
	# MotorA_PWM.stop()          # stop the PWM output 

	
def MotorB_PWM(MotorB_DutyCycle):
	if MotorB_PWM_Activation = 0:
		print "Activating PWM on motor B..."
		MotorB_PWM = GPIO.PWM(18, 50) 		#Start PWM on Pin 7 with a frequency of 50Hz 
		MotorB_PWM.start(MotorB_DutyCycle)  # start the PWM on 50 percent duty cycle  
		MotorB_PWM_Activation = 1
	else: 
		print "Updating Motor B duty cycle"
		MotorB_PWM.ChangeDutyCycle(MotorB_DutyCycle)

def cleanup():
	# Reset all the GPIO pins by setting them to LOW
	GPIO.output(12, GPIO.LOW) # Set AIN1
	GPIO.output(11, GPIO.LOW) # Set AIN2
	GPIO.output(7, GPIO.LOW) # Set PWMA
	GPIO.output(15, GPIO.LOW) # Set BIN1
	GPIO.output(16, GPIO.LOW) # Set BIN2
	GPIO.output(18, GPIO.LOW) # Set PWMB
	GPIO.cleanup()
	print "GPIO are clean!"

def main():
#TODO MainFunction with keyboard controls, add exit criteria
        try:
			while True:   
				print "We're in the game now!"
				# Drive the motor clockwise
				# Motor A:
				GPIO.output(12, GPIO.HIGH) # Set AIN1
				GPIO.output(11, GPIO.LOW) # Set AIN2
				# Motor B:
				GPIO.output(15, GPIO.HIGH) # Set BIN1
				GPIO.output(16, GPIO.LOW) # Set BIN2
			
				# Set the motor speed
				# Motor A:
				MotorA_PWM(25) # Set PWMA
				# Motor B:
				MotorB_PWM(25) # Set PWMB
						
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
				MotorA_PWM(50) # Set PWMA
				# Motor B:
				MotorB_PWM(50) # Set PWMB
			
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
                print "We're in the End Game now!"
		cleanup() # GPIO cleanup on exit
	
if __name__ == "__main__":
	main()
  
print "Job's done!"