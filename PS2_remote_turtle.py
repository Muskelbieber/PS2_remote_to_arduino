##############
## Script listens to serial port and does stuff
##############
## requires pySerial to be installed 
import serial
import turtle
from PS2_remote_data import serial_port,\
 baud_rate,\
 button_to_signal,\
 signal_to_button, signal_to_int
  
ser = serial.Serial(serial_port, baud_rate)
#The Information function to print all button uses
def info():
	print('OPEN/CLOSE: Terminate the whole programm by exit()')
	print('PLAY: Activates/deactivates Turtle gamemode')
	print('Triangle: Display Turtle shape')
	print('Up arrow: Turtle move 25 in forward facing direction')
	print('Left arrow: Turtle rotates left 5 degrees')
	print('Right arrrow: Turtle rotates right 5 degrees')
	print('Display: Shows this information again in the terminal')


turtle_val=False;
info();
while(True):
	line = ser.readline();
	#ser.readline returns a binary, convert to string
	line = line.decode("utf-8");
	
	#Terminal output of what one pressed
	print(line);
	print(signal_to_button[line]);
	print(signal_to_int[line]);
	
	
	#System commands
	#if(signal_to_int[line]==int('0x68B5B', 0)):exit();#OPEN/CLOSE
	if(signal_to_int[line]==signal_to_int[button_to_signal['OPEN/CLOSE']]):
		exit();#OPEN/CLOSE
	#Help Information again displaying
	if(signal_to_int[line]==signal_to_int[button_to_signal['DISPLAY']]):
		info();
	#Draw play Turtle
	if(signal_to_int[line]==signal_to_int[button_to_signal['PLAY']]):
		turtle_val = not turtle_val;
	if(turtle_val==True): 
		if(signal_to_int[line]==signal_to_int[button_to_signal['Triangle']]):
			turtle.shape("turtle") 
		if(signal_to_int[line]==signal_to_int[button_to_signal['Up arrow']]):
			turtle.forward(25); 
		if(signal_to_int[line]==signal_to_int[button_to_signal['Right arrow']]):
			turtle.right(5); 
		if(signal_to_int[line]==signal_to_int[button_to_signal['Left arrow']]):
			turtle.left(5);
