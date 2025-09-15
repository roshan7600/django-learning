from django.shortcuts import render

# Create your views here.
def ice_cream(request):
    return render(request, 'ice_cream.html')