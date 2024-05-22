import pandas as pd
import tasks
import logging
from time import time

INPUT_FILE_PATH = 'input_data_files/'
OUTPUT_FILE_PATH = 'output_data_files/'

if __name__ == '__main__':
    # Read the Excel file
    data = tasks.read_excel_file(INPUT_FILE_PATH + 'TestFiles.xlsx')
    
    # Generate email addresses
    data['Email'] = tasks.generate_email_address(data['Name'])
    
    # Save data into separate files for boys, girls, and special characters
    tasks.save_files(data, OUTPUT_FILE_PATH)
    
    print("Data processing and file separation completed successfully.")