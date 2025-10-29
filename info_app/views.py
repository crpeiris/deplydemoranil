from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'info_app/welcome.html')

def calendar(request):
    return render(request, 'info_app/calendar.html')
