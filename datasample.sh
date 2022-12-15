#!/bin/sh

command="/home/pi/software/txiot/sdk2/output/release/bin/data_template_sample"


appname=data_template_sample

logfile=/usr/local/log/data_temlate_sample.log

#返回 ps -ef 出来的所有字符串中含有 $appname 的进程个数

checkrun=`ps -ef | grep $appname | grep -v "grep" | wc -l` 

echo "$appname 运行监测开始….."

#ps -ef | grep launcher | grep -v "grep" | wc -l

 

#while true

#do

#echo $checkrun

if [ 0 = $checkrun ]; then

    #进程不存在

    time2=$(date "+%Y-%m-%d %H:%M:%S")

    echo "$appname 服务宕机,正在重新启动"

  #echo "$appname 服务宕机，宕机时间为:"$time2>>$appname.log

        #./$appname $appname &logfile

   nohup $command >/dev/null    2>&1 &

    #nohup  /usr/local/Presto/presto-server-0.100/bin/launcher run  >  presto_run.log  2>&1 &

sleep 1

 pid=$(ps -ef | grep -v 'grep' | egrep $appname| awk '{printf $2 " "}')   

 echo "$appname ($pid)重新启动成功!!!"

else

  #进程存在
  sleep 1

pid=$(ps -ef | grep -v 'grep' | egrep $appname| awk '{printf $2 " "}')      

 echo "$appname ($pid) 服务运行正常...持续监控中"

fi

time=$(date "+%Y-%m-%d %H:%M:%S")

echo "本轮监测完毕,当前时间为:"$time

#done

#这里有一行

 

 

