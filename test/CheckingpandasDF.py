import pandas as pd 

class DataFrameloader:

    def __init__(self, df:pd.DataFrame):
        self.df = df

    def head(self, n):
        
        return self.df.head(n)
    
    def columns(self):

        return len(self.df.columns)
    
    def get_row(self, n):
        self.n = n
        return self.df.iloc[self.n]
    
    def get_rowElement(self, n, m):
        self.n = n
        self.m = m
        return self.df.iloc[self.n][self.m]