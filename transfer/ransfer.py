import requests


def send(payload):
    url = "https://sandbox.wallets.africa/bills/airtime/providers"

    headers = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer uvjqzm5xl6bw"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text.encode('utf8')
