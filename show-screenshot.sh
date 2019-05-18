#!/bin/sh
file=$( ls -1 screenshots/screenshot-*.png --sort=time | head -n 1 );
echo "$file"
img2txt "$file"
