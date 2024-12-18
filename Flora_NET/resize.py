# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L6FA7tjzHbMW28CMKX-Ms8IZl1oTnuII

**Image Resizing**
"""

# Define batch size
batch_size = 16

# Create data loaders for train, validation, and test sets
train_loader = DataLoader(train_aug, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_aug, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_aug, batch_size=batch_size, shuffle=False)

#Printing the Details
print("Training data:", train_loader)
print("Validation data:", val_loader)
print("Testing data:", test_loader)

"""**Show Images with their Labels**"""

import matplotlib.pyplot as plt
import torchvision
import numpy as np

# Define class names
class_names = [
    'Aesculus chinensis',
    'Albizia julibrissin',
    'Camptotheca acuminata',
    'Flowering cherry',
    'Koelreuteria paniculata',
    'Lagerstroemia indica',
    'Liriodendron chinense',
    'Loropetalum chinense var. rubrum',
    'Magnolia liliflora Desr',
    'Malushalliana',
    'Nandina domestica',
    'Nerium oleander L',
    'Osmanthus fragrans',
    'Photinia serratifolia',
    'Prunus persica',
    'Rhododendron pulchrum',
    'Styphnolobium japonicum'
]

# Function to display images with labels
def imshow(img, labels):
    img = img / 2 + 0.5  # Unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.axis('off')  # Turn off axis
    plt.show()
    print('Actual Labels:', ', '.join(class_names[labels[j]] for j in range(len(labels))))

# Get some random training images
dataiter = iter(train_loader)
images, labels = next(dataiter)

# Show images with labels
imshow(torchvision.utils.make_grid(images), labels)

num_classes = len(class_names)