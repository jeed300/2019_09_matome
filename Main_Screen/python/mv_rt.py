import RPi.GPIO as GPIO
import time
import smbus

I2C_ADDR = 0x3f	# LCD Device
LCD_WIDTH = 16	# Maximum characters per line

LCD_CHR = 1	# MODE: Sending data
LCD_CMD = 0 # MODE: Sending command

LCD_LINE_1 = 0x80	# LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0	# LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94	# LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4	# LCD RAM address for the 4th line

LCD_BACKLIGHT = 0x08	# ON
#LCD_BACKLIGHT = 0x00	# OFF

ENABLE = 0b00000100

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# Open I2C interface
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

MOTOR1_F = 23
MOTOR1_B = 24
MOTOR2_F = 27
MOTOR2_B = 22

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(MOTOR1_F, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(MOTOR1_B, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(MOTOR2_F, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(MOTOR2_B, GPIO.OUT, initial=GPIO.LOW)
	print("Finished set up...")

def lcd_init():
	# Initialize display
	lcd_byte(0x33, LCD_CMD)
	lcd_byte(0x32, LCD_CMD)
	lcd_byte(0x06, LCD_CMD)
	lcd_byte(0x0C, LCD_CMD)
	lcd_byte(0x28, LCD_CMD)
	lcd_byte(0x01, LCD_CMD)
	time.sleep(E_DELAY)

def lcd_byte(bits, mode):
	bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
	bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT 
	
	bus.write_byte(I2C_ADDR, bits_high)
	lcd_toggle_enable(bits_high)

	bus.write_byte(I2C_ADDR, bits_low)
	lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
	time.sleep(E_DELAY)
	bus.write_byte(I2C_ADDR, (bits | ENABLE))
	time.sleep(E_PULSE)
	bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
	time.sleep(E_DELAY)

def lcd_string(message, line):
	message = message.ljust(LCD_WIDTH, " ")
	lcd_byte(line, LCD_CMD)
	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), LCD_CHR)

# main function
def main():
	print("Start...")
	setup()
	# Initialize lcd display
	lcd_init()
#	lcd_string("Hello", LCD_LINE_1)
#	lcd_string("   RPC", LCD_LINE_2)

#	time.sleep(2)

#	lcd_string("Provided by", LCD_LINE_1)
#	lcd_string("PICason", LCD_LINE_2)

#	time.sleep(2)
	
	GPIO.output(MOTOR1_B, GPIO.HIGH)
	GPIO.output(MOTOR2_B, GPIO.LOW)
	GPIO.output(MOTOR1_F, GPIO.LOW)
	GPIO.output(MOTOR2_F, GPIO.HIGH)
	print("MOTOR turning right...")
	lcd_string("MOTOR turn right", LCD_LINE_1)
#	time.sleep(5)
#	GPIO.output(MOTOR1_F, GPIO.LOW)
#	GPIO.output(MOTOR2_F, GPIO.LOW)
#	print("MOTOR stopping...")
#	lcd_string("MOTOR STOP  ", LCD_LINE_1)
#	time.sleep(2)


# Execute methods
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		print('finished mv_fw.py')
