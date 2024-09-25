'''
Purpose: Analyze a subset of the bulk RNA-seq data from "Comprehensive genomic profiles of small cell lung cancer" by George et al. (2015) in Nature
'''

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import locale

# Set the locale to the user's default (for proper display of numbers and such)
locale.setlocale(locale.LC_ALL, '') 



# Load the data
bulk_data = pd.read_csv('Data/scl_common.csv')
print(bulk_data.head())
print("There are " + str(bulk_data.shape[0]) + " patients and " + str(f'{bulk_data.shape[1] - 13:n}') + " genes in the dataset.")
print("There are " + str(bulk_data.shape[0]) + " rows and " + str(f'{bulk_data.shape[1]:n}') + " total columns in the dataset.")
print(str(bulk_data.columns[13]).upper() + " is the first gene in the dataset.")

# Plot the distribution of the first gene
# Create a new figure
for i in range(13, len(bulk_data.columns)):
    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.hist(bulk_data[bulk_data.columns[i]], bins=50, color='blue', alpha=0.7)
    ax1.set_title('Distribution of ' + str(bulk_data.columns[i]).upper())
    ax1.set_xlabel('Expression')
    ax1.set_ylabel('Frequency')
    ax2.hist(np.log2(bulk_data[bulk_data.columns[i]] + 1), bins=50, color='red', alpha=0.7)
    ax2.set_title('Log2 Distribution of ' + str(bulk_data.columns[i]).upper())
    ax2.set_xlabel('Log2 Expression')
    ax2.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()