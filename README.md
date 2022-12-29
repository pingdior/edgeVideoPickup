# edgeVideoPickup
利用腾讯提供的云点播PYTHON版本的SDK，进行边缘视频数据采集上腾讯指定APPID的云点播资源，具体安装步骤如下：
## 1 安装vod-python-sdk；
## 2 下载本库edgeVideoPickup，且把其下所有文件拷贝进入vod-python-sdk的一级目标下；
## 3 调整
- 建立2个文件夹，放采集的数据和处理后的视频：h264 , mp4 并且在ctcmsconf.py 文件里，修改当前文件夹所在的路径
- 确认当前配置文件loadTXVODParameter.py，填入云点播用户名称、密码、区域和子APPID，共4个项，确定存储路径是否是目标云点播库账号
- 修改权限，支持当前账户执行。建议使用：chmod 755
## 4 安装MP4BOX，且把路径写入：/etc/profile文件里，加入以下两行：
- MP_PATH=/usr/local/MP4Box/bin
- export PATH=$PATH:$MP_PATH
### 可使用 MP4Box -h来测试，是否安装成功
### sudo apt-get install gpac
## 最后，运行主程序：python doCreatMP4.py
一分钟左右，数据可以在指定APPID的云点播库查看到
## 也可以使用crontab程序，在设置时间间隔内执行，例如：
## #每天23:30腾讯上传云点播的短视频
- 25 23 * * *  sudo chmod 755 /home/pi/txvod/h264/*.*
- 25 23 * * *  sudo chmod 755 /home/pi/txvod/mp4/*.*

- 30 23 * * *  rm /home/pi/txvod/h264/*.*
- 5 23 * * *  rm /home/pi/txvod/mp4/*.*

## #在规定时间范围内每隔3分钟上传云点播短视频
*/3 * * * * sh  /home/pi/tailup/txvod/vod-python-sdk/excute.sh  >>/dev/null  2>&1 &

if crontab fail, we can use "cd" current path 

