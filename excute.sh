#!/bin/sh
cd /home/pi/tailup/txvod/vod-python-sdk
rm ./h264/*.*
rm ./mp4/*.*
python doCreatMP4.py
