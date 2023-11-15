# apple-contact-export
Python script to extract contacts from an iTunes backup (iOS 13) and save them as a CSV file. Update the file path (line 13) to where your iTunes backup is located, typically at C:\Users\(username)\AppData\Roaming\Apple Computer\MobileSync\Backup\. Look for the file named 31bb7ba8914766d4ba40d6dfb6113c8b614be442. You can also customize the output file's path and name as needed.

# Improvements

- Use Context Managers for File and Database Operations: This ensures that resources are properly managed and released, even if an error occurs.

- Streamline Database Querying and Data Handling: Instead of multiple lists, use a single list of dictionaries to store the contact information. This simplifies data handling and makes the code more readable.

- Parameterize Database Path: Instead of hardcoding the database path, it's better to use a function parameter or command-line argument. This makes the script more flexible.

- Efficient Data Writing to CSV: Use the CSV writer directly in the data processing loop to avoid holding all data in memory.

- Improve Comments and Documentation: Clear comments and documentation help in understanding the purpose and functionality of the script.

- Error Handling: Add basic error handling for database and file operations.