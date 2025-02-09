# Load CSV to SQLite3 and Analyze McDonald's Nutrition Data

## Overview
This project reads a CSV file containing McDonald's nutrition data, loads it into an SQLite3 database using Pandas, and performs basic data analysis and visualization.

## Features
- Loads McDonald's nutrition data from a CSV file.
- Stores data in an SQLite3 database.
- Retrieves data using SQL queries.
- Performs statistical analysis using Pandas.
- Visualizes sodium content in different food categories with Seaborn.

## Requirements
Ensure you have the following installed before running the script:
- Python 3.x
- Pandas
- SQLite3
- Matplotlib
- Seaborn

You can install the dependencies using:
```bash
pip install pandas matplotlib seaborn
```

## Usage
1. Place `menu.csv` in the same directory as the script.
2. Run the Python script:
   ```bash
   python load_csv_to_sqlite.py
   ```
3. The script will:
   - Read the CSV file
   - Store data in SQLite
   - Retrieve and display data
   - Generate a scatter plot of sodium content

## File Structure
```
📂 Project Folder
├── menu.csv               # Nutrition data file
├── load_csv_to_sqlite.py   # Main Python script
├── README.md               # Project documentation
```

## Example Output
The script will display statistical summaries of the dataset and generate a plot showing sodium content across different food categories.

## Improvements & Future Enhancements
- Add error handling for missing files or incorrect data.
- Optimize SQL queries for better performance.
- Expand visualization to include other nutritional factors.


