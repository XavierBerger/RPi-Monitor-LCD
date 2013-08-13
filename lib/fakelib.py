########################################################################
# Fake library used to develop RPi-Monitor-LCD in Ubuntu
########################################################################
def wiringPiSetup():
  print "wiringPiSetup()"
    
def mcp23017Setup(PIN_BASE,I2C_ADDR):
  print "mcp23017Setup"

def pinMode(PIN_BASE,INPUT):
  print "pinMode"
  
def pullUpDnControl(PIN_BASE,PUD_UP):
  print "pullUpDnControl"
  
def init():
  print "init"

def cls():
  print "cls"
  
def backlight(value):
  print "backlight %d " % value

def digitalRead(button):
  pass
  
def delay(delay):
  pass

def centre_text(raw,text):
  print "[%d] %s" % (raw,text)

def load_bitmap(bitmap):  
  print "loadbitmap %s" % bitmap

def gotorc(r,c):
  print "gotorc (%d,%d)" % ( r, c )

def text(value):
  print "text"

def set_brightness(value):
  print "led: %d" % value

def set_contrast(value):
  print "set_contrast: %d" % value
