from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') # home.html not yet created in templates