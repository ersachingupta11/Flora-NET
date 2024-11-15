# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L6FA7tjzHbMW28CMKX-Ms8IZl1oTnuII
"""

#Import Libraries
import os
from PIL import Image, ImageOps
import shutil

"""**Horizontal and Vertical Flipping**"""

# Define paths for original and augmented datasets
original_dirs = {
    "train": "/content/drive/My Drive/split_flower_datasets/train",
    "val": "/content/drive/My Drive/split_flower_datasets/val",
    "test": "/content/drive/My Drive/split_flower_datasets/test"
}

augmented_dirs = {
    "train": "/content/drive/My Drive/split_flower_datasets/train_aug",
    "val": "/content/drive/My Drive/split_flower_datasets/val_aug",
    "test": "/content/drive/My Drive/split_flower_datasets/test_aug"
}

# Create directories for augmented datasets if they don't exist
for aug_dir in augmented_dirs.values():
  if not os.path.exists(aug_dir):
    os.makedirs(aug_dir)

# Define the augmentation function for horizontal and vertical flipping
def augment_and_save_images_with_flip(source_dir, destination_dir):
    for class_name in os.listdir(source_dir):
        class_directory = os.path.join(source_dir, class_name)
        augmented_class_directory = os.path.join(destination_dir, class_name)

        # Create class directories in augmented dataset folder
        if not os.path.exists(augmented_class_directory):
            os.makedirs(augmented_class_directory)

        # Iterate over images in the class folder
        for img_name in os.listdir(class_directory):
            img_path = os.path.join(class_directory, img_name)
            with Image.open(img_path) as img:
                # Save the original image
                img.save(os.path.join(augmented_class_directory, img_name))

                # Apply horizontal flip and save
                h_flip = ImageOps.mirror(img)
                h_flip.save(os.path.join(augmented_class_directory, f"hflip_{img_name}"))

                # Apply vertical flip and save
                v_flip = ImageOps.flip(img)
                v_flip.save(os.path.join(augmented_class_directory, f"vflip_{img_name}"))

                # Apply both horizontal and vertical flip and save
                hv_flip = ImageOps.mirror(v_flip)
                hv_flip.save(os.path.join(augmented_class_directory, f"hvflip_{img_name}"))

"""**Contrast Stretching**"""

def contrast_stretch(img):
    """
    Apply contrast stretching to enhance image contrast.
    """
    return ImageOps.autocontrast(img)

def augment_and_save_images_with_contrast(source_dir, destination_dir):
    for class_name in os.listdir(source_dir):
        class_directory = os.path.join(source_dir, class_name)
        augmented_class_directory = os.path.join(destination_dir, class_name)

        # Create class directories in augmented dataset folder
        if not os.path.exists(augmented_class_directory):
            os.makedirs(augmented_class_directory)

        # Iterate over images in the class folder
        for img_name in os.listdir(class_directory):
            img_path = os.path.join(class_directory, img_name)
            with Image.open(img_path) as img:
                # Save the original image
                img.save(os.path.join(augmented_class_directory, img_name))

                # Apply contrast stretching and save
                contrast_img = contrast_stretch(img)
                contrast_img.save(os.path.join(augmented_class_directory, f"contrast_{img_name}"))

"""**Gaussian Filtering**"""

from PIL import ImageFilter

def gaussian_filter(img, radius=2):
    """
    Apply Gaussian filtering (blur) to an image.
    Args:
        img: PIL Image object.
        radius: The radius of the Gaussian blur. Higher values give more blur.
    Returns:
        Blurred image with Gaussian filter applied.
    """
    return img.filter(ImageFilter.GaussianBlur(radius))


def augment_and_save_images_with_gaussian(source_dir, destination_dir):
    for class_name in os.listdir(source_dir):
        class_directory = os.path.join(source_dir, class_name)
        augmented_class_directory = os.path.join(destination_dir, class_name)

        # Create class directories in augmented dataset folder
        if not os.path.exists(augmented_class_directory):
            os.makedirs(augmented_class_directory)

        # Iterate over images in the class folder
        for img_name in os.listdir(class_directory):
            img_path = os.path.join(class_directory, img_name)
            with Image.open(img_path) as img:

                # Save the original image
                img.save(os.path.join(augmented_class_directory, img_name))

                # Apply Gaussian filtering and save
                gaussian_img = gaussian_filter(img, radius=2)
                gaussian_img.save(os.path.join(augmented_class_dir, f"gaussian_{img_name}"))

"""**Gaussian Noise Additive**"""

import numpy as np

def add_gaussian_noise(img, mean=0, std=25):
    """
    Add Gaussian noise to an image.
    Args:
        img: PIL Image object.
        mean: Mean of the Gaussian noise.
        std: Standard deviation of the Gaussian noise.
    Returns:
        Noisy image with Gaussian noise applied.
    """
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Generate Gaussian noise
    noise = np.random.normal(mean, std, img_array.shape).astype(np.float32)

    # Add the noise to the image and clip values to ensure they remain in [0, 255]
    noisy_img_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)

    # Convert back to PIL image
    noisy_img = Image.fromarray(noisy_img_array)
    return noisy_img


def augment_and_save_images_with_noise(source_dir, destination_dir):
    for class_name in os.listdir(source_dir):
        class_directory = os.path.join(source_dir, class_name)
        augmented_class_directory = os.path.join(destination_dir, class_name)

        # Create class directories in augmented dataset folder
        if not os.path.exists(augmented_class_directory):
            os.makedirs(augmented_class_directory)

        # Iterate over images in the class folder
        for img_name in os.listdir(class_directory):
            img_path = os.path.join(class_directory, img_name)
            with Image.open(img_path) as img:

                # Save the original image
                img.save(os.path.join(augmented_class_directory, img_name))

                # Apply Gaussian noise and save
                noisy_img = add_gaussian_noise(img, mean=0, std=25)
                noisy_img.save(os.path.join(augmented_class_directory, f"noisy_{img_name}"))

"""**Main File**"""

# Apply augmentation for train, validation, and test datasets
for dataset_type, src_dir in original_dirs.items():
    dest_dir = augmented_dirs[dataset_type]
    augment_and_save_images_with_flip(source_dir, destination_dir)
    augment_and_save_images_with_contrast(source_dir, destination_dir)
    augment_and_save_images_with_gaussian(source_dir, destination_dir)
    augment_and_save_images_with_noise(source_dir,destination_dir)