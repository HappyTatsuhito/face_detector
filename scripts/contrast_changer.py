#!/usr/bin/env python
# -*- coding: utf-8 -*

import cv2
import os
import sys
import numpy as np

path = os.getcwd()[:-8]
gamma_1 = 0.8
gamma_2 = 1.5

look_up_table_1 = np.zeros((256,1), dtype=np.uint8)
look_up_table_2 = np.zeros((256,1), dtype=np.uint8)
for i in range(256):
    look_up_table_1[i][0] = 255* (float(i)/255) ** (1.0 / gamma_1)
    look_up_table_2[i][0] = 255* (float(i)/255) ** (1.0 / gamma_2)

for image_path in os.listdir(path + '/face_image/'):
    print image_path
    for image_file in os.listdir(path + '/face_image/'+image_path):
        
        img = cv2.imread(path+'/face_image/' + image_path + '/' + image_file)
        img_gamma_1 = cv2.LUT(img, look_up_table_1)
        img_gamma_2 = cv2.LUT(img, look_up_table_2)

        print '\t'+ image_file

        cv2.imwrite(path + '/face_image2/' + image_path + '/' + image_file.split('_')[0] + '_' + str(int(image_file.split('_')[1])+4) + '_' + image_file.split('_')[2], img_gamma_1)
        cv2.imwrite(path + '/face_image2/' + image_path + '/' + image_file.split('_')[0] + '_' + str(int(image_file.split('_')[1])+8) + '_' + image_file.split('_')[2], img_gamma_2)

        os.system('cp ' + path + '/learning/' + image_path + '/' + image_file[:-3] + 'txt ' + path + '/learning2/' + image_path + '/' + image_file.split('_')[0] + '_' + str(int(image_file.split('_')[1])+4) + '_' + image_file.split('_')[2][:-3] + 'txt')
        os.system('cp ' + path + '/learning/' + image_path + '/' + image_file[:-3] + 'txt ' + path + '/learning2/' + image_path + '/' + image_file.split('_')[0] + '_' + str(int(image_file.split('_')[1])+8) + '_' + image_file.split('_')[2][:-3] + 'txt')
