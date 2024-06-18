import pandas as pd

# Path to the Excel file
excel_file = r'path_to_your_file.xls'

# Read the first sheet of the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Save the DataFrame to a CSV file
csv_file = r'path_to_your_file.csv'
df.to_csv(csv_file, index=False)
