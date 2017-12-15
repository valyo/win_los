#!/bin/bash

PYTHON=$(which python)
DATE=$(date +"%Y-%m-%d")

#check if an output file from taday exists
if [ ! -s $HOME/winners_loosers/$DATE-vinnare-forlorareNew.txt ]
then
  $PYTHON $HOME/winners_loosers/getWinLos.py > $HOME/winners_loosers/$DATE-vinnare-forlorareNew.txt
  echo "collected $DATE" >> $HOME/winners_loosers/log.txt
else
  echo "nothing to do $(date)" >> $HOME/winners_loosers/log.txt
fi

$PYTHON $HOME/winners_loosers/getWinLos.01.py