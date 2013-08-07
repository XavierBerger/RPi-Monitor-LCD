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

import sys, os, pprint
import array

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
 
class Configuration(object):
  def __init__(self):
    pass

  def load(self, filename):
    self.data = {}
    with open(filename, 'r') as f:
      for line in f:
        line = line.replace('\n','')
        if (len(line) == 0) or (line[0] == '#') : continue
        (key, value) = line.split('=') 
        leaves = key.split('.')
        prevleaf = None
        tree=self.data
        for currentleaf in leaves:
          if prevleaf == None:
            prevleaf = currentleaf
            continue
          if is_number(prevleaf):
            prevleaf=int(prevleaf)
          if is_number(currentleaf):
            try:
              tree[prevleaf]
            except:
              try:
                tree[prevleaf]=[]
              except:
                tree[prevleaf].append([])
          else:
            try:
              tree[prevleaf]
            except:
              try:
                tree[prevleaf]={}
              except:
                tree.append({})
          tree=tree[prevleaf]
          prevleaf = currentleaf
        
        if is_number(currentleaf):
          currentleaf = int(currentleaf)
          tree.append(value)
        else:
          tree[currentleaf] = value
        
    #Process fsm configuration and look for "action"
    backtolist={}
    for event in self.data['fsm']['events']:
      if event['dst'] == 'action':
         backtolist[event['src']]="backto%s"% event['src']
    for dst,name in backtolist.items():
      self.data['fsm']['events'].append( { 'name':name, 'src':'action', 'dst':dst  } )

    #Process autorefresh parameter
    autorefresh=[]
    for name,desc in self.data['pages'].items():
      try:
        autorefresh.append(name)
      except:
        pass
    for name in autorefresh:
      self.data['fsm']['events'].append( { 'name':'refresh', 'src':name, 'dst':'refresh'  } )
      self.data['fsm']['events'].append( { 'name':"backto%s" % name, 'src':'refresh', 'dst':name  } )
      

  def printConfiguration(self):
    pp = pprint.PrettyPrinter(indent=2,width=100)
    #print "=== configuration.data['pages'] ==="
    #pp.pprint(self.data['pages'])
    #print "=== configuration.data['fsm']['initial'] ==="
    #pp.pprint(self.data['fsm']['initial'])
    #print "=== configuration.data['fsm']['events'] ==="
    #pp.pprint(self.data['fsm']['events'])
    #print "=== configuration.data['modules'] ==="
    #pp.pprint(self.data['modules'])
    print "=== configuration.data ==="
    pp.pprint(self.data)

if __name__ == "__main__":
  configuration = Configuration()
  configuration.load('./rpimonitorlcd.conf')
  configuration.printConfiguration()
