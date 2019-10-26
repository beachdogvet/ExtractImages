#!/bin/sh

clear
echo "\nBegin extracting files from $1"

7z e $1 -o$2
echo "\n\nFinished extracting files from $1 \n\n"


exit 0

