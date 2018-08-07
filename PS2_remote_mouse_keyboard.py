##############
## Script listens to serial port and does stuff
##############
## requires pySerial to be installed 
import serial
from PS2_remote_data import serial_port,\
 baud_rate,\
 button_to_signal,\
 signal_to_button, signal_to_int
 
import pyautogui;

pyautogui.FAILSAFE = True#Move the mouse to the upper left corner to exi
#Screen stuff
#print(pyautogui.size())
width, height = pyautogui.size()

#Mouse stuff
MouseX, MouseY = pyautogui.position()

#Pause /Safty features
pyautogui.PAUSE = 0.1; 

ser = serial.Serial(serial_port, baud_rate)
#The Information function to print all button uses
def info():
	print('OPEN/CLOSE: Terminate the whole programm by exit()')
	print('Start: Activates/deactivates Remote Control of Mouse')
	print('Triangle: Display Turtle shape')
	print('Up arrow: Up')
	print('Down arrrow: Down')
	print('Left arrow: Left')
	print('Right arrrow: Right')
	print('SLOW/Left: Reduce the movement speed by half')
	print('SLOW/Right: Increases the movement speed by double')
	print('Display: Shows this information again in the terminal')
	
	
cont_val=False;
move_speed=1/150;
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
		
#KeyBoard/Mouse Control
    #Modus de/activation
	if(signal_to_int[line]==signal_to_int[button_to_signal['START']]):
		cont_val = not cont_val#Display
		print('The Control is in the remote:'+str(cont_val))
	if(cont_val==True):
	#MousePointer movement speed adjustment
		if(signal_to_int[line]==signal_to_int[button_to_signal['SLOW/Left']]):
			move_speed=move_speed*0.5;print('Move Speed(without Keanu ):'+str(int(move_speed*150*100)))
			
		if(signal_to_int[line]==signal_to_int[button_to_signal['SLOW/Right']]):
			move_speed=move_speed*2;print('Move Speed(without Keanu ):'+str(int(move_speed*150*100)))
	#Mouse Movement
		if(signal_to_int[line]==signal_to_int[button_to_signal['Left arrow']]):
			pyautogui.moveRel(-int(width*move_speed),0 )
		if(signal_to_int[line]==signal_to_int[button_to_signal['Right arrow']]):
			pyautogui.moveRel(int(width*move_speed),0 )
		if(signal_to_int[line]==signal_to_int[button_to_signal['Up arrow']]):
			pyautogui.moveRel(0,-int(height*move_speed) )
		if(signal_to_int[line]==signal_to_int[button_to_signal['Down arrow']]):
			pyautogui.moveRel(0,int(height*move_speed) )
	#Mouse buttton actions
		if(signal_to_int[line]==signal_to_int[button_to_signal['Circle']]):
			pyautogui.click(button='right');
		if(signal_to_int[line]==signal_to_int[button_to_signal['X']]):
			pyautogui.click(button='middle');
		if(signal_to_int[line]==signal_to_int[button_to_signal['ENTER']]):
			pyautogui.click(button='left');

