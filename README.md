
# Inferring Actions from Video Demonstration using IDM 

## Step 1

Clone the repository


## Step 2

Download the datasets from here - [dataset](https://drive.google.com/drive/folders/16GyukwTnQFjILKkuYM3dGdFBen76Goel?usp=sharing) 

Keep the `data` and `validation` folder in your root directory of the project. 

## Step 3 

Install necessary packages - 

* PyTorch [(Installation Instruction)](https://pytorch.org/get-started/locally/)
* Numpy
* Tensorboard
* os 
* gc 

## Step 4 

Install jupyter lab and run the local jupyter server by following the [instructions](https://jupyter.org/install) 

## Step 5 

Open the `IDM.ipynb` file. Configure the adjustable variables and then run the script.  

# For custom data generation 

## Step 1

Setup Airsim on Unreal Engine using the instructions here - [Windows](https://microsoft.github.io/AirSim/build_windows/), [Linux](https://microsoft.github.io/AirSim/build_linux/), [macOS](https://microsoft.github.io/AirSim/build_macos/) 

## Step 2

Run the airsim in [computer vision](https://microsoft.github.io/AirSim/image_apis/) mode. And run either `DataCollectionPipeline.py` for keyboard controlled data collection or `RandomDataCollectionPipeline.py` for automated data collection. 
