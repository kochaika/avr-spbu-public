#ifndef F_CPU
#define F_CPU 16000000UL
#endif


#include <avr/io.h>
#include <util/delay.h>


int main(){


	// PB4
	//01111010
	//xxxxxxxx
	//76543210
//	DDRB = 0xFF; // 0b11111111
	DDRB |= 0b00000001; // DDRB = DDRB | 0b00010000;


	while(1){
	//xxxxx1xx
//	PORTB = 0xFF;
	PORTB |= 0b00000001;
	_delay_ms(250);
	PORTB &= ~0b00000001; //PORTB = PORTB & 0b11101111
	_delay_ms(250);
	// delay
	// turn of led
	// delay

	}


}
