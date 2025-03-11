
# Utility to read data from CSV files


import pandas as pd
import os

class CSVReader:
    @staticmethod
    def read_csv(file_path):
        # Read data from a CSV file
        try:
            # Check if file exists
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"CSV file not found: {file_path}")
                
            # Read CSV into pandas DataFrame
            df = pd.read_csv(file_path)
            
            # Check if DataFrame is empty
            if df.empty:
                raise ValueError(f"CSV file is empty: {file_path}")
                
            return df
        except Exception as e:
            raise Exception(f"Error reading CSV file: {e}")
    
    @staticmethod
    def get_search_query(file_path, row_index=0):
        
        # Get a search query from CSV file
        
        df = CSVReader.read_csv(file_path)
        
        if 'search_query' not in df.columns:
            raise ValueError("CSV file does not contain 'search_query' column")
            
        if row_index >= len(df):
            raise IndexError(f"Row index {row_index} is out of bounds for CSV with {len(df)} rows")
            
        return df.loc[row_index, 'search_query']