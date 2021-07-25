from load_data import  create_dataset, data_dir
import torchvision as tv
import torch
import time
import pandas as pd
import numpy as np
import torch.nn.functional as F
import torch.optim as om
import torchvision as tv
import torch.utils.data as data
import torch.nn as nn
from PIL import Image

imgFilesList, class_labels, labels,count_labels, total_imgs, img_width, img_height, nClasses = create_dataset(data_dir)


# Transforming and data partition.
# Min-max-scale 
toTensor = tv.transforms.ToTensor()
resize = tv.transforms.Resize((224,224))

def scale_image(x):
    x = resize(x)
    y = toTensor(x)
    if (y.min() < y.max()):
        y = (y-y.min())/(y.max()-y.min())
    z = y - y.mean()
    return z

def transform_(imgFilesList, class_labels):
    img_rescaled = torch.stack([scale_image(Image.open(x)) for x in imgFilesList])
    labels_rescaled = torch.tensor(class_labels)

    print(f'Min pixel value = {img_rescaled.min().item()}; Max = {img_rescaled.min().item()}; Mean = {img_rescaled.mean().item()}')

    return img_rescaled, labels_rescaled


if __name__ == '__main__':

    img_rescaled, labels_rescaled = transform_(imgFilesList, class_labels)
