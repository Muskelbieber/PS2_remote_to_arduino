# This my change acording to your set-up.
#you can see your port at the right lower corner of the Arduino IDE
serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
#write_to_file_path = "output.dat";

#Button assingment in dex from hex
button_to_signal = {'OPEN/CLOSE':'0x68B5B\r\n',\
 'RESET':'0xA8B5B\r\n',\
 'AUDIO with 2 F':'0x26B92\r\n',\
 'SHUFFLE':'0xACB92\r\n',\
 '1':'0xB92\r\n',\
 '2':'0x80B92\r\n',\
 '3':'0x40B92\r\n',\
 'ANGLE':'0xA6B92\r\n',\
 'PROGRAM':'0xF8B92\r\n',\
 '4':'0xC0B92\r\n',\
 '5':'0x20B92\r\n',\
 '6':'0xA0B92\r\n',\
 'SUBTITLE':'0xC6B92\r\n',\
 'REPEAT':'0x34B92\r\n',\
 '7':'0x60B92\r\n',\
 '8':'0xE0B92\r\n',\
 '9':'0x10B92\r\n',\
 'SLOW/Left':'0x6B92\r\n',\
 'SLOW/Right':'0x86B92\r\n',\
 'CLEAR':'0xF0B92\r\n',\
 '0':'0x90B92\r\n',\
 'TIME':'0x14B92\r\n',\
 'SCAN/Left':'0xCCB92\r\n',\
 'SCAN/Right':'0x2CB92\r\n',\
 'PREV':'0xCB92\r\n',\
 'NEXT':'0x8CB92\r\n',\
 'A-B':'0x54B92\r\n',\

 'PLAY':'0x4CB92\r\n',\
 'PAUSE':'0x9CB92\r\n',\
 'STOP':'0x1CB92\r\n',\
 'DISPLAY':'0x2AB92\r\n',\
 'TOP MENU':'0x58B92\r\n',\
 'MENU':'0xD8B92\r\n',\
 'RETURN':'0x70B92\r\n',\
 'Triangle':'0x3AB5B\r\n',\
 'Up arrow':'0x9EB92\r\n',\
 'Circle':'0xBAB5B\r\n',\
 'Left arrow':'0xDEB92\r\n',\
 'ENTER':'0xD0B92\r\n',\
 'Right arrow':'0x3EB92\r\n',\
 'Square':'0xFAB5B\r\n',\
 'Down arrow':'0x5EB92\r\n',\
 'X':'0x7AB5B\r\n',\
 'L1':'0x5AB5B\r\n',\
 'L3':'0x8AB5B\r\n',\
 'R3':'0x4AB5B\r\n',\
 'R1':'0xDAB5B\r\n',\
 'L2':'0x1AB5B\r\n',\
 'SELECT':'0xAB5B\r\n',\
 'START':'0xCAB5B\r\n',\
 'R2':'0x9AB5B\r\n',\
 'Repeat':'0xFFFFFFFF\r\n',\
};

