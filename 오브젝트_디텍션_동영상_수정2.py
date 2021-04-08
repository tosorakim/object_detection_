# -*- coding: utf-8 -*-
"""오브젝트 디텍션_동영상.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HW6rbeESA_BwU0ISNnH7O1Liw8atjG-a
"""

!nvidia-smi -L  # GPU 를 사용하는지 확인하는 코드

from google.colab import drive

drive.mount('/content/gdrive')

!git clone https://github.com/heartkilla/yolo-v3.git

# Commented out IPython magic to ensure Python compatibility.
#  %tensorflow_version 1.x

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolo-v3
!pip install -r /content/yolo-v3/requirements.txt

import  tensorflow  as  tf
print ( tf.__version__)

"""이미 학습된 가중치 파일(1000개의 클래스를 분류하는 가중치)을 내려받습니다. """

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolo-v3
!wget -P /content/yolo-v3/weights https://pjreddie.com/media/files/yolov3.weights

import tensorflow as tf

tf.__version__

!python /content/yolo-v3/load_weights.py

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolo-v3
!python detect.py images 0.5 0.5 /content/yolo-v3/data/images/office3.jpg

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolo-v3
!apt install ffmpeg libopencv-dev libgtk-3-dev python-numpy python3-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libtiff5-dev libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libv4l-dev libtbb-dev qtbase5-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils unzip

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolo-v3

!python detect.py video 0.5 0.5 data/video/shinjuku.mp4

from google.colab import files
files.download('./detections/detections.mp4')

!uname -an

!wget http://ciscobinary.openh264.org/libopenh264-1.8.0-linux64.4.so.bz2

!wget http://ciscobinary.openh264.org/libopenh264-2.0.0-linux64.5.so.bz2