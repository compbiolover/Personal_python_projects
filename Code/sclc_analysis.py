'''
Purpose: Analyze a subset of the bulk RNA-seq data from "Comprehensive genomic profiles of small cell lung cancer" by George et al. (2015) in Nature
'''

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import locale
from scipy import stats

# Set the locale to the user's default (for proper display of numbers and such)
locale.setlocale(locale.LC_ALL, '') 


# Load the data
bulk_data = pd.read_csv('Data/scl_common.csv')
print(bulk_data.head())
print("There are " + str(bulk_data.shape[0]) + " patients and " + str(f'{bulk_data.shape[1] - 13:n}') + " genes in the dataset.")
print("There are " + str(bulk_data.shape[0]) + " rows and " + str(f'{bulk_data.shape[1]:n}') + " total columns in the dataset.")
print(str(bulk_data.columns[13]).upper() + " is the first gene in the dataset.")


# Function to test for normality
def test_normality(data, gene_name, transformation='raw'):
    """
    Perform Anderson-Darling test and return test statistic and critical values.
    """
    result = stats.anderson(data)
    return pd.Series({
        'gene': gene_name,
        'transformation': transformation,
        'statistic': result.statistic,
        'critical_values': result.critical_values,
        'significance_level': result.significance_level
    })


# Test normality for each gene and transformation
results = []
bulk_data_sub = bulk_data.iloc[:, 13:]
for gene in bulk_data_sub.index:
    data = bulk_data_sub.loc[gene]
    results.append(test_normality(data, gene, 'raw'))
    results.append(test_normality(np.log2(data + 1), gene, 'log2'))
    results.append(test_normality(np.log10(data + 1), gene, 'log10'))

results_df = pd.DataFrame(results)

# Find the best transformation for each gene (lowest Anderson-Darling statistic)
best_transformations = results_df.loc[results_df.groupby('gene')['statistic'].idxmin()]

# Print summary
print(best_transformations['transformation'].value_counts())

'''
ax1 = best_transformations['transformation'].value_counts().plot(kind='bar')
ax1.set_xlabel('Transformation')
ax1.set_ylabel('Count')
ax1.set_title('Best Transformations for Each Gene')
ax1.set_xticklabels(['Log2', 'Log10'], rotation=0)
'''


# Plots of the various metadata columns
'''
for column in bulk_data.columns[1:13]:
    ax = bulk_data[column].value_counts().plot(kind='bar')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    ax.set_title('Distribution of ' + column)
    plt.show() 
'''



# Now seeing that our gene expression data is heavily skewed, we will perform a log2 transformation on the data
# Log2 transform the data
metadata = bulk_data.iloc[:, :13]
gene_expr = np.log2(bulk_data.iloc[:, 13:] + 1)

# Combine the metadata and transformed gene expression data
bulk_data_transformed = pd.concat([metadata, gene_expr], axis=1)

# Replace the original dataframe with the transformed one
bulk_data = bulk_data_transformed

# Verify the transformation
print(bulk_data.head())
print(f"Shape of the dataframe: {bulk_data.shape}")

