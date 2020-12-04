from django.shortcuts import render

# Create your views ere.
def home(request):
    return render(request, 'pages/home.html')