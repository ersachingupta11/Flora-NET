# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L6FA7tjzHbMW28CMKX-Ms8IZl1oTnuII
"""

import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Define the path to your dataset
# Define the path to your dataset in Google Drive
dataset_path = "/content/drive/My Drive/flower_datasets"
output_path = "/content/drive/My Drive/split_flower_datasets"

# Check if the output folders exist; if not, create them
if not os.path.exists(output_path):
    os.makedirs(output_path)


# Define transformations for preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize images to 224x224
    transforms.ToTensor(),           # Convert images to tensors
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalize images
])


# Load the dataset from the specified directory
dataset = dataset_path.ImageFolder(data_dir, transform=transform)


#Split the dataset into the Training (80%), Validation (10%), and Testing (10%)
splitfolders.ratio(dataset_path, output=output_path, seed=42, ratio=(.8, .1, .1))
#Create the Folders for Training, Validation and Testing
train_dataset_path = "/content/drive/My Drive/split_flower_datasets/train"
val_dataset_path = "/content/drive/My Drive/split_flower_datasets/val"
test_dataset_path = "/content/drive/My Drive/split_flower_datasets/test"

import sys
new_batch = int(sys.argv[3])

# Batch size
batch_size = new_batch  # Set your batch size here

# Create DataLoaders for training, validation, and testing
train_dataset = DataLoader(
    datasets.ImageFolder(train_dataset_path, transform=transform),
    batch_size=batch_size,
    shuffle=True  # Shuffle training data
)

val_dataset = DataLoader(
    datasets.ImageFolder(val_dataset_path, transform=transform),
    batch_size=batch_size,
    shuffle=False  # No need to shuffle validation data
)

test_dataset = DataLoader(
    datasets.ImageFolder(test_dataset_path, transform=transform),
    batch_size=batch_size,
    shuffle=False  # No need to shuffle testing data
)
