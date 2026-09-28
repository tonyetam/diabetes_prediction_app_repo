import requests

# fastapi endpoint url
API_URL = "http://127.0.0.1:8000/predict"

payload = {
    "Pregnancies": 2,
    "Glucose": 140,
    "BloodPressure": 300,
    "SkinThickness": 100,
    "Insulin": 80,
    "BMI": 25,
    "DiabetesPedigreeFunction": 0.356,
    "Age": 25
}

# send POST request
response = requests.post(API_URL, json=payload)

print ("Status Code:", response.status_code)
print("Response JSON:", response.json())