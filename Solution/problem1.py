# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:19:07 2023

@author: Bhargava_Me

Problem 1:
"""
#import libraries
import pandas as pd
import numpy as np
import os
import dask.dataframe as dd

def reading_metadata(location):
    #reading metadata information
    meta_df = pd.read_csv(location)

    #keeping_only_reqd_cols from metadata_df
    meta_df = meta_df[['Security Name', 'Symbol']]
    return meta_df
    
def get_file_details(directory):
    nested_dir = os.listdir(directory)
    files = []
    for file in os.listdir(directory+"/"):
        files.append((file, directory+"/"+file))
    return files

def read_and_add(file_info):
    data = dd.read_csv(file_info[1])
    data["Symbol"] = file_info[0][:-4]
    return data

def dask_read(files):
    dfs = [read_and_add(file_info) for file_info in files]
    df = dd.concat(dfs)
    df = df.compute()
    return df

def merge(data, meta_df):
    columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume", "Symbol", "Security Name"]
    merged_df = meta_df.merge(data, on='Symbol')
    merged_df = merged_df[columns]
    return merged_df
def write_to_parquet(df, out_loc):
    df.to_parquet(out_loc)

if __name__ == '__main__':
    #location = "symbols_valid_meta.csv"
    #directory = "archive"
    #out_loc = "stage/outpu1.parquet"
    location = input("Enter metadata file full location with the file name: ")
    directory = input("enter the directory where etfs and stocks data is present: ")
    out_loc = input("full location where you want to write the outfile file: ")
    meta_df = reading_metadata(location)
    files = get_file_details(directory)
    df = dask_read(files)
    df = merge(df, meta_df)
    write_to_parquet(df, out_loc)
    