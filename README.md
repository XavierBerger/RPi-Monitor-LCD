RPi-Monitor-LCD
===============

Development repository not ready yet for fork...

Dependencies:
  sudo apt-get install python-dev python-imaging python-imaging-tk python-pip
  sudo pip install wiringpi
  sudo pip install fysom
  sudo pip install spidev

  git clone https://github.com/XavierBerger/pcd8544.git
  cd pcd8544
  ./setup clean build
  sudo ./setup install

  gpio load i2c
