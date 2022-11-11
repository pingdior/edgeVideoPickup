import h264_to_mp4
import autoCamera
import loadTXVODParameter 
h264_to_mp4.init_video_folder();
h264FilePath =h264_to_mp4.gen_h264_filepath();
print h264FilePath 
print "--------------------------------"
mp4FilePath =h264_to_mp4.gen_mp4_filepath();
print mp4FilePath 
print "--------------------------------"
autoCamera.getCamera(h264FilePath);
h264_to_mp4.convert_to_mp4(h264FilePath,mp4FilePath);
autoCamera.mp4LoadTXVod(mp4FilePath,loadTXVODParameter.VODID,loadTXVODParameter.VODKEY,loadTXVODParameter.VODAREA);
