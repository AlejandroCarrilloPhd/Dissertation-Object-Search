# Creating the cleaning file based on my original R script 
# Libraries 
import pandas as pd
import numpy as np 

# Testing the function
# Import the csv file and call it df
df = pd.read_csv('C:/Users/alexc/OneDrive/Desktop/Dissertation-Object-Search/Study 1/data/10322_VAST1_2023-11-01_14h13.15.208.csv')


#### SECTION 1: Long Form ####

# Start by writing the function to do long form cleaning 
# WITH EACH ROW REPRESENTING A SEPARATE TRIAL, SUITABLE FOR JUDD,
# WESTFALL, & KENNY 2012 RANDOM FACTOR ANALYSIS.
def longformVASTcleaning(data_original):
    # copy the original data to a new dataframe
    df = data_original.copy()
    # remove practice trials 
    df.drop(range(0,12), inplace=True)
    # Remove the final text row
    df.drop(372, inplace=True )
    # Select specific variables for analysis
    # Extract the selected columns and assign to a new dataframe
    df2 = df[["Dstim_1_image", "Dstim_1_position",
    "Dstim_2_image", "Dstim_2_position",
    "Dstim_3_image", "Dstim_3_position",
    "Dstim_4_image", "Dstim_4_position",
    "Dstim_5_image", "Dstim_5_position",
    "Dstim_6_image", "Dstim_6_position",
    "Dstim_7_image", "Dstim_7_position",
    "Dstim_8_image", "Dstim_8_position",
    "Dstim_9_image", "Dstim_9_position",
    "Dstim_10_image", "Dstim_10_position",
    "Dstim_11_image", "Dstim_11_position",
    "Dstim_12_image", "Dstim_12_position",
    "Dstim_13_image", "Dstim_13_position",
    "Dstim_14_image", "Dstim_14_position",
    "Dstim_15_image", "Dstim_15_position",
    "Dstim_16_image", "Dstim_16_position",
    "Dstim_17_image", "Dstim_17_position",
    "Dstim_18_image", "Dstim_18_position",
    "Dstim_19_image", "Dstim_19_position",
    "target_object", "target_object_position",
    "target_type", "pretrial_text",
    "setSize", "response",
    "rt", "correct",
    "face", "race",
    "condition_name", "block_order", "participant", "gridCheck",	
    "mouseRT",	"mouseCorr",	"Tnum_position",	"Dnum_position",	
    "Dnum2_position","Dnum3_position"]].copy()
    # Recode reaction time from seconds to milliseconds
    df2['rt'] = (df2['rt'] * 1000).round(0)

    # Create additional variables for error analysis and time restrictions
    # Mark reaction times less than 300ms as NA(considered too quick)
    df2['rt2'] = np.where(df2['rt'] < 300, np.nan, df2['rt'])
    # Mark incorrect trials as NA in reaction time
    df2['rt3'] = np.where(df2['correct'] == "FALSE", np.nan, df2['rt2'])
    # Mark reaction times over 9999ms as NA (considered too long)
    df2['rt4'] = np.where(df2['rt3'] > 9999, np.nan, df2['rt3'])
    # Count the number of timeouts (reaction time over 9999ms)
    df2['number_timeouts'] = (df2['rt'] > 10000).sum()
    # Mark participants with excessive timeouts (over 1/8 of total 360 trials)
    df2['over_timeouts'] = np.where(df2['number_timeouts'] > 45, 1, 0)
    # Count the number of errors
    df2['number_errors'] = (df2['correct'] == "FALSE").sum()
    # Count the numbers of mouse selection errors 
    df2['mouse_number_errors'] = (df2['correct'] == "FALSE").sum()
    # Reorder columns for better data organization 
    all_columns_df2 = df2.columns.tolist()
    dstim_columns_df2 = [col for col in all_columns_df2 if col.startswith('Dstim')]
    non_dstim_columns_df2 = [col for col in all_columns_df2 if col != 'participant' and col not in dstim_columns_df2]
    ordered_columns_df2 = ['participant'] + non_dstim_columns_df2 + dstim_columns_df2
    df2 = df2[ordered_columns_df2]
    return df2
    pass 

