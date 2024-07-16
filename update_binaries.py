#!/usr/bin/env python3

import requests
import os

print("Downloading libvinput library")

base_url = 'https://github.com/xslendix/libvinput/releases/latest/download/'
files = ['libvinput.dll', 'libvinput.dylib', 'libvinput.so']
save_dir = './vinput/lib/'

os.makedirs(save_dir, exist_ok=True)

for file in files:
    url = base_url + file
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(save_dir, file) + '.dat'
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded {file} successfully.')
    else:
        print(f'Failed to download {file}. Status code: {response.status_code}')

