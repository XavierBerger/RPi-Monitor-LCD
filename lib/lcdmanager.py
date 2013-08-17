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
# 
#
###########################################################################
import pcd8544.lcd as lcd
#import fakelib as lcd

class Singleton(object):
  class __Singleton:

    def __init__(self):
      self.contrast = 0xaa
      self.brightness = 256

    def lightup(self):
      self.brightness +=10
      lcd.set_brightness(self.brightness)
      
    def lightdown(self):
      self.brightness -=10
      lcd.set_brightness(self.brightness)
      
    def contrastup(self):
      self.contrast +=1
      lcd.set_contrast(self.contrast)
      
    def contrastdown(self):
      self.contrast -=1
      lcd.set_contrast(self.contrast)
      
  instance = None

  def __new__(c):
    if not Singleton.instance:
      Singleton.instance = Singleton.__Singleton()
    return Singleton.instance

def lightup():
  singleton = Singleton()
  return singleton.lightup()

def lightdown():
  singleton = Singleton()
  return singleton.lightdown()

def contrastup():
  singleton = Singleton()
  return singleton.contrastup()

def contrastdown():
  singleton = Singleton()
  return singleton.contrastdown()
  
if __name__ == '__main__':
  print "No test defind for this module"
  pass
 
