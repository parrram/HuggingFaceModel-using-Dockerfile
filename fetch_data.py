import requests
import json

response = requests.get('https://huggingface.co/api/models')

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")

data = response.json()

print("Sample data received from API:")
for item in data[:5]:
    print(item)

top_models = sorted(
    [model for model in data if 'downloads' in model and 'name' in model],
    key=lambda x: x['downloads'], 
    reverse=True
)[:10]

with open('report.txt', 'w') as f:
    for model in top_models:
        f.write(f"{model['name']}: {model['downloads']}\n")
