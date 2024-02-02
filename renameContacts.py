import os
import csv
import re

def format_number(raw_number):
    # Remove all non-numeric characters for comparison
    return re.sub(r'[^\d]', '', raw_number)

def load_contact_mappings(csv_path):
    mapping = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            raw_number = row['Phone 1 - Value']
            formatted_number = format_number(raw_number)
            mapping[formatted_number] = row['Name']
    return mapping

def rename_files_in_directory(directory, csv_path):
    contact_mappings = load_contact_mappings(csv_path)

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            # Extract all phone numbers from the filename
            phone_numbers = re.findall(r'\+(\d+)', filename)
            new_names = []
            for phone_number in phone_numbers:
                # Format each number for matching
                formatted_number = format_number(phone_number)
                # Append the name corresponding to the phone number
                if formatted_number in contact_mappings:
                    contact_name = f"{contact_mappings[formatted_number]} ({phone_number})"
                    new_names.append(contact_name)
            
            # Skip renaming if no contact names were found
            if new_names:
                # Create a new filename with all the corresponding contact names
                new_filename = ", ".join(new_names) + ".html"
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                # Avoid FileExistsError by ensuring a unique new filename
                counter = 1
                while os.path.exists(new_path):
                    base, extension = os.path.splitext(new_filename)
                    new_filename = f"{base} ({counter}){extension}"
                    new_path = os.path.join(directory, new_filename)
                    counter += 1
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed "{filename}" to "{new_filename}"')

# Set the path to your directory and CSV file
directory_path = 'C:/Users/ianco/Desktop/iMessage Export/imessage_export' # Change to your directory path
csv_file_path = 'C:/Users/ianco/Desktop/iMessage Export/contacts.csv' # Change to your CSV file path

rename_files_in_directory(directory_path, csv_file_path)