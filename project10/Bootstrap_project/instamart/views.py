from django.shortcuts import render

# Create your views here.
def vegetables(request):
    return render(request , 'vegetables.html')