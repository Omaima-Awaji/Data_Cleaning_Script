# Data Cleaning Script 🧹

A Python script that cleans messy customer data from a CSV file, validates emails and phone numbers, standardizes dates, and generates a cleaning report.

## Features
- Cleans and standardizes column names
- Strips extra whitespace from all fields
- Fills missing values based on config settings
- Removes duplicate rows
- Validates and lowercases email addresses
- Cleans and formats phone numbers to +1XXXXXXXXXX
- Parses and standardizes dates across multiple formats
- Exports cleaned data to a new CSV file
- Generates a JSON cleaning report with stats

## Project Files
- data_cleaning.py - main script
- config.json - settings for fill values, date format, and duplicate handling
- messy_customer.csv - sample input file with messy data
- cleaning_report.json - example output report

## How to Use
Run the script:

python data_cleaning.py

The script will automatically generate:
- cleaned_customers.csv
- cleaning_report.json

## Config File
The config.json file controls the cleaning behavior:

{
    "fill_missing_text": "N/A",
    "drop_duplicates": true,
    "date_format": "%Y-%m-%d"
}

## Output Example
Cleaning Report:
- total_rows_original: 20
- total_rows_cleaned: 17
- duplicates_removed: 3
- invalid_emails: 2
- invalid_phones: 1
- invalid_dates: 0

## Requirements
- Python 3.x
- pandas

## Installation
pip install pandas
