import pandas as pd

def read_excel_file(path: str) -> pd.DataFrame:
    """
    This function reads an Excel file and returns a DataFrame.
    
    Parameters:
    path (str): Path to the Excel file
    
    Returns:
    pd.DataFrame: DataFrame containing the data from the Excel file
    """
    try:
        data = pd.read_excel(path)
        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def generate_email_address(names: pd.Series) -> pd.Series:
    """
    This function generates email addresses from a list of names.
    
    Parameters:
    names (pd.Series): Series of names
    
    Returns:
    pd.Series: Series of email addresses
    """
    email_addresses = names.str.replace(' ', '.').str.lower() + '@example.com'
    return email_addresses

def save_files(data: pd.DataFrame, output_path: str):
    """
    This function processes the data and saves it into separate files for boys, girls, and special characters.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the student data
    output_path (str): Path to the output directory
    """
    # Filter data based on gender
    boys = data[data['Gender'] == 'Male']
    girls = data[data['Gender'] == 'Female']
    
    # Filter data containing special characters in the name
    special_chars = data[data['Name'].str.contains('[^a-zA-Z0-9 ]', regex=True)]
    
    # Save data into separate files
    boys.to_csv(output_path + 'boys.csv', index=False)
    girls.to_csv(output_path + 'girls.csv', index=False)
    special_chars.to_csv(output_path + 'special_characters.csv', index=False)