from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Htmlforms(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']

        return HttpResponse(f'Username is {un} and Password is {pw}')
    return render(request,'Htmlforms.html')
