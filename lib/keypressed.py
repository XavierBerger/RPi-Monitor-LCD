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
###########################################################################
#
# This module is a skeleton that can be used to customize RPi-Monitor-LCD 
#
###########################################################################
import pcd8544.lcd as lcd
#import fakelib as lcd

class Singleton(object):
  class __Singleton:

    def __init__(self):
      pass

    def onup(self):
      lcd.cls()
      lcd.centre_text(0,'RPi-Monitor')
      lcd.centre_text(3,'key up')

    def ondown(self):
      lcd.cls()
      lcd.centre_text(0,'RPi-Monitor')
      lcd.centre_text(3,'key down')

    def onleft(self):
      lcd.cls()
      lcd.centre_text(0,'RPi-Monitor')
      lcd.centre_text(3,'key left')

    def onright(self):
      lcd.cls()
      lcd.centre_text(0,'RPi-Monitor')
      lcd.centre_text(3,'key right')

    def onenter(self):
      lcd.cls()
      lcd.centre_text(0,'RPi-Monitor')
      lcd.centre_text(3,'key enter')

  instance = None

  def __new__(c):
    if not Singleton.instance:
      Singleton.instance = Singleton.__Singleton()
    return Singleton.instance

def onup():
  singleton = Singleton()
  return singleton.onup()

def ondown():
  singleton = Singleton()
  return singleton.ondown()

def onleft():
  singleton = Singleton()
  return singleton.onleft()

def onright():
  singleton = Singleton()
  return singleton.onright()

def onenter():
  singleton = Singleton()
  return singleton.onenter()

  
if __name__ == '__main__':
  aResult = aFunction()
  print aResult

 
