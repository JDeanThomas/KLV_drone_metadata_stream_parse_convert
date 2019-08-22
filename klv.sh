#!/bin/bash

echo Enter KLV File Directory to Convert:

read -p "Directory: " dir

echo "converting files in $dir"

ffmpeg -i Day\ Flight.mpg -map data-re -codec copy -f data - | python3 $dir

echo "finished"