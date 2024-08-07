import re
import os

# Function to search for a phone number pattern in a file
def searchPhone(file_path, pattern=r'\d{3}-\d{3}-\d{4}'):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            match = re.search(pattern, text)
            if match:
                return match.group()
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
    return None

# List to store results
results = []

# Walk through the directory and search for the pattern in each file
for folder, sub_folders, files in os.walk(os.getcwd() + '/extracted_content'):
    for file_name in files:
        full_path = os.path.join(folder, file_name)
        result = searchPhone(full_path)
        if result:
            results.append((folder, file_name, result))
        print(file_name)

# Print results
for folder, file_name, pqp in results:
    print(f"The file {file_name} is located in the folder {folder}, and the Phone Number is: {pqp}")