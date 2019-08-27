#!/bin/bash

echo Enter KLV File Directory to Convert:

read -p "Directory: " dir

echo "converting files in $dir"

#for i in *.avi; do ffmpeg -i "$i" "${i%.*}.mp4"; done

for i in $dir/*.mpg; do ffmpeg -i "$i" -map data-re -codec copy -f data - | python3 ./klvdata_parse.py; done

echo "finished"