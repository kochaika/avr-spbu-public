
// E    -> PC1
// RS   -> PC0
// DATA -> PORTD



void send_cmd(unsigned char cmd){

//	RS = 0;
	PORTC &= 0b11111110;

//	E = 1;
	PORTC |= 0b00000010;

	// DATA = cmd;
	PORTD = cmd;

//	E = 0;
	PORTC &= ~0b00000010;

	_delay_us(50);
}




void lcd_init(){
	send_cmd(0b00001100);
	_delay_us(20);
	send_cmd(0b00000110);
	_delay_us(40);
}


int main(){



// port init
 lcd_init();

char *str = "hello";
	for(int i=0; str[i]; i++)
		send_data(str[i]);

send_cmd(0b00100000);


}
