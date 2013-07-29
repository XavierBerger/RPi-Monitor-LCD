#!/usr/bin/env python
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

if __name__ == "__main__":
  configuration = Configuration()
  configuration.load('../rpimonitorlcd.conf')
  pp = pprint.PrettyPrinter(indent=4)
  print "=== configuration.data ==="
  pp.pprint(configuration.data)
  print "=== configuration.data['fsm']['initial'] ==="
  pp.pprint(configuration.data['fsm']['initial'])
  print "=== configuration.data['fsm']['events'] ==="
  pp.pprint(configuration.data['fsm']['events'])
  
