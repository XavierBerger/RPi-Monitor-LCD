#[RPi-Monitor-LCD](http://rpi-experiences.blogspot.fr/)

###Development still in progress. Repository not ready yet for fork...

## Introduction
**RPi-Monitor-LCD** is designed to display information extracted from [**RPi-Monitor**](https://github.com/XavierBerger/RPi-Monitor) into a [**pcd8544**](https://github.com/XavierBerger/pcd8544) LCD.
5 buttons connected to the Raspberry Pi through i2c bus and MCP23008 chip come in addition to the assembly presented into [**pcd8544**](https://github.com/XavierBerger/pcd8544) project. These 5 buttons are interpreted by **RPi-Monitor-LCD** as UP, DOWN, LEFT, RIGHT and ENTER.

**RPi-Monitor-LCD** is architectured around a finite state machine powered by [fysom](https://github.com/mriehl/fysom). The state machine behavior is highly configurable and stored into a configuration file. The configuration file will call additionnal libraries to perform custom actions.

The project is entended to be a framework easily customizable and not a fully packaged solution. Using **RPi-Monitor-LCD** will certainly require some customization and adaptation.

In this repository **RPi-Monitor-LCD** is provided with a working example showing the possibilities offered by finite state machine engine implementation. 

## Electronic assembly

In the [doc](https://github.com/XavierBerger/RPi-Monitor-LCD/tree/master/doc) directory, you will find an example of implementation working with **RPi-Monitor-LCD**

![bb](https://raw.github.com/XavierBerger/RPi-Monitor-LCD/master/doc/RPi-Monitor-LCD_bb.png)

**Note**: This electronic assembly comes with additionnal components (DS18B20 temperature sensor and a set of 433MHz components) I plan to use in future projects.

## Installation

Install the dependencies with the following commands:

  * `sudo apt-get install python-dev python-imaging python-imaging-tk python-pip`
  * `sudo pip install wiringpi2`
  * `sudo pip install fysom`
  * `sudo pip install spidev`
  * Install PCD8544 library as follow:

```
git clone https://github.com/XavierBerger/pcd8544.git
cd pcd8544
./setup.py clean build 
sudo ./setup.py install
```

  * Remove `i2c-bcm2708` from `/etc/modprobe.d/raspi-blacklist.conf`
  * Add `i2c-dev` in `/etc/modules`
  * `reboot` or execute `gpio load i2c`
  
##Finite State Machine behavior and configuration

Keyboard and backlight configuration

```
keyboard.repeat=<Number of cycles before concerning key as repeated>
backlight.delay=<Number of seconds to turn light on when key pressed >
```

Initial state for the FSM

`fsm.initial=<state name>`

Define the content of a page associated to a state name

`pages.<state name>.content.<line number>=<python command>`

Define event (for a source state, define what is the destination state when a key is pressed)
```
fsm.events.<event id>.name=<key name [up|down|left|right|enter]>
fsm.events.<event id>.src=<state name>
fsm.events.<event id>.dst=<state name>
```

On key pressed callback
```
fsm.<state name>.onup=<python command>
fsm.<state name>.ondown=<python command>
fsm.<state name>.onleft=<python command>
fsm.<state name>.onright=<python command>
fsm.<state name>.onenter=<python command>
```

**Note**: A special state named ```action``` is designed to execute action and comes back to the initial source state

### To be written...

##Example
This repository contains an example of state machine configured as shown in the diagram bellow:
![fsm](https://raw.github.com/XavierBerger/RPi-Monitor-LCD/master/doc/rpimonitorlcd.png)
