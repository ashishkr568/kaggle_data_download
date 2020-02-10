# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:10:50 2020

@author: ashishkr568
"""

# Code to
#   * Get the list of competitions from kaggle
#   * Get the list of datasets from kaggle
#   * Download a dataset from kaggle and unzip it 


# Import packages
import pandas as pd
import kaggle

# Get list of active competitions in kaggle


#------Function to clean the downloaded list and convert it to dataframe------#
def kaggle_ds_clean(ds_list):
    # Convert comp_list(test.SList) to pandas dataframe
    # to do this we need to replace all characters with multiple spaces with ';'
    # and then split it by ";" 
    df=pd.DataFrame(data=ds_list)[0].str.replace(r'[^\S]{2,}',";").str.split(";", expand=True)
    
    # Clean dataframe - Remove unnecessary rows and columns and set header
    # Delete last column
    df=df.drop(len(df.columns)-1,axis=1)
    
    # Set header and delete unnecessary rows and reset index
    df.columns=df.iloc[0]
    df=df.drop([0,1],axis=0)
    df=df.reset_index(drop=True)
    
    return df
#-----------------------------------------------------------------------------#
    

#---Get list of competitions from kaggle, clean it and convert to dataframe---#
kaggle_comp_list= !kaggle competitions list
comp_list_df=kaggle_ds_clean(kaggle_comp_list)
#-----------------------------------------------------------------------------#


#-----Get list of datasets from kaggle, clean it and convert to dataframe-----#
kaggle_doc_list= !kaggle datasets list
kaggle_doc_df=kaggle_ds_clean(kaggle_doc_list)
#-----------------------------------------------------------------------------#

#---------------Download a competition dataset from kaggle--------------------#

# We can download dataset from kaggle by providing the competition name and 
# output folder name. The output folder will be created in the current project directory

# -c: competition name
# -p: path to where the file should be saved

# In the below example we are downloading data for digit recognizer competition
!kaggle competitions download -c digit-recognizer -p downloaded_data

# To unzip the files we can use shutil package in python
import shutil
shutil.unpack_archive("downloaded_data/digit-recognizer.zip","downloaded_data/digit_recognizer","zip")
#-----------------------------------------------------------------------------#

# Remove unnecessary variables
del(kaggle_doc_list,
    kaggle_comp_list)
