import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def fix_data_types(self):
        self.df["age"] = pd.to_numeric(self.df["age"], errors="coerce")
        self.df["salary"] = pd.to_numeric(self.df["salary"], errors="coerce")

    def handle_missing_values(self):
        self.df["age"].fillna(self.df["age"].mean(), inplace=True)
        self.df["salary"].fillna(self.df["salary"].median(), inplace=True)

    def remove_invalid_rows(self):
        self.df = self.df[self.df["age"] >= 18]
        self.df = self.df[self.df["salary"] >= 0]

    def get_clean_data(self):
        return self.df