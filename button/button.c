#include <avr/io.h>

void main(){
	// button -> PB0
	// led    -> PD7


	DDRD  |= 0b10000000;
	DDRB  &= 0b11111110;
	PORTB |= 0b00000001;

	
/*

	
	
	DDRA = 0x00;
	DDRB = 0x00;
	PORTA = 0xFF;
	PORTB = 0xFF;
	DDRC = 0xFF;

	unsigned char a = PINA;
	unsigned char b = PINB;

	unsigned char c = a + b;	

	PORTC = c;

*/	

	while(1){
		unsigned char var = PINB;
		if(var & 0x01){ // 1 // 0b00000001
			PORTD |= 0b10000000;
		} else {
			PORTD &= ~0b10000000;
		}
	}

}
