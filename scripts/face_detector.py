#!/usr/bin/env python
# -*- coding: utf-8 -*

import cv2
import os
import sys
import shutil

def writeDataSet(img, path, image_path, image_file, faces):
    image_height, image_width = img.shape[:2]
    x, y, w, h = faces[0]
    convert_x = float(x + x + w)/2.0/image_width
    convert_y = float(y + y + h)/2.0/image_height
    convert_w = float(w)/image_width
    convert_h = float(h)/image_height
    learning_txt = str(int(image_path)) + ' ' + str(convert_x) + ' ' + str(convert_y) + ' ' + str(convert_w) + ' ' + str(convert_h) + '\n'
    label_txt = open(path + '/learning/' + image_path + '/' + image_file[:-3] + 'txt', 'w')
    label_txt.write(learning_txt)
    label_txt.close()
    
def main():
    path = os.getcwd()[:-8]

    face_cascade_path_1 = path + '/weight/haarcascade_frontalface_default.xml'
    face_cascade_path_2 = path + '/weight/haarcascade_frontalface_alt.xml'
    face_cascade_1 = cv2.CascadeClassifier(face_cascade_path_1)
    face_cascade_2 = cv2.CascadeClassifier(face_cascade_path_2)
    
    for image_path in os.listdir(path + '/face_image/'):
        
        print image_path
        count = 0
        for image_file in os.listdir(path + '/face_image/'+image_path):
            img = cv2.imread(path+'/face_image/' + image_path + '/' + image_file)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade_1.detectMultiScale(img_gray)
            if len(faces) != 1:
                faces = face_cascade_2.detectMultiScale(img_gray)
                if len(faces) != 1:
                    shutil.move(path + '/face_image/' + image_path + '/' + image_file, path + '/not_used_image/' + image_path)
                    continue
            print '\t' + image_file
            writeDataSet(img, path, image_path, image_file, faces)
            
if __name__ == '__main__':
    main()
