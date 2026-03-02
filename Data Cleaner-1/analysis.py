from data_loading import DataLoader
from  data_cleaning import DataCleaner
from  data_analuse import DataAnalyzer

# Load data
loader = DataLoader()
df = loader.load_csv("raw_data.csv")

print("Raw Data:")
print(df)

# Clean data
cleaner = DataCleaner(df)
cleaner.remove_duplicates()
cleaner.fix_data_types()
cleaner.handle_missing_values()
cleaner.remove_invalid_rows()

cleaned_df = cleaner.get_clean_data()

print("\nCleaned Data:")
print(cleaned_df)

# Analyze data
analyzer = DataAnalyzer(cleaned_df)
print("\nBasic Statistics:")
print(analyzer.basic_stats())

print("\nMissing Values Report:")
print(analyzer.missing_values_report())

# Save cleaned data
cleaned_df.to_csv("cleaned_data.csv", index=False)