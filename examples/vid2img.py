import os
import cv2
import numpy as np
# Video to Image
path = "./[1]vid2img/"
file_list = os.listdir(path)
print("{}".format(file_list))

def getFrame(sec,file_name):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()

    if hasFrames:
        h = 256
        w = 256
        resized_image = cv2.resize(image, (h, w)).astype(np.float32)
        if count < 10:
            cv2.imwrite("./[2]inputs/" + file_name +'_0000'+str(count)+".jpg", resized_image)     # save frame as JPG file
        elif count < 100:
            cv2.imwrite("./[2]inputs/" + file_name +'_000'+str(count)+".jpg", resized_image)     # save frame as JPG file
        elif count < 1000:
            cv2.imwrite("./[2]inputs/" + file_name +'_00'+str(count)+".jpg", resized_image)     # save frame as JPG file
        elif count < 10000:
            cv2.imwrite("./[2]inputs/" + file_name +'_0'+str(count)+".jpg", resized_image)     # save frame as JPG file

    return hasFrames

for file in file_list:
    vidcap = cv2.VideoCapture(path+file)
    sec = 0
    frameRate = 1 #//it will capture image in each 1 second
    count=1
    success = getFrame(sec,file)

    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,file)