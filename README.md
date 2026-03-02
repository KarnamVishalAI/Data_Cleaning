# Data Cleaning & Analysis..

## Overview
Real-world datasets are rarely clean. They often contain missing values, incorrect data types, duplicates, and invalid records.

This project is a **Python-based Data Cleaning & Analysis** that demonstrates how to systematically clean messy data and generate basic statistical insights using **Pandas and NumPy**.

The goal of this project is to build **strong data foundations** before moving into Machine Learning.

---

## Features
- Load CSV data safely with error handling
- Remove duplicate records
- Handle missing values using statistical methods
- Fix incorrect data types
- Remove invalid records (e.g., negative salary, underage entries)
- Generate basic statistical summaries
- Export cleaned data for further analysis or ML pipelines

---

## Project Structure
Data-Cleaner-1/
│
├── analysis.py # Main script to run the pipeline
├── data_loading.py # Handles data loading
├── data_cleaning.py # Data cleaning logic
├── data_analyse.py # Data analysis & statistics
├── raw_data.csv # Messy input dataset
├── cleaned_data.csv # Output cleaned dataset
└── pycache/ # Auto-generated Python cache files

## code

---

## Dataset
The input dataset (`raw_data.csv`) intentionally contains:
- Missing values
- Wrong data types
- Duplicate rows
- Negative salary values
- Invalid age entries

This simulates **real-world messy data**, not idealized examples.

---

## Tools & Technologies
- Python
- Pandas
- NumPy

---

## How to Run
1. Clone the repository
2. Make sure `raw_data.csv` is in the project root
3. Run the analysis script:
   ```bash
   python analysis.py
