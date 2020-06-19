import json
import os
from dotenv import load_dotenv
from django.shortcuts import render
from .models import Details
from .ransfer import send
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


load_dotenv()


logger = logging.getLogger(__name__)
@csrf_exempt
def index(request):
    context = {}
    success, fail = [], []
    if request.method == "POST":
        
        amounts, phones, providers = [], [], []
        for key, value in request.POST.items():
            if value == [""] or value == 'Select a Provider':
                continue            
            key = key.split("_")[0]
            if key == "amount":
                amounts.append(value)
            elif key == "phone":
                phones.append(value)
            elif key == 'provider':
                providers.append(value)
            print(providers)
        logger.warning("Collecting values")
        zipped_file = list(zip(phones, providers, amounts))
        print(zipped_file)
        if zipped_file:
            for value in zipped_file:
                data = {
                    "Code": value[1].lower(),
                    "Amount": value[2],
                    "PhoneNumber": value[0],
                    "SecretKey": os.environ.get('SECRET_KEY')
                }
                logger.warning("Sending " + value[2] + " to PhoneNumber:" + value[0])
                response = send(data)
                response = response.decode("utf8")
                data = json.loads(response)
                
                if data["ResponseCode"] == "200":
                    success.append(f"Successfuly sent to {value[0]} ")
                else:
                    fail.append(f"Failed to send to {value[0]}")

            data = {
                "success": success,
                "fail":fail
            }
            return JsonResponse(data)
        else:
            fail.append("Input the right value")
            data = {
                "fail":fail
            }
            return JsonResponse(data)

    return render(request, "index.html", context)
