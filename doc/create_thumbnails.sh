#!/bin/bash
for iloop in RPi-Monitor-LCD_bb.png  RPi-Monitor-LCD_pcb.png  RPi-Monitor-LCD_schem.png; do
  cp $iloop thumb_$iloop
  mogrify -resize 50% -format png thumb_$iloop
done

