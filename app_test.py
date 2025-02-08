import requests

url = "http://127.0.0.1:5000/predict"
data = {"input": 5}

response = requests.post(url, json=data)
print(response.json())  # Should print: {"prediction": 10}