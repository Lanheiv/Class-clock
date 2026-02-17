import requests
import json

def get_post_data(url, headers, data_path):
    session = requests.Session()

    session.get(url)

    return session.post(
        url + data_path[0],
        headers=headers,
        json=data_path[1],
    )