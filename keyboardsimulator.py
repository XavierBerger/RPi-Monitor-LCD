#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is designed to (with the corrrect wiring) simulate
# key pressing on electronique assembly.
# This could be usefull if like me, you have plenty of GPIO thanks
# to mcp23017 and miss some switch for test.
#
import termios, fcntl, sys, os, time
import wiringpi2 as wiringpi
if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

# Define constants
INPUT, OUTPUT = LOW, HIGH = OFF, ON = [0, 1]
UP,DOWN,RIGHT,LEFT,ENTER = BUTTONS = [8,9,10,11,12]
PIN_BASE = 64
I2C_ADDR = 0x20
DELAY = 0.1

def initialize():
  # Initialize wiringpi
  wiringpi.wiringPiSetup()
  wiringpi.mcp23017Setup(PIN_BASE, I2C_ADDR)
  for button in BUTTONS:
    wiringpi.pinMode(PIN_BASE + button, OUTPUT)
    wiringpi.digitalWrite(PIN_BASE + button,ON)

def onup():
  print "UP (%d)" % (PIN_BASE + UP)
  wiringpi.digitalWrite(PIN_BASE + UP,OFF)
  time.sleep(DELAY)
  wiringpi.digitalWrite(PIN_BASE + UP,ON)

def ondown():
  print "DOWN (%d)" % (PIN_BASE + DOWN)
  wiringpi.digitalWrite(PIN_BASE + DOWN,OFF)
  time.sleep(DELAY)
  wiringpi.digitalWrite(PIN_BASE + DOWN,ON)

def onright():
  print "RIGHT (%d)" % (PIN_BASE + RIGHT)
  wiringpi.digitalWrite(PIN_BASE + RIGHT,OFF)
  time.sleep(DELAY)
  wiringpi.digitalWrite(PIN_BASE + RIGHT,ON)

def onleft():
  print "LEFT (%d)" % (PIN_BASE + LEFT)
  wiringpi.digitalWrite(PIN_BASE + LEFT,OFF)
  time.sleep(DELAY)
  wiringpi.digitalWrite(PIN_BASE + LEFT,ON)

def onenter():
  print "ENTER (%d)" % (PIN_BASE + ENTER)
  wiringpi.digitalWrite(PIN_BASE + ENTER,OFF)
  time.sleep(DELAY)
  wiringpi.digitalWrite(PIN_BASE + ENTER,ON)

def keypressed():
  fd = sys.stdin.fileno()

  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

  combo = [ 0 , 0 , 0]
  try:
    while 1:
      try:
        c = sys.stdin.read(1)
        combo.pop(0)
        combo.append(c)
        if combo[2] == '\n': onenter()
        if (combo[0] == '\x1b') and (combo[1] == '['):
          if combo[2] == 'A': onup()
          if combo[2] == 'B': ondown()
          if combo[2] == 'C': onright()
          if combo[2] == 'D': onleft()
      except IOError: pass
  except KeyboardInterrupt:
    pass
  finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

if __name__ == "__main__":
  initialize()
  keypressed()