signal_to_int = {'0x68B5B\r\n':int('0x68B5B', 0),\
'0xA8B5B\r\n': int('0xA8B5B', 0),\
'0x26B92\r\n': int('0x26B92', 0),\
'0xACB92\r\n': int('0xACB92', 0),\
'0xB92\r\n': int('0xB92', 0),\
'0x80B92\r\n': int('0x80B92', 0),\
'0x40B92\r\n': int('0x40B92', 0),\
'0xA6B92\r\n': int('0xA6B92', 0),\
'0xF8B92\r\n': int('0xF8B92', 0),\
'0xC0B92\r\n': int('0xC0B92', 0),\
'0x20B92\r\n': int('0x20B92', 0),\
'0xA0B92\r\n': int('0xA0B92', 0),\
'0xC6B92\r\n': int('0xC6B92', 0),\
'0x34B92\r\n': int('0x34B92', 0),\
'0x60B92\r\n': int('0x60B92', 0),\
'0xE0B92\r\n': int('0xE0B92', 0),\
'0x10B92\r\n': int('0x10B92', 0),\
'0x6B92\r\n': int('0x6B92', 0),\
'0x86B92\r\n': int('0x86B92', 0),\
'0xF0B92\r\n': int('0xF0B92', 0),\
'0x90B92\r\n': int('0x90B92', 0),\
'0x14B92\r\n': int('0x14B92', 0),\
'0xCCB92\r\n': int('0xCCB92', 0),\
'0x2CB92\r\n': int('0x2CB92', 0),\
'0xCB92\r\n': int('0xCB92', 0),\
'0x8CB92\r\n': int('0x8CB92', 0),\
'0x54B92\r\n': int('0x54B92', 0),\

'0x4CB92\r\n': int('0x4CB92', 0),\
'0x9CB92\r\n': int('0x9CB92', 0),\
'0x1CB92\r\n': int('0x1CB92', 0),\
'0x2AB92\r\n': int('0x2AB92', 0),\
'0x58B92\r\n': int('0x58B92', 0),\
'0xD8B92\r\n': int('0xD8B92', 0),\
'0x70B92\r\n': int('0x70B92', 0),\
'0x3AB5B\r\n': int('0x3AB5B', 0),\
'0x9EB92\r\n': int('0x9EB92', 0),\
'0xBAB5B\r\n': int('0xBAB5B', 0),\
'0xDEB92\r\n': int('0xDEB92', 0),\
'0xD0B92\r\n': int('0xD0B92', 0),\
'0x3EB92\r\n': int('0x3EB92', 0),\
'0xFAB5B\r\n': int('0xFAB5B', 0),\
'0x5EB92\r\n': int('0x5EB92', 0),\
'0x7AB5B\r\n': int('0x7AB5B', 0),\
'0x5AB5B\r\n': int('0x5AB5B', 0),\
'0x8AB5B\r\n': int('0x8AB5B', 0),\
'0x4AB5B\r\n': int('0x4AB5B', 0),\
'0xDAB5B\r\n': int('0xDAB5B', 0),\
'0x1AB5B\r\n': int('0x1AB5B', 0),\
'0xAB5B\r\n': int('0xAB5B', 0),\
'0xCAB5B\r\n': int('0xCAB5B', 0),\
'0x9AB5B\r\n': int('0x9AB5B', 0),\
'0xFFFFFFFF\r\n': int('0xFFFFFFFF', 0),\
};

signal_to_button = {'0x68B5B\r\n': 'OPEN/CLOSE',\
'0xA8B5B\r\n': 'RESET',\
'0x26B92\r\n': 'AUDIO with 2 F',\
'0xACB92\r\n': 'SHUFFLE',\
'0xB92\r\n': '1',\
'0x80B92\r\n': '2',\
'0x40B92\r\n': '3',\
'0xA6B92\r\n': 'ANGLE',\
'0xF8B92\r\n': 'PROGRAM',\
'0xC0B92\r\n': '4',\
'0x20B92\r\n': '5',\
'0xA0B92\r\n': '6',\
'0xC6B92\r\n': 'SUBTITLE',\
'0x34B92\r\n': 'REPEAT',\
'0x60B92\r\n': '7',\
'0xE0B92\r\n': '8',\
'0x10B92\r\n': '9',\
'0x6B92\r\n': 'SLOW/Left',\
'0x86B92\r\n': 'SLOW/Right',\
'0xF0B92\r\n': 'CLEAR',\
'0x90B92\r\n': '0',\
'0x14B92\r\n': 'TIME',\
'0xCCB92\r\n': 'SCAN/Left',\
'0x2CB92\r\n': 'SCAN/Right',\
'0xCB92\r\n': 'PREV',\
'0x8CB92\r\n': 'NEXT',\
'0x54B92\r\n': 'A-B',\

'0x4CB92\r\n': 'PLAY',\
'0x9CB92\r\n': 'PAUSE',\
'0x1CB92\r\n': 'STOP',\
'0x2AB92\r\n': 'DISPLAY',\
'0x58B92\r\n': 'TOP MENU',\
'0xD8B92\r\n': 'MENU',\
'0x70B92\r\n': 'RETURN',\
'0x3AB5B\r\n': 'Triangle',\
'0x9EB92\r\n': 'Up arrow',\
'0xBAB5B\r\n': 'Circle',\
'0xDEB92\r\n': 'Left arrow',\
'0xD0B92\r\n': 'ENTER',\
'0x3EB92\r\n': 'Right arrow',\
'0xFAB5B\r\n': 'Square',\
'0x5EB92\r\n': 'Down arrow',\
'0x7AB5B\r\n': 'X ',\
'0x5AB5B\r\n': 'L1',\
'0x8AB5B\r\n': 'L3',\
'0x4AB5B\r\n': 'R3',\
'0xDAB5B\r\n': 'R1',\
'0x1AB5B\r\n': 'L2',\
'0xAB5B\r\n': 'SELECT',\
'0xCAB5B\r\n': 'START',\
'0x9AB5B\r\n': 'R2',\
'0xFFFFFFFF\r\n': 'R2',\
};
