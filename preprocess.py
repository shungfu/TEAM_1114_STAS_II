import numpy as np
import cv2
import json
import os
import config as cfg


def preprocess():
    name_dir = os.listdir(cfg.ALL_ANNOTATIONS_DIR)
    name_dir = [name[:-5] for name in name_dir]

    os.makedirs(cfg.ALL_MASK_DIR, exist_ok = True)
    os.makedirs(cfg.ALL_MASK_IMAGES_DIR, exist_ok = True)
    for name in name_dir:
        image = cv2.imread(f'{cfg.ALL_IMAGES_DIR}/{name}.jpg')

        polys = []
        with open(f'{cfg.ALL_ANNOTATIONS_DIR}/{name}.json') as f:
            datas = json.load(f)
            for data in datas['shapes']:
                data = np.array(data['points'],dtype=np.int32)
                polys.append(data)

        polys = np.array(polys)

        im = np.zeros(image.shape[:2],dtype='uint8')

        for poly in polys:
            poly = np.reshape(poly,(1,poly.shape[0],poly.shape[1]))
            cv2.polylines(im, poly, 1, 255)
            cv2.fillPoly(im,poly, 255)

        mask = im
        masked = cv2.bitwise_and(image, image ,mask=mask)
        cv2.imwrite(f'{cfg.ALL_MASK_DIR}/{name}.jpg', mask)
        cv2.imwrite(f'{cfg.ALL_MASK_IMAGES_DIR}/{name}.jpg', masked)

if __name__=='__main__':
    preprocess()
