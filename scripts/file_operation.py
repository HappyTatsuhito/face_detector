#!/usr/bin/env python
# -*- coding: utf-8 -*

import cv2
import os
import sys
import random

args = sys.argv[-1]

'''
if 'face_detector.py' in args:
    exit()
dir_path = args + '/'
'''

path = os.getcwd()[:-8]

img = cv2.imread('/home/demlab/Desktop/group3_data_set/group1_data_set/7_2_222.jpg')
print img.shape[:2]

'''
txt_file = open('/home/demlab/Desktop/group3_data_set/txt/all.txt')
learning_path = txt_file.readlines()
txt_file.close()
txt_random_path = random.sample(learning_path, len(learning_path))
count = 0
t_txt = 'aaa'
for txt_path in txt_random_path:
    if count < 21840:
        t_txt = '/train.txt'
    else :
        t_txt = '/test.txt'
    learning_txt_file = open('/home/demlab/Desktop/group3_data_set/txt/'+t_txt, 'a')
    learning_txt_file.write(txt_path)
    learning_txt_file.close()
    count += 1
'''    

    
'''
for file_path in os.listdir(path + '/learning/'):
    os.system('mv '+path+'/learning/'+file_path+'/* '+ '/home/demlab/Desktop/group3_data_set/data_set')
    os.system('mv '+path+'/face_image/'+file_path+'/* '+ '/home/demlab/Desktop/group3_data_set/data_set')
'''
