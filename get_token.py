import requests

apikey = "DUmrdgim1LtffxQS89Pzk4Q8FF02MKixH4qJ18Mcr629"
url = "https://iam.cloud.ibm.com/identity/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
    "apikey": apikey
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("✅ Access Token:\n", response.json()["access_token"])
else:
    print("❌ Error:", response.status_code, response.text)
