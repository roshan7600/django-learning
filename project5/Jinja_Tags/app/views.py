from django.shortcuts import render

# Create your views here.
def jinja_tags(request):
    d={'name' : 'Roshan' , 'age': 25}
    return render(request , 'jinja_tags.html' , context=d)