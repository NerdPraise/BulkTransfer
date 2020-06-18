import json
from django.shortcuts import render
from .models import Details
from .ransfer import send
import logging

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    if request.method == "POST":
        amounts, phones, providers = [], [], []
        for key, value in request.POST.items():

            key = key.split("_")[0]
            if key == "amount":
                amounts.append(value)
            elif key == "phone":
                phones.append(value)
            elif key == 'provider':
                providers.append(value)
        logger.warning("Collecting values")
        zipped_file = list(zip(phones, providers, amounts))
        for value in zipped_file:
            data = {
                "Code": value[1].lower(),
                "Amount": value[2],
                "PhoneNumber": value[0],
                "SecretKey": "hfucj5jatq8h"
            }
            logger.warning("Sending " + value[2] + " to PhoneNumber:" + value[0])
            response = send(data)
            response = response.decode("utf8")
            data = json.loads(response)
                
            if data["ResponseCode"] == "200":
                context = {"success": f"Sucessfull sent to {value[0]}"}
            else:
                context = {"error": f"Error sending to {value[0]}"}

    return render(request, "index.html", context)
