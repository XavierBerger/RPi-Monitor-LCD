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
#import pcd8544.lcd as lcd
import fakelib as lcd

class Singleton(object):
  class __Singleton:

    def __init__(self):
      self.aValue = "a value"

    def onup(self,caller):
      lcd.cls()
      caller.lightOn()
      lcd.centre_text(3,'key up')

    def ondown(self,caller):
      lcd.cls()
      caller.lightOn()
      lcd.centre_text(3,'key down')

    def onleft(self,caller):
      lcd.cls()
      caller.lightOn()
      lcd.centre_text(3,'key left')

    def onright(self,caller):
      lcd.cls()
      caller.lightOn()
      lcd.centre_text(3,'key right')

    def onenter(self,caller):
      lcd.cls()
      caller.lightOn()
      lcd.centre_text(3,'key enter')

  instance = None

  def __new__(c):
    if not Singleton.instance:
      Singleton.instance = Singleton.__Singleton()
    return Singleton.instance

def onup(caller):
  singleton = Singleton()
  return singleton.onup(caller)

def ondown(caller):
  singleton = Singleton()
  return singleton.ondown(caller)

def onleft(caller):
  singleton = Singleton()
  return singleton.onleft(caller)

def onright(caller):
  singleton = Singleton()
  return singleton.onright(caller)

def onenter(caller):
  singleton = Singleton()
  return singleton.onenter(caller)

  
if __name__ == '__main__':
  aResult = aFunction()
  print aResult

 
