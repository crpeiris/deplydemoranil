from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'info_app/welcome.html')


def resources(request):
    return render(request, 'info_app/resources.html')

def support(request):
    return render(request, 'info_app/support.html')
