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
                if len(value) <= 13:
                    phones.append(value)
                else:
                    fail.append("Input correct phone number")
            elif key == 'provider':
                providers.append(value)
        logger.warning("Collecting values")
        zipped_file = list(zip(phones, providers, amounts))
        if zipped_file:
            for value in zipped_file:
                data = {
                    "Code": value[1].lower(),
                    "Amount": int(value[2]),
                    "PhoneNumber": value[0],
                    "SecretKey": os.environ.get('SECRET_KEY')
                }
                logger.warning("Sending " + value[2] + " to PhoneNumber:" + value[0])
                response = send(data)
                response = response.decode("utf8")
                data = json.loads(response)
                
                if "ResponseCode" in data.keys() and data["ResponseCode"] == "200":
                    success.append(f"Successfuly sent to {value[0]} ")
                elif "ResponseCode" in data.keys() and data["ResponseCode"] == "400":
                    fail.append(f"Not enough balance to send to {value[0]}")
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

    return render(request, "index.html")
    
    
def bulk_transfer(request):
    return render(request, "bulk.html")

@csrf_exempt
def bulk_send(request):
    success, fail = [], []
    if request.method == "POST" :
        amount = request.POST.get("amount") 
        provider = request.POST.get("provider")
        phones = request.POST.get("phone")
        phones = phones.split(",")
        for phone in phones:
            data = {
                    "Code": provider.lower(),
                    "Amount": int(amount),
                    "PhoneNumber": phone,
                    "SecretKey": os.environ.get('SECRET_KEY')
            }
            response = send(data)
            response = response.decode("utf8")
            data = json.loads(response)
                
            if "ResponseCode" in data.keys() and data["ResponseCode"] == "200":
                success.append(f"Successfuly sent to {phone} ")
            elif "ResponseCode" in data.keys() and data["ResponseCode"] == "400":
                fail.append(f"Not enough balance to send to {phone}")
            else:
                fail.append(f"Failed to send to {phone}")

        data = {
                "success": success,
                "fail":fail
            }
        return JsonResponse(data)