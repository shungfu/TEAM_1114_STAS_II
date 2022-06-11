import numpy as np
import cv2
import json
import os



def preprocess():
    name_dir = os.listdir('All_Annotations')
    name_dir = [name[:-5] for name in name_dir]

    os.makedirs('./All_Mask',exist_ok = True)
    os.makedirs('./All_Masked_Images',exist_ok = True)
    for name in name_dir:
        image = cv2.imread(f'All_Images/{name}.jpg')

        polys = []
        with open(f'All_Annotations/{name}.json') as f:
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
        cv2.imwrite(f'All_Mask/{name}.jpg', mask)
        cv2.imwrite(f'All_Masked_Images/{name}.jpg', masked)

if __name__=='__main__':
    preprocess()