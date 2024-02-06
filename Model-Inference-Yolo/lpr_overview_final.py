# -*- coding: utf-8 -*-
"""LPR_Overview_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V5mQiN0DFwUwuk-QKUW_6vxDQwFaEjBS

# <font color='red' size='5px'/> LPR Project<font/>
"""

from IPython.display import Image

"""#<font color='blue' size='5px'/> Overview<font/>

## 1 Problem Statement

**Problem Statement:**

Design and implement a real-time license plate detection system capable of accurately detecting and localizing license plates in images. The system should be able to handle various environmental conditions, such as different lighting conditions, vehicle orientations, and background clutter, and provide reliable results for further processing or use in applications like traffic monitoring, parking management, or law enforcement.

## 2 Project Goal
**Key Objectives and Requirements:**

1. Use or create a deep learning-based object detection model, such as YOLO, to identify license plates in a given image or video frame.

2. Label and collect a dataset of images with vehicles that have license plates, including various situations and license plate types.

3. Train the detection model on the dataset to achieve high accuracy and robustness in real-world conditions.

4. Apply post-processing techniques, like Non-Maximum Suppression (NMS), to improve the detected license plate bounding boxes.

5. Provide visual feedback by showing bounding boxes and text labels (license plate numbers) on detected license plates.

6. Develop a user-friendly interface for testing the system on live camera feeds and pre-recorded video.

7. Evaluate the system’s performance using relevant metrics (e.g., precision, recall, F1-score) and ensure it meets or exceeds predefined accuracy targets.

8. Document the system’s architecture, training process, and deployment instructions for future maintenance and scalability.


##Deliverables:

- Trained model for identifying license plates.
- Software tool or library for license plate recognition with a user interface.
- Documentation explaining system design, data processing, model training, and deployment steps.
- Performance assessment report, including accuracy measures and real-time frame rates.

# <font color='blue' size='5px'/> Literature Review<font/>

## 1 Introduction

**Introduction**

The video is about using YOLO for drowsiness detection, including leveraging the ultralytics of YOLO, fine-tuning the drowsiness model, and testing it in real-time. The presenter showcases the implementation of the YOLO model and performs real-time detections using images, videos, and a webcam. Additionally, the video covers training a custom model for drowsiness detection.

**Loading Pre-Trained Ultralytics Model**

To load the pre-trained ultralytics model, we need to import torch, matplotlib, numpy and cv2 libraries. The model detects 38 cars and 4 trucks with reasonable confidence intervals in a new image passed through a new link.

**Real-Time Detection**

The speaker demonstrates real-time detection using YOLO on a video and a webcam. The code is creating a full file path to the image with a unique identifier and .jpg file extension. The presenter also shows how to run YOLO on a video file.

**Training Custom Drowsiness Detector Model**

The speaker closed the real-time detection and will now train a custom drowsiness detector model using collected images and labels. Two key dependencies need to be installed, piqt5 and lxml, followed by running pi rcc5 command to seed the label image file. The trainer explains the training command and its parameters for YOLOv5 object detection.

**Testing Custom Model**

The YOLO model has finished training and generated data, now it's time to test it. The presenter shows how to test the custom model on a new image, with the output showing whether the person in the image is alert or drowsy.

In summary, the video covers using YOLO for drowsiness detection, including loading pre-trained models, real-time detection on videos and webcams, training custom models, and testing them on new images.

[Original Video](https://www.youtube.com/watch?v=tFNJGim3FXw)

## 2 Dataset

#<font color='blue' size='5px'/> YOLOv5s Project<font/>

##  Packages
"""

# Import the numpy, cv2, torch, pathlib, and matplotlib libraries
import numpy as np
import cv2
import torch
from pathlib import Path
import matplotlib.pyplot as plt

# Import the Image class from PIL
from PIL import Image

# Import the os module
import os

# Mount the Google Drive to access the files
from google.colab import drive
drive.mount('/content/drive')

# Import the torch, torchvision, and transforms modules
import torch
import torchvision
import torchvision.transforms as transforms # For applying transformations on images
from torch.utils.data import DataLoader, Dataset

# Split the dataset into random subsets
from torch.utils.data import  random_split

# Load the model from ultralytics
!pip install ultralytics
!git clone https://github.com/ultralytics/yolov5  # clone the repository
!cd yolov5
!pip install -r requirements.txt  # install the requirements

# The output shape of the model will be (batch_size, num_anchors, grid_size, grid_size, 5), where 5 refers to the number of predicted values for each anchor box, which includes the bounding box coordinates (x, y, width, height), and objectness score.

# Load the model using torch.hub
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom

# Initialize the utils module
import torch
import utils
display = utils.notebook_init()  # checks

# Train the model on the custom dataset
!cd yolov5 && python train.py --img 512 --batch 16 --epochs 10 --data dataset.yml --weights yolov5s.pt --workers 2

# Download the files from the yolov5 folder
from google.colab import files

# Replace 'filename' with the name of the file that you want to download
files.download('/content/yolov5/runs')

# Replace 'filename' with the name of the file that you want to download
files.download('/content/yolov5/runs/train/exp3')

# Load the custom weights for the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp15/weights/last.pt', force_reload=True)
