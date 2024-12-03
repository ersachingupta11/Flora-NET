# Title 
Integrating Dual Coordinate Attention with Adaptive Kernel-Based Convolution Network for Medicinal Flower Identification
 
# Problem Description
Medicinal flowers are a vital part of several domains like healthcare, cosmetics, and many more. Accurate classification of medicinal flowers is necessary to develop precise herbs for disease ailments. Several deep learning methods have been deployed for classification, but they fail to capture the long-range dependencies of the feature maps and hierarchical feature maps among the flora-images.

# Proposed Study
The proposed Flora-NET contains three phases: Data-processing, where the images have been uniformly resized to 224 x 224, followed by the conventional image augmentation methods. The second phase includes the DCAFE and inv-FR modules for better feature extraction and refinement. The third phase contains the classification module for flower identification.

# Result
The proposed Flora-NET method has been trained and tested on two publicly available flower datasets: Urban Street and Medicinal Flower Blossom datasets. The results affirmed that the proposed method overshadows the existing methods for precise medicinal flower classification.

# Repo Structure
The Flora-NET method has the following structure:
- `.py files`: `.py` scripts with training, inference, and image processing functions
- `Exemplary Datafiles/`: input data (images are not included due to size constraints) from each class of Urban Street and Medicinal Blossom datasets
- `Dataset Link/`: Contains the URLs for the public datasets and can be downloaded  [Urban Street](https://www.sciencedirect.com/science/article/pii/S0168169923002405) and [Medicinal Blossom](https://www.sciencedirect.com/science/article/pii/S0168169923002405)
- `pretrainedmodels/`: weights and configurations of models pre-trained on external datasets

# Install Dependencies
```
!pip install -r requirement.txt
```
# Github Cloning
```
!pip install git+https://github.com/your-repository/involution.git
```

# Linking Google Drive containing Flower Images 
```
from google.colab import drive
drive.mount('/content/drive')
# List files in a specific folder
!ls /content/drive/MyDrive
```

# Resize and Augmentation
```
!python resize.py
!python conventional_augmentation.py
```

# Dataset Splitting into Training, Validation and Testing (80:10:10)
```
!python data_split.py
```
# Execute Model
```
!python Flora_NET.py --epochs 100 --learning_rate 0.001 --batch_size 16
```
