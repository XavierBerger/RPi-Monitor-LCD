#!/usr/bin/env python
import sys, os, pprint
import array
 
class Configuration(object):
  def __init__(self):
    self.toto = {'initial': 'green',
                     'events': [
                         {'name': 'up',    'src': 'green', 'dst': 'green'},
                         {'name': 'down',  'src': 'green', 'dst': 'green'},
                         {'name': 'left',  'src': 'green', 'dst': 'green'},
                         {'name': 'right', 'src': 'green', 'dst': 'green'},
                         {'name': 'enter', 'src': 'green', 'dst': 'green'}],
                }
    self.smc = {}

  def load(self, filename):
    with open(filename, 'r') as f:
      for line in f:
        line = line.replace('\n','')
        if (len(line) == 0) or (line[0] == '#') : continue
        #print line
        (key, value) = line.split('=') 
        leaves = key.split('.')




if __name__ == "__main__":
  configuration = Configuration()
  configuration.load('../rpimonitorlcd.conf')
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(configuration.toto)

'''
    chomp;
    /^\s*#|^$/ and next;                 # Ignore comments
    my ($key, $value) = /^([^=]*)=(.*)/; # Extract key and value
    my @leaves=split('\.', $key);        # Explode key and construct config hash
    my $tree=$this;
    my $current;
    my $next;
    while (scalar(@leaves) > 0) {
      $current ||= shift (@leaves);
      $next = shift (@leaves);
      if ( $next =~ /^\d+$/ ) {
        if ($current =~ /^\d+$/) {
          @{$tree}[$current-1] ||= [];
          $tree=@{$tree}[$current-1];
        }
        else {
          $tree->{$current} ||= [];
          $tree=$tree->{$current};
        }
      } else {
        if ($current =~ /^\d+$/) {
          @{$tree}[$current-1] ||= {};
          $tree=@{$tree}[$current-1];
        }
        else {
          $tree->{$current} ||= {};
          $tree=$tree->{$current};
        }
      }      
      if ( ($next eq 'rrd') and $value) { push(@{$this->{'rrd'}},$tree) };
      $current = $next;
    }
    if ($current =~ /^\d+$/) {
      @{$tree}[$current-1] = $value;
    }
    else {
      $tree->{$current} = $value;
    }
'''
