#!/usr/bin/env python
# -*- coding: utf-8 -*

import cv2
import os
import sys
import shutil

path = os.getcwd()[:-8]

for image_path in os.listdir(path + '/face_image/'):
    print image_path
    for image_file in os.listdir(path + '/face_image/'+image_path):
        
        img = cv2.imread(path+'/face_image/' + image_path + '/' + image_file)
        
        image_height, image_width = img.shape[:2]

        cv2.imwrite(path + '/face_image/' + image_path + '/' + image_file.split('_')[0] + '_' + str(int(image_file.split('_')[1])+2) + '_' + image_file.split('_')[2], cv2.flip(img, 1))
        
        f = open(path + '/learning/' + image_path + '/' + image_file[:-3] + 'txt')
        learning_txt = f.read()
        f.close()
        converted_x, converted_y, converted_w, converted_h = learning_txt.split()[1:]
        w = float(converted_w) * image_width
        h = float(converted_h) * image_height
        x = image_width - (float(converted_x) * image_width * 2.0 - w) / 2 - w
        y = (float(converted_y) * image_height * 2.0 - h) / 2
        
        convert_x = float(x + x + w)/2.0/image_width
        convert_y = float(y + y + h)/2.0/image_height
        convert_w = float(w)/image_width
        convert_h = float(h)/image_height
        
        learning_txt = str(int(image_path)) + ' ' + str(convert_x) + ' ' + str(convert_y) + ' ' + str(convert_w) + ' ' + str(convert_h) + '\n'
        label_txt = open(path + '/learning/' + image_path + '/' + image_file.split('_')[0] + '_' + str(int(image_file.split('_')[1])+2) + '_' + image_file.split('_')[2], 'w')
        label_txt.write(learning_txt)
        label_txt.close()
