#!/usr/bin/env python
# -*- coding: utf-8 -*

import cv2
import os
import sys

args = sys.argv[-1]

if 'face_detector.py' in args:
    exit()
dir_path = args + '/'

path = os.getcwd()[:-8]

for txt_file in os.listdir(path + '/learning/' + dir_path):
    f = open(path + '/learning/' + dir_path + '/' + txt_file)
    learning_txt = f.read()
    f.close()

    txt_msg = str(int(learning_txt.split()[0])) + ' ' + learning_txt.split()[1] + ' ' + learning_txt.split()[2] + ' ' + learning_txt.split()[3] + ' ' + learning_txt.split()[4]

    print path + '/learning/' + dir_path + txt_file

    label_txt = open(path + '/learning/' + dir_path + txt_file, 'w')
    label_txt.write(txt_msg)
    label_txt.close()
