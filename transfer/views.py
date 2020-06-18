from django.shortcuts import render
from .models import Details
from .ransfer import send
import logging

logger = logging.getLogger(__name__)


# Create your views here.
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
                "Code": "",
                "Amount": value[2],
                "PhoneNumber": value[0],
                "SecretKey": ""

            }
            logger.warning("Sending " + value[2] + " to PhoneNumber:" + value[0])
            send(data)

    return render(request, "index.html", context)
