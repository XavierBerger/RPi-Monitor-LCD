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
# rpimonitordm (RPi-Monitor Data Miner) is a plugin for RPi-Monitor-LCD
# designed to extract and make available current data from RPi-Monitor.
# To decrease server load, rpimonitordm will only query the server is
# cached data are too old.
#
import time, httplib, json

class RPM(object):
  class __Singleton:

    def __init__(self):
      self.val = None
      self.lastUpdate = 0

    def __str__(self):
      return `self` + self.val
   
    def getData(self):
      if (time.time() - self.lastUpdate ) >  10:
        print "********** Get data from server **********"
        connection = httplib.HTTPConnection("localhost", 8888)
        connection.request("GET","/dynamic.json")
        response = connection.getresponse()
        if ( response.status == 200 ):
          self.data = json.loads(response.read())
        connection.close()
        self.lastUpdate=time.time()
      return self.data

  instance = None

  def __new__(c):
    if not RPM.instance:
      RPM.instance = RPM.__Singleton()
    return RPM.instance

def getData():
  rpm = RPM()
  return rpm.getData()
  
if __name__ == '__main__':
  while True:
    data = getData()
    print data['uptime']
    time.sleep(3.5);

 
