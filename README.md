# Machine_Learning_PPE_Detection

Hi All, 

I''m Khanh Hoang

This my Machine Learning Project as a student at Ho Chi Minh university of technology

To run this project, I recommend you to use anaconda prompt to run env. This project is for beginner in AI Domain, some command to run this

* conda env list -> List all the environment variables
* conda activate <environment>
* conda deactivate -> Deactivate environment

PPE Segmentation
Personal Protective Equipment (PPE) Segmentation is a computer vision project aimed at detecting and segmenting PPE elements (such as helmets, vests, gloves, goggles, etc.) in images or videos of people. The goal is to improve workplace safety monitoring by automatically identifying the presence or absence of necessary safety gear in real time.


Table of Contents
Overview
Features
Installation
Usage
Data
Model Training
Evaluation
Results
Contributing
License
Overview
Workplace safety is critical, especially in hazardous environments such as construction sites, factories, and labs. PPE Segmentation leverages deep learning models to detect and segment different PPE items, ensuring safety compliance and preventing accidents. By identifying PPE in images or videos, this project aims to reduce human error in manual inspections and assist in automatic PPE verification.

Features
Multi-Class Segmentation: Supports detection and segmentation of various PPE items, such as helmets, vests, gloves, and glasses.
Real-Time Processing: Capable of processing video feeds in real time.
Flexible Model Training: Can train on new datasets or fine-tune pre-trained models to fit specific PPE detection needs.
Extensible Pipeline: Easily adaptable for custom PPE classes or other object detection and segmentation needs.
Installation
Prerequisites
Python 3.7+
PyTorch
OpenCV
NumPy
Matplotlib
(Optional) CUDA for GPU support
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/PPE-Segmentation.git
cd PPE-Segmentation
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Running Pre-trained Model
To run the model on images or videos:

bash
Copy code
python predict.py --input path_to_input_image_or_video --output path_to_output_directory
Training
To train a model from scratch or fine-tune a pre-trained model:

bash
Copy code
python train.py --config config.yaml
Configuration
Configuration settings are stored in config.yaml. Modify this file to adjust parameters such as dataset path, learning rate, batch size, and model architecture.

Data
This project requires labeled datasets with PPE classes for training. Each image should have segmentation masks for each PPE item. You can either use a public dataset or create a custom dataset.

Example datasets:
Open Images Dataset with custom labels for PPE.
COCO Dataset with annotations.
Model Training
To train the segmentation model, use the command provided in the Usage section, and ensure your configuration in config.yaml matches your dataset setup.

Prepare the Data: Ensure images and masks are properly labeled and split into training, validation, and test sets.
Training: Start training with the train.py script. The model will save checkpoints and log metrics for each epoch.
Fine-tuning: Fine-tune the model with pre-trained weights for better performance on specific datasets.
Evaluation
Evaluate the model's performance using the evaluate.py script:

bash
Copy code
python evaluate.py --model path_to_model_checkpoint --dataset path_to_test_dataset
Evaluation metrics include:

Mean Intersection over Union (mIoU)
Pixel Accuracy
Precision/Recall for each PPE class
Results
Results of model evaluation are saved in the results/ directory, where you can view the mIoU and other metrics for each class. Example output images or segmented masks can also be saved and visualized for qualitative analysis.

Contributing
We welcome contributions to improve the model and add more features. Please fork the repository and create a pull request for any enhancements, bug fixes, or new features.

Fork the Project
Create a new Branch (git checkout -b feature/YourFeature)
Commit your Changes (git commit -m 'Add YourFeature')
Push to the Branch (git push origin feature/YourFeature)
Open a Pull Request
License
Distributed under the MIT License. See LICENSE for more information.
