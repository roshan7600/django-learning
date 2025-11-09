from django.shortcuts import render
from app.models import *
# from django.db.models.functions import length
# Create your views here.

def display_tables(request):
    QLTO=Emp.objects.all()
# FILTER METHOD ARE USED TO CONDITON AND FILTER IT 
    QLTO=Emp.objects.filter(JOB='SALESMAN')

# order_by method are used in decending order
    QLTO=Emp.objects.order_by('-JOB')

# this method are used to remove this  JOB='SALESMAN' and other are showing
    QLTO=Emp.objects.exclude(JOB='SALESMAN')

    QLTO=Emp.objects.all()

    d={'QLTO':QLTO}


    return render(request,'display_tables.html' , d)


def Emp_To_Mgr(request):
    QLTO=Emp.objects.all().select_related('MGR') 

    QLTO=Emp.objects.all().select_related('MGR').filter(JOB='CLERK') 
    QLTO=Emp.objects.all().select_related('MGR').filter(MGR__JOB='CLERK') 
    

    QLTO=Emp.objects.all().select_related('DEPTNO') 
    QLTO=Emp.objects.all().select_related('DEPTNO').filter(ENAME='SMITH') 
    QLTO=Emp.objects.all().select_related('DEPTNO').filter(DEPTNO__LOC='NEW YORK')


    d={'QLTO':QLTO}
    return render(request,'display_tables.html' , d)