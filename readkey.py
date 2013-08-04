#!/usr/bin/env python
import wiringpi2 as wiringpi

# Define constants
INPUT, OUTPUT = LOW, HIGH = OFF, ON = [0, 1]
BUTTONS = [0,1,2,3,4]
PIN_BASE = 64
I2C_ADDR = 0x20
PUD_UP=2

wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(PIN_BASE,I2C_ADDR)


for button in BUTTONS:
  wiringpi.pinMode(PIN_BASE + button,INPUT)
  wiringpi.pullUpDnControl(PIN_BASE + button,PUD_UP)

while 1:
  for index,button in enumerate(BUTTONS):
    button_state = wiringpi.digitalRead(PIN_BASE + button)
    if button_state == OFF:
      print "button (%d) %d = %d" % (PIN_BASE + button, index, button_state)
    wiringpi.delay(20)
