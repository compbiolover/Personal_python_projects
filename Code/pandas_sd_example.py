# Description: This script is used to show students how to properly get standard deviation of a dataset

# Importing the libraries
import pandas as pd
import numpy as np
import os

# Get the current working directory so we can read the file
print("Current directory: " + os.getcwd())

# Load the data
df = pd.read_csv('Personal_Python_projects/Data/virus_miniset0.txt', sep= '\t')
print(df.head())

# Calculate the standard deviation of the 'M-12' column
print("Standard deviation of 'M-12' and 'M-36' columns:\n" + str(df[['M-12', 'M-36']].std()))