# Creating the cleaning file based on my original R script 
# Libraries 
import pandas as pd

# Testing the function
# Import the csv file and call it df
df = pd.read_csv('Study 1/data/10322_VAST1_2023-11-01_14h13.15.208.csv')
# View the excel_file's sheet names
print(df)

#### SECTION 1: Long Form ####

# Start by writing the function to do prepare the data
def longformVASTcleaning(data_original):
    # copy the original data to a new dataframe
    df = data_original
    # remove practice trials 

    pass 