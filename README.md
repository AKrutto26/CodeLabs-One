# Student Names Processing Project

## Overview
This project processes student names from an Excel file, generates email addresses, filters names with special characters, and calculates name similarities using LABSE (Language-agnostic BERT Sentence Embedding). The results are saved into separate Excel files for boys, girls, special character names, and name similarities.

## Directory Structure


## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python installed (preferably 3.6+).
3. Install the necessary libraries by running:

```bash
pip install pandas transformers torch

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python installed (preferably 3.6+).
3. Install the necessary libraries by running:

```bash
pip install pandas transformers torch
python main.py
| Name        | Gender | Email             |
|-------------|--------|-------------------|
| John Doe    | Male   | john.doe@school.com |
| ...         | ...    | ...               |
| Name        | Gender | Email             |
|-------------|--------|-------------------|
| Jane Doe    | Female | jane.doe@school.com |
| ...         | ...    | ...               |
| Name        | Gender | Email             |
|-------------|--------|-------------------|
| J@ne Doe    | Female | j@ne.doe@school.com |
| ...         | ...    | ...               |
| Name1       | Name2        | Similarity |
|-------------|--------------|------------|
| John Doe    | Jane Doe     | 0.87       |
| ...         | ...          | ...        |



This `README.md` file provides a clear overview of the project, instructions for setting up the environment, running the script, and understanding the output files. Adjust the contact information and any other details specific to your project as needed.

