Video Caption Generation using Sequence-to-Sequence Model

This is a code repository for the Video Caption Generation using Sequence-to-Sequence Model. The repository contains three Python files:

model.py: This file contains the implementation of the Sequence-to-Sequence Model for video caption generation.
training.py: This file is used to train the model using video features and corresponding captions.
testing.py: This file is used to generate captions for new videos using the trained model.
hw2_seq2seq.sh: shell script to run the model.

Program Testing Instructions
Description
Please follow the steps carefully.

Installation
First clone the repository to your local machine.

Testing
To test the program, please follow these instructions carefully:

Add the test video features to a folder "testing_data"

Edit the shell script and replace $path1 with the path to the testing_data folder, and $path2 with the location where you want the output .txt file to be saved.

Download the model from the Google Drive link that I shared in the model_link file located in the "Model" folder. Please note that you must also put the picket_data.pickle file in the same "Model" folder.

Run the shell script using the following command: ./run.sh.

Folder Structure
Model: This folder contains the pre-trained model

Author
The code is written by Maitreyee Narkhede
