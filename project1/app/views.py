from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse('Go to the home page')
    
    return render(request, 'index.html')



# def about(request):
#     return HttpResponse('This is the about page')

# def contact(request):
#     return HttpResponse('This is about contact')
    
    
