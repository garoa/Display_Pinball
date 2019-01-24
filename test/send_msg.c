#include <SerialPort.h>

SerialPort serial_port("/dev/ttyUSB0");

int main(){
  serial_port.Open();
  serial_port.SetBaudRate(SerialPort::BAUD_19200);

	char msg1[29] = "  ABOBRINHA BLAH BLAH BLAH  ";
	char msg2[29] = "       HACKERSPACE SP       ";

	int i;
	serial_port.WriteByte('M');

	for (i=0;i<28;i++){
		serial_port.WriteByte(msg1[i]);
	}

	for (i=0;i<28;i++){
		serial_port.WriteByte(msg2[i]);
	}

	return 0;
}
