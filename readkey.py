#!/usr/bin/env python
#
# Copyright 2013 - Xavier Berger - http://rpi-experiences.blogspot.fr/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import wiringpi2 as wiringpi
import pcd8544.lcd as lcd

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

lcd.init()

try:
  while 1:
    for index,button in enumerate(BUTTONS):
      button_state = wiringpi.digitalRead(PIN_BASE + button)
      if button_state == OFF:
        print "button (%d) %d = %d" % (PIN_BASE + button, index, button_state)
      wiringpi.delay(20)
except KeyboardInterrupt:
  pass

