from django.shortcuts import render

# Create your views here.
def datas(request):
    return render(request, "success.html")