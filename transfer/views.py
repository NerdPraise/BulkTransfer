from django.shortcuts import render
import bulktransfer


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        for key, value in request.POST.items():
            print(key, value)
            
    return render(request, "index.html", context)