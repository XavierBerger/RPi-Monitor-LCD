#RPi-Monitor-LCD

Development still in progress. Repository not ready yet for fork...

## Introduction
**RPi-Monitor-LCD** is designed to display information extracted from [**RPi-Monitor**](https://github.com/XavierBerger/RPi-Monitor) into a [**pcd8544**](https://github.com/XavierBerger/pcd8544) LCD.

**RPi-Monitor-LCD** is architectured around a finite state machine powered by [fysom](https://github.com/mriehl/fysom). The configuration of the state machine highly configurable and is stored into a configuration file.
The configuration file will call additionnal libraries to perform action.

The project is entended to be a framework easily customizable and not a fully packaged solution. Using **RPi-Monitor-LCD ** will certainly require some customization and adaptation.

In this repository **RPi-Monitor-LCD** is provided with a working example showing the possibilities offered by finite state machine engine implementation. 


## Installation

Dependencies:
  * sudo apt-get install python-dev python-imaging python-imaging-tk python-pip
  * sudo pip install wiringpi2
  * sudo pip install fysom
  * sudo pip install spidev

  git clone https://github.com/XavierBerger/pcd8544.git
  cd pcd8544
  ./setup clean build
  sudo ./setup install

  Remove i2c from blacklist

  Add i2c-dev in /etc/modules
  
  Reboot or execute gpio load i2c
  
  
