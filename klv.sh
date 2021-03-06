#!/bin/bash

echo Enter KLV File Directory to Convert:

read -p "Directory: " dir

echo "converting files in $dir"

for i in $dir/*.mpg; 
    do ffmpeg -i "$i" -map data-re -codec copy -f data - | 
    python3 ./klvdata_parse.py >> "${i%.*}.text"; 
done

echo "finished"