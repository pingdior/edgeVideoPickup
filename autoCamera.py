from qcloud_vod.vod_upload_client import VodUploadClient
from qcloud_vod.model import VodUploadRequest
import time
from picamera import PiCamera
from time import sleep
import os

def getFileName():
  localtime = time.localtime(time.time());
  timeStr = time.strftime("%Y%m%d%H%M%S",localtime);
  newFileName = 'wbq'+timeStr+'.h264';
  return newFileName;

def getCamera(fileName):
  try:
   camera = PiCamera();
   camera.start_preview();
   camera.start_recording(fileName);
   sleep(30);
   camera.stop_recording();
   camera.stop_preview();
  except Exception as err:
   print(err)
  return

def convert_to_mp4(source_path):
    HFOMAT=".h264";
    MFOMAT=".mp4";
    target_path = source_path;
    target_path = target_path.replace(HFOMAT,MFOMAT);
    print target_path;
    print source_path;
    cmod='MP4Box'+' -add '+source_path+' '+target_path;
    execute_state = os.system(cmod);
    print(cmod)
    print(execute_state)
    if execute_state==0:
        return target_path;
    else:
        return

def mp4LoadTXVod(mpFileName,vodID,vodKey,vodArea,vodAppId):
 client = VodUploadClient(vodID,vodKey)
 request = VodUploadRequest()
 request.MediaFilePath = mpFileName;
 request.StorageRegion = vodArea;
 request.SubAppId = vodAppId;
 try:
   response = client.upload(vodArea,request)
   print(response.FileId)
   print(response.MediaUrl)
   return response.FileId
 except Exception as err:
   print(err)
   return ""
