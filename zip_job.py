## The zip_job.py python script 

import os
import zipfile

# Array of letters
letters = ['a', 'b', 'c', 'd']

# Create txt files
for letter in letters:
    file_path = f'{letter}.txt'
    with open(file_path, 'w') as file:
        file.write(f'This is the content of {letter}.txt')

# Check if all txt files were created
for letter in letters:
    file_path = f'{letter}.txt'
    if not os.path.isfile(file_path):
        print(f'Failed to create {file_path}')
        exit(1)

# Create zip files with txt files
for letter in letters:
    print(os.environ)
    zip_filename = f'{letter}_{os.environ["VERSION"]}.zip'
    zip_file_path = os.path.join('/tmp', zip_filename)
    txt_file_path = f'{letter}.txt'

    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        zip_file.write(txt_file_path, os.path.basename(txt_file_path))

# Check if all zip files were created
for letter in letters:
    zip_filename = f'{letter}_{os.environ["VERSION"]}.zip'
    zip_file_path = os.path.join('/tmp', zip_filename)
    if not os.path.isfile(zip_file_path):
        print(f'Failed to create {zip_file_path}')
        exit(1)

print('All files and zip files were created successfully.')
