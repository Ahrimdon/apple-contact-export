'''
This script extracts contacts from an iTunes backup for an iPhone with iOS 13 and saves it as a CSV file.
The file '31bb7ba8914766d4ba40d6dfb6113c8b614be442' should be under the 31 folder.
Before running, ensure you have a backup of the iTunes backup file.
'''

import sqlite3
import csv
import sys

def extract_contacts(db_path, output_csv_path):
    """
    Extracts contacts from the specified iTunes backup database and writes them to a CSV file.
    Args:
    db_path: str - Path to the iTunes backup database file.
    output_csv_path: str - Path to the output CSV file.
    """
    try:
        with sqlite3.connect(db_path) as conn, open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            cursor = conn.cursor()
            query = '''
            SELECT ABPerson.First, ABPerson.Last, ABMultiValue.value
            FROM ABPerson
            INNER JOIN ABMultiValue ON ABPerson.ROWID = ABMultiValue.record_id
            WHERE ABPerson.First != 'SPAM'
            '''
            cursor.execute(query)

            fieldnames = ['Given name', 'Family Name', 'Phone 1 - Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for first, last, number in cursor:
                writer.writerow({
                    'Given name': first or ' ',
                    'Family Name': last or ' ',
                    'Phone 1 - Value': number
                })

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Replace with the path to your database and output CSV file.
db_path = 'C:\\path\\to\\input\\31bb7ba8914766d4ba40d6dfb6113c8b614be442'
output_csv_path = 'C:\\path\\to\\output\\contacts.csv'

extract_contacts(db_path, output_csv_path)