# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:56:43 2023

@author: Bhargava_Me
"""
#import libraries
import pandas as pd

def read_parquet(location):
    df = pd.read_parquet(location)
    return df

def apply_transformations(df):
    df['vol_moving_avg'] = df['Volume'].rolling(30).mean()
    df['adj_close_rolling_med'] = df['Volume'].rolling(30).median()
    return df

def write_output_data(location, df):
    df.to_parquet(location)
    
if __name__ == '__main__':
    #location = "stage/outpu1.parquet"
    #out_loc = "stage/outpu2.parquet"
    location = input("Enter input file full location with the file name: ")
    out_loc = input("full location where you want to write the outfile file: ")
    df = read_parquet(location)
    df = apply_transformations(df)
    write_output_data(out_loc,df)
