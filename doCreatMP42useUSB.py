import h264_to_mp4
import autoCamera
import loadTXVODParameter 
import datetime
import ctcmsconf

h264_to_mp4.init_video_folder();
h264FilePath =h264_to_mp4.gen_h264_filepath();
print h264FilePath 
print "--------------------------------"
mp4FilePath =h264_to_mp4.gen_mp4_filepath();
print mp4FilePath 
print "--------------------------------"
h264_to_mp4.create_to_mp4(h264FilePath,mp4FilePath);

mediaUrl = autoCamera.mp4LoadTXVod(mp4FilePath,loadTXVODParameter.VODID,loadTXVODParameter.VODKEY,loadTXVODParameter.VODAREA);
print("mediaUrl:"+mediaUrl+"--------------------------------------------------------") 
print("MEDIOURLDIR:"+ctcmsconf.MEDIOURLDIR+"-----------------------------------------------------")
localtime = datetime.datetime.now()
timeStr = localtime.strftime('%Y-%m-%d-%H-%M-%S')
print(timeStr+"--------------------------------------------------------") 

if mediaUrl != "":
   fileName = ctcmsconf.MEDIOURLDIR+timeStr+".txt";
   fw = open(fileName ,'w');
   fw.write(mediaUrl);
else:
   fileName =  ctcmsconf.MEDIOURLDIR+"error"+timeStr+".txt";
   fw = open(fileName ,'w');
fw.close()

