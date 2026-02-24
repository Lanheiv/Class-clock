from datetime import datetime
import requests
import json
import os

def write_file(path, data):
    if hasattr(data, "json"):
        data = data.json()
    with open(path, 'w') as f:
        json.dump(data, f, indent=2) 

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

def write_errore_file(data):
    with open("scoper/files/error_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] {data}\n")