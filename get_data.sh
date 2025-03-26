#!/bin/bash

# Create directories if they don't exist
mkdir -p ckp
mkdir -p NeuroMotion/MSKlib/models

# Download the files using gdown and specifying the output file for each
gdown 1RIYnYxLkBZ9_7MJQgQBSjAk_oXBTqY0b -O ckp/model_linear.pth
gdown 1xxeXF4RS7qH-kq3yrfCiWIQ7DemMounr -O ckp/muap_example.pkl
gdown 10PoLwJcHoS8ZRvqlExENpt3tt2Vus72s -O NeuroMotion/MSKlib/models/poses.csv
gdown 1HD3UQFgaxSTsZIFW04bp-pLmn8UROBEp -O NeuroMotion/MSKlib/models/ARMS_Wrist_Hand_Model_4.3.zip

unzip NeuroMotion/MSKlib/models/ARMS_Wrist_Hand_Model_4.3.zip -d NeuroMotion/MSKlib/models/