#!/bin/sh
cd /home/pi/tailup/txvod/vod-python-sdk
rm /dev/shm/h264/*.*
rm /dev/shm/mp4/*.*
python doCreatMP4.py
