#!/bin/bash

PYTHON=$(which python)
DATE=$(date +"%Y-%m-%d")

#check if an output file from taday exists
if [ ! -s $HOME/winners_losers/$DATE-vinnare-forlorareNew.txt ]
then
  $PYTHON $HOME/winners_losers/getWinLos.py > $HOME/winners_losers/$DATE-vinnare-forlorareNew.txt
  echo "collected $DATE" >> $HOME/winners_losers/log.txt
else
  echo "nothing to do $(date)" >> $HOME/winners_losers/log.txt
fi

$PYTHON $HOME/winners_losers/getWinLos.01.py
