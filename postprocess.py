import cv2
import os
import numpy as np

import config as cfg

# data_path = './Predictions_Ensemble6_th043/'
# ori_path = './Inference_Images/'
# output_path = './Result_Ensemble6_th043/'
# mask_path = './Masked_Result_Ensemble6_th043/'

os.makedirs(cfg.ENSEMBLE_RST_DIR, exist_ok=True)
os.makedirs(cfg.ENSEMBLE_MASK_DIR, exist_ok=True)

filenames = os.listdir(cfg.ENSEMBLE_PRED_DIR)
for filename in filenames:
    ori_img_path = os.path.join(cfg.INFERENCE_IMAGE_DIR, filename[:-4]+'.jpg')
    img_path = os.path.join(cfg.ENSEMBLE_PRED_DIR, filename)
    image = cv2.imread(img_path, 0)
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    ## Fill hole
    for idx in range(len(contours)):
        contour = contours[idx]
        area = cv2.contourArea(contour)
        cv2.fillPoly(image, pts =[contour], color=(255,255,255))
    
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    ## Erase Edge
    kernel = np.ones((3,3), np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 2)
    

    ori_img = cv2.imread(ori_img_path)


    cv2.imwrite(os.path.join(cfg.ENSEMBLE_RST_DIR, filename), erosion)
    masked = cv2.bitwise_and(ori_img, ori_img, mask = erosion)
    cv2.imwrite(os.path.join(cfg.ENSEMBLE_MASK_DIR, filename), masked)
    