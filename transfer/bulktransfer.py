import requests


url = "https://sandbox.wallets.africa/bills/airtime/providers"

payload = {
    "Code": "",
    "Amount": "",
    "PhoneNumber":"",
    "SecretKey":""

}

headers = {
				'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
