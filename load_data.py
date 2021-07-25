import os
import random
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from tqdm import tqdm
from PIL import Image
import torch.nn.functional as F
import torch.optim as om
import torchvision as tv
import torch.utils.data as data
import torch
import torch.nn as nn



# Helper function to load up the dataset
def create_dataset(dir):
    # an unnested list of filenames
    imgFilesList = []

    # labels for each individual image in the list
    class_labels = []

    labels = os.listdir(data_dir)
    nClasses = len(labels)

    imgFiles = [[os.path.join(data_dir, labels[i], x)
     for x in tqdm(os.listdir(os.path.join(data_dir, labels[i])), desc=f"Loading Images from {labels[i]}")] 
     for i in range(nClasses)]

    # count of images in each category
    count_labels = [len(imgFiles[i]) for i in range(nClasses)]

    for i in range(nClasses):
        imgFilesList.extend(imgFiles[i])
        class_labels.extend([i]*count_labels[i])

    # total number of images
    total_imgs = len(class_labels)
    img_width, img_height = Image.open(imgFilesList[0]).size

    return imgFilesList, class_labels, labels, count_labels , total_imgs, img_width, img_height, nClasses




if name__=="__main__":
    imgFilesList, class_labels, labels,count_labels, total_imgs, img_width, img_height, nClasses = create_dataset(data_dir)