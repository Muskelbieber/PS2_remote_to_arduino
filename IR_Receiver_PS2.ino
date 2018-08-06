
#include "IRremote.h"

int receiver = 11; // Signal Pin of IR receiver to Arduino Digital Pin 11

/*-----( Declare objects )-----*/
IRrecv irrecv(receiver);     // create instance of 'irrecv'
decode_results results;      // create instance of 'decode_results'

/*-----( Function )-----*/
void translateIR() // takes action based on IR code received

/*-----(Binary code of PS2 remote scph-10420)----
 * found with ir decoder but after pressing a button a diffrent
 * of FFFFFFF repeats are send, maybe because the remote also
 * tells a length of button presses as needed for movement 
 * controller like a ps2 controler

68B5B OPEN/CLOSE with 2 F
A8B5B RESET with 2 F
26B92 AUDIO with 2 F
ACB92 SHUFFLE 
B92 1
80B92 2
40B92 3
A6B92 ANGLE
F8B92 PROGRAM
C0B92 4
20B92 5
A0B92 6
C6B92 SUBTITLE
34B92 REPEAT
60B92 7
E0B92 8
10B92 9
6B92 SLOW/Left
86B92 SLOW/Right
F0B92 CLEAR
90B92 0
14B92 TIME
CCB92 SCAN/Left
2CB92 SCAN/Right
CB92 PREV
8CB92 NEXT
54B92 A-B

4CB92 PLAY
9CB92 PAUSE
1CB92 STOP
2AB92 DISPLAY
58B92 TOP MENU
D8B92 MENU
70B92 RETURN
3AB5B Triangle
9EB92 Up arrow 5 F
BAB5B Circle
DEB92 Left arrow
D0B92 ENTER
3EB92 Right arrow
FAB5B Square
5EB92 Down arrow
7AB5B X 
5AB5B L1
8AB5B L3
4AB5B R3
DAB5B R1
1AB5B L2
AB5B SELECT
CAB5B START
9AB5B R2
*/
// describing Remote IR codes 

{

  switch(results.value)

  {
    case 0x68B5B:Serial.println("0x68B5B"); break;// with 2 F
    case 0xA8B5B: Serial.println("0xA8B5B"); break;//with 2 F
    case 0x26B92 : Serial.println("0x26B92"); break;//with 2 F
    case 0xACB92 : Serial.println("0xACB92"); break;
    case 0xB92: Serial.println("0xB92"); break;
    case 0x80B92: Serial.println("0x80B92"); break;
    case 0x40B92: Serial.println("0x40B92"); break;
    case 0xA6B92: Serial.println("0xA6B92"); break;
    case 0xF8B92:Serial.println("0xF8B92"); break;
    case 0xC0B92: Serial.println("0xC0B92"); break;
    case 0x20B92: Serial.println("0x20B92"); break;
    case 0xA0B92: Serial.println("0xA0B92"); break;
    case 0xC6B92: Serial.println("0xC6B92"); break;
    case 0x34B92: Serial.println("0x34B92"); break;
    case 0x60B92: Serial.println("0x60B92"); break;
    case 0xE0B92: Serial.println("0xE0B92"); break;
    case 0x10B92: Serial.println("0x10B92"); break;
    case 0x6B92: Serial.println("0x6B92"); break;
    case 0x86B92: Serial.println("0x86B92"); break;
    case 0xF0B92: Serial.println("0xF0B92"); break;
    case 0x90B92: Serial.println("0x90B92"); break;
    case 0x14B92: Serial.println("0x14B92"); break;
    case 0xCCB92: Serial.println("0xCCB92"); break;
    case 0x2CB92: Serial.println("0x2CB92"); break;
    case 0xCB92: Serial.println("0xCB92"); break;
    case 0x8CB92: Serial.println("0x8CB92"); break;
    case 0x54B92: Serial.println("0x54B92"); break;

    case 0x4CB92: Serial.println("0x4CB92"); break;
    case 0x9CB92: Serial.println("0x9CB92"); break;
    case 0x1CB92: Serial.println("0x1CB92"); break;
    case 0x2AB92: Serial.println("0x2AB92"); break;
    case 0x58B92: Serial.println("0x58B92"); break;
    case 0xD8B92: Serial.println("0xD8B92"); break;
    case 0x70B92: Serial.println("0x70B92"); break;
    case 0x3AB5B: Serial.println("0x3AB5B"); break;
    case 0x9EB92: Serial.println("0x9EB92"); break;//5 F
    case 0xBAB5B: Serial.println("0xBAB5B"); break;
    case 0xDEB92: Serial.println("0xDEB92"); break;
    case 0xD0B92: Serial.println("0xD0B92"); break;
    case 0x3EB92: Serial.println("0x3EB92"); break;
    case 0xFAB5B: Serial.println("0xFAB5B"); break;
    case 0x5EB92: Serial.println("0x5EB92"); break;
    case 0x7AB5B: Serial.println("0x7AB5B"); break;
    case 0x5AB5B: Serial.println("0x5AB5B"); break;
    case 0x8AB5B: Serial.println("0x8AB5B"); break;
    case 0x4AB5B: Serial.println("0x4AB5B"); break;
    case 0xDAB5B: Serial.println("0xDAB5B"); break;
    case 0x1AB5B: Serial.println("0x1AB5B"); break;
    case 0xAB5B: Serial.println("0xAB5B"); break;
    case 0xCAB5B: Serial.println("0xCAB5B"); break;
    case 0x9AB5B: Serial.println("0x9AB5B"); break;
  
 // default: 
   // Serial.println(" other button   ");

  }// End Case

  delay(50); // Do not get immediate repeat


} //END translateIR
void setup()   /*----( SETUP: RUNS ONCE )----*/
{
  Serial.begin(9600);
  //Serial.println("IR Receiver Button Decode"); 
  irrecv.enableIRIn(); // Start the receiver

}/*--(end setup )---*/


void loop()   /*----( LOOP: RUNS CONSTANTLY )----*/
{
  if (irrecv.decode(&results)) // have we received an IR signal?

  {
    translateIR(); 
    irrecv.resume(); // receive the next value
  }  
}/* --(end main loop )-- */


