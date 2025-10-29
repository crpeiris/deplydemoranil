from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'info_app/welcome.html')

def project(request):
    return render(request, 'info_app/project.html')
