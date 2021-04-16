import sys
sys.path.append('../')

import pandas as pd;
import time;
import cv2
import numpy as np
from rcnnpose.estimator import BodyPoseEstimator
from rcnnpose.utils import draw_body_connections, draw_keypoints, draw_masks
import math
import os

estimator = BodyPoseEstimator(pretrained=True);


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def main(input_img, outfile):
#     start = time.time();
    image_src = cv2.imread(input_img)
    pred_dict = estimator(image_src, masks=False, keypoints=True)
    # masks = estimator.get_masks(pred_dict['estimator_m'], score_threshold=0.8)
    keypoints = estimator.get_keypoints(pred_dict['estimator_k'], score_threshold=0.99)


    if len(keypoints) == 0:
        print("not found");
#     print(f"masks : {masks}");
#     print(f"keypoints : {keypoints}");
    else:
        nose = keypoints[0][0][:2];
        eye_l = keypoints[0][1][:2];
        eye_r = keypoints[0][2][:2];
        ear_l = keypoints[0][3][:2];
        ear_r = keypoints[0][4][:2];
        sho_l = keypoints[0][5][:2];
        sho_r = keypoints[0][6][:2];
        elb_l = keypoints[0][7][:2];
        elb_r = keypoints[0][8][:2];
        wri_l = keypoints[0][9][:2];
        wri_r = keypoints[0][10][:2];
        hip_l = keypoints[0][11][:2];
        hip_r = keypoints[0][12][:2];
        knee_l = keypoints[0][13][:2];
        knee_r = keypoints[0][14][:2];
        ankle_l = keypoints[0][15][:2];
        ankle_r = keypoints[0][16][:2];
        neck = (ear_l+ear_r)/2;
        fname = outfile[8:]

        # Angle
        sho_l_angle = getAngle(elb_l,sho_l,hip_l)
        sho_r_angle = getAngle(elb_r,sho_r,hip_r)
        elb_l_angle = getAngle(sho_l,elb_l,wri_l)
        elb_r_angle = getAngle(sho_r,elb_r,wri_r)
        neck_angle = abs(180-getAngle(neck, (sho_l+sho_r)/2, (hip_l+hip_r)/2))
        trunk_angle = getAngle((sho_l+sho_r)/2, (hip_l+hip_r)/2, (((hip_l+hip_r)/2)[0], ((sho_l+sho_r)/2)[1]))

        if sho_l_angle > 180:
            sho_l_angle = 360-sho_l_angle

        if sho_r_angle > 180:
            sho_r_angle = 360-sho_r_angle
        
        if elb_l_angle > 180:
            elb_l_angle = 360-elb_l_angle

        if elb_r_angle > 180:
            elb_r_angle = 360-elb_r_angle
            
        if neck_angle > 180:
            neck_angle = 360-neck_angle
            
        if trunk_angle > 180:
            trunk_angle = 360-trunk_angle

        df_joint = pd.DataFrame({"file_name": fname,
                        "nose":nose, "neck":neck, 
                        "eye_l":eye_l, "eye_r":eye_r, 
                        "ear_l":ear_l, "ear_r":ear_r, 
                        "sho_l":sho_l,"sho_r":sho_r,
                        "elb_l":elb_l,"elb_r":elb_r,
                        "wri_l":wri_l,"wri_r":wri_r,
                        "hip_l":hip_l,"hip_r":hip_r,
                        "knee_l":knee_l, "knee_r":knee_r,
                        "ankle_l":ankle_l, "ankle_r":ankle_r}, index=["x","y"]);
        print(df_joint);

        #write down the angle on image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_src,'neck: '+str(round(neck_angle,2)),(160,10), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image_src,'shoulder_left: '+str(round(sho_l_angle,2)),(160,20), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image_src,'shoulder_right: '+str(round(sho_r_angle,2)),(160,30), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image_src,'elbow_left: '+str(round(elb_l_angle,2)),(160,40), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image_src,'elbow_reft: '+str(round(elb_r_angle,2)),(160,50), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image_src,'trunk: '+str(round(trunk_angle,2)),(160,60), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)


        df_ang = pd.DataFrame({
            "file_name": fname,
            "sho_l":sho_l_angle, "sho_r":sho_r_angle, "elb_l":elb_l_angle, "elb_r":elb_r_angle, "neck":neck_angle, "trunk":trunk_angle
        }, index=["angle"]);
        print(df_ang);

        # csv저장
        df_joint.to_csv("joint_coordinates.csv", mode='a', header=True)
        df_ang.to_csv("joint_angle.csv",mode='a', header=True)

        image_dst = cv2.cvtColor(image_src, cv2.COLOR_BGR2GRAY)
        # image_dst = cv2.merge([image_dst] * 3)
        # overlay_m = draw_masks(image_dst, masks, color=(0, 255, 0), alpha=0.5)
        overlay_k = draw_body_connections(image_src, keypoints, thickness=3, alpha=0.7)
        overlay_k = draw_keypoints(overlay_k, keypoints, radius=1, alpha=1)
        image_dst = overlay_k;

        cv2.imwrite(outfile, image_dst);


if __name__ == "__main__":

    path = "./[3]outputs_background_removed"
    file_list = os.listdir(path)

    for file in file_list:
        main(f"[3]outputs_background_removed/"+file, f"[4]outputs_keypoint/"+file);

