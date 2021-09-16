# avr-spbu-public

`usermod -aG dialout <username>`

```
avr-gcc -g -std=c99 -O1 -mmcu=atmega328p -o out.elf example.c
avrdude -v -patmega328p -P /dev/ttyACM0 -c arduino -U flash:w:"out.elf"
```
