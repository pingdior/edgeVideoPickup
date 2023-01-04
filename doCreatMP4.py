import h264_to_mp4
import autoCamera
import loadTXVODParameter
import datetime
import ctcmsconf

h264_to_mp4.init_video_folder();
h264FilePath =h264_to_mp4.gen_h264_filepath();
print h264FilePath
print "<1> has h264file Path--------------------------------"
mp4FilePath =h264_to_mp4.gen_mp4_filepath();
print mp4FilePath
print "<2> has mp4file Path--------------------------------"
autoCamera.getCamera(h264FilePath);
print "<3> has h264file--------------------------------"
h264_to_mp4.convert_to_mp4(h264FilePath,mp4FilePath);
print "<4> has mp4file--------------------------------"
mediaUrl = autoCamera.mp4LoadTXVod(mp4FilePath,loadTXVODParameter.VODID,loadTXVODParameter.VODKEY,loadTXVODParameter.VODAREA);
print("<5.1> mediaUrl:"+mediaUrl+"--------------------------------------------------------")
print("<5.2> MEDIOURLDIR:"+MEDIOURLDIR+"-----------------------------------------------------")
localtime = datetime.datetime.now()
timeStr = localtime.strftime('%Y-%m-%d-%H-%M-%S')
print("<5.3> timeStr:"+timeStr+"--------------------------------------------------------")

    exist=os.path.exists(ctcmsconf.MEDIOURLDIR)
    if not exist:
        os.makedirs(ctcmsconf.MEDIOURLDIR)
if mediaUrl != "":
   fileName = ctcmsconf.MEDIOURLDIR+timeStr+".txt"
   fw = open(fileName ,'w');
   fw.write(mediaUrl);
   print("<6> File is URL OK "+"--------------------------------------------------------")
else:
   fileName =  MEDIOURLDIR+"error"+timeStr+".txt"
   fw = open(fileName ,'w');
   print("<6> File is ERROR OK "+"--------------------------------------------------------")
fw.close()

