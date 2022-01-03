from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cal(request):
    return render(request, 'addition.html', {'name': 'ram'})

def add(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])

    result = num1+num2

    return render(request, "result.html", {'addd': result})