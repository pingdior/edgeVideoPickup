import os
import random
import time
import ctcmsconf

def init_video_folder():
    exist=os.path.exists(ctcmsconf.H264_PATH)
    if not exist:
        os.makedirs(H264_PATH)
    
    exist=os.path.exists(ctcmsconf.MP4_PATH)
    if not exist:
        os.makedirs(ctcmsconf.MP4_PATH)

def convert_to_mp4(source_path,target_path):
    cmod='MP4Box -fps '+str(ctcmsconf.MP4_FPS)+' -add '+source_path+' '+target_path;
    execute_state = os.system('MP4Box -fps '+str(ctcmsconf.MP4_FPS)+' -add '+source_path+' '+target_path);
    print(cmod)
    print(execute_state)
    if execute_state==0:
        return True
    else:
        return False

def check_is_exist(path,suffix):
    return os.path.exists(path+'.'+suffix)
	
def gen_mp4_filepath(filename=''):
     if filename=='':
        filename=gen_random_filename(ctcmsconf.MP4_PATH+'record-'+format_currrenttime('%Y%m%d%H%m%s'))
     else:
        filename=gen_random_filename(filename)
        
     if check_is_exist(filename,'mp4'):
        return gen_mp4_filepath(filename)
     else:
        return filename+'.mp4'

def gen_h264_filepath(filename=''):
    if filename=='':
        filename=gen_random_filename(ctcmsconf.H264_PATH+'record-'+format_currrenttime('%Y%m%d%H%m%s'))
    else:
        filename=gen_random_filename(filename)
        
    if check_is_exist(filename,'h264'):
        return gen_mp4_filepath(filename)
    else:
        return filename+'.h264'

def gen_random_filename(filename):
    return filename+str(random.randint(0,10))
def format_currrenttime(format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format,time.localtime(time.time()))

