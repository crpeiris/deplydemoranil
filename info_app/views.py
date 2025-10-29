from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'info_app/welcome.html')


def project(request):
    """Render a simple Project brief page for the course demo.

    The template contains the brief, milestones and submission guidelines.
    """
    return render(request, 'info_app/project.html')
