import requests

def send(payload):
    url = "https://api.wallets.africa/bills/airtime/purchase"

    headers = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer knqeabg6upuv"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text.encode('utf8')

