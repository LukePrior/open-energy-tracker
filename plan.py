from mimetypes import guess_extension
import os
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'x-v': '3'}

def get_data(url):
    r = requests.get(url, headers=headers)
    response = r.json()

    return response

# https://stackoverflow.com/a/25851972/9389353
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

raw_file = open("brands/brands.json", "r")
brands = json.load(raw_file)
raw_file.close()

changed_product = 0

for file in os.listdir('brands/plans/'):
    id = file.replace(".json","")

    raw_file = open("brands/plans/"+file, "r")
    brand = json.load(raw_file)
    raw_file.close()

    if 'data' not in brand:
        continue

    folder = "brands/plan/" + id
    if not os.path.exists(folder):
        os.makedirs(folder)