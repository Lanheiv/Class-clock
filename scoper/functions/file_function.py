import requests
import json
import os

def write_file(path, data):
    with open(path, 'w') as f:
        json.dump(data.json(), f)    

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def delete_files():
    directory = 'scoper/files/raw'
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) and not os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Error deleting {file_path}: {e}')
