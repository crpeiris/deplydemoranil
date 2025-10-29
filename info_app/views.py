from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'info_app/welcome.html')


def projects(request):
    """Render the projects page."""
    return render(request, 'info_app/projects.html')
