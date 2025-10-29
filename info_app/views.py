from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'info_app/welcome.html')
def lab_sessions(request):
    return render(request, 'info_app/lab_sessions.html')
