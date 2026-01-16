from django.shortcuts import render

# Create your views here.
def startHome(request):
    return render(request, 'Main/mainPage.html')