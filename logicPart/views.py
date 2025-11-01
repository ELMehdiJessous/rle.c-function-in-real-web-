from django.shortcuts import render
from django.http import HttpResponse
from .utils import rle_encode

# Create your views here.


def home(request):
    result = ""
    if request.method == 'POST':
        input_txt = request.POST.get("input_usertxt","")
        result = rle_encode(input_txt)
    return render(request,"home.html",{"res": result})
