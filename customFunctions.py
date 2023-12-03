import pandas as pd
import numpy as np

"""
Description: This file provides quick and easy functions to produce different tables from the dataset, along with some easy functions.
Author: Fahim Muntasir, Research Engineer, AIMS Lab, IRIIC, UIU.

"""


def show_percent(data, column_name:str):
    """Shows percent of values
    author: Fahim Muntasir
    date: 2/12/23
    """
    
    value_counts = data[column_name].value_counts()
    total_samples = len(data)
    percentages = (value_counts / total_samples) * 100
    result_df = pd.DataFrame({'Counts': value_counts, 'Percentages': percentages})
    return result_df



def single_column_categorical_table(dataframe, index_column:str, categorical_column:str):
    """
    Created by: Fahim Muntasir
    Date: 24/11/2023
    
    dataframe: the main dataset
    index_column: Based on which index the values are calculated.
    categorical_column: Calculation for the selected categorical column
    return: returns a table with both count and percentages concatenated in a table.
    """
    df_subset = dataframe[[index_column, categorical_column]]
    count_Table = pd.crosstab(index=df_subset[index_column], columns=df_subset[categorical_column],  margins = True, margins_name = 'Total')
    
    percent_table = (count_Table/count_Table.iloc[-1,-1])*100
    percent_table.rename(index = lambda x: f"{x} (%)" , inplace = True)
    

    # Concatenate with keys to distinguish between count and percentage sections
    result_table = pd.concat([count_Table, percent_table], keys=['Count', 'Percentage'], axis='index')

    # Reorder the index to have the 'Percentage' rows after the 'Count' rows for each category
    result_table = result_table.sort_index(level=0)
    result_table = result_table.round(decimals=2)

    return result_table
    