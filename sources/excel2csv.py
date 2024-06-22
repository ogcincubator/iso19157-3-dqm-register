
import pandas as pd
import openpyxl

def excel_to_csv(excel_file):
    xls = pd.ExcelFile(excel_file)
    sheet_names = xls.sheet_names
    
    for sheet_name in sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        csv_filename = f"{sheet_name}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Converted '{sheet_name}' to '{csv_filename}'")

if __name__ == "__main__":
    excel_file = "../ISO19157-3/ISO19157-3_DQM.xlsx"  # Replace with the path to your Excel file
    excel_to_csv(excel_file)