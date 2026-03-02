class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        return self.df.describe()

    def missing_values_report(self):
        return self.df.isnull().sum()