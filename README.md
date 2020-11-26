# POS-Tagging

## About
A POS Tag predictor bulit using the Hidden Markov Model

## Guidelines to run the code
### Step 1
If u have the zip file then extract it in a folder
                      OR
Clone from the Repository:- git clone https://github.com/rishichordia/POS-Tagging.git

### Step 2
Preprocess the train and the test data by running the bash script:- ./do

### Step 3
Now run the model on the test-data set using python.We can train both the naive and the HMM model

For the HMM model:-

Type the commnand:- python3 Confusion_Matrix.py hmm

For the basic probability model:-

Type the commnand:- python3 Confusion_Matrix.py hmm 

### Step 4
Now to analyze the performance of the model run the folloeing command

python3 Performance.py

