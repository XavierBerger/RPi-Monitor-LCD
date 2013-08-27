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

class Singleton(object):
  class __Singleton:

    def __init__(self):
      self.aValue = "a value"

    def aFunction(self):
      # Implement a function here and return a value
      return self.aValue

  instance = None

  def __new__(c):
    if not Singleton.instance:
      Singleton.instance = Singleton.__Singleton()
    return Singleton.instance

# Define the function callable by the state machine
def aFunction():
  # Get Singleton
  singleton = Singleton()
  # Execute the associated funtion and return its result
  return singleton.aFunction()
  
if __name__ == '__main__':
  aResult = aFunction()
  print aResult

 
