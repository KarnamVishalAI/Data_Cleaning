import pandas as pd

class DataLoader:
    def load_csv(self, file_path):
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error loading file:", e)