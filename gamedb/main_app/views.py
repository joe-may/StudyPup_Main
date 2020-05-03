from django.shortcuts import render


# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def welcome(request):
  return render(request, 'welcome.html')

def game1(request):
  return render(request, 'game1.html')

def game2(request):
  return render(request, 'game2.html')

def game3(request):
  return render(request, 'game3.html')