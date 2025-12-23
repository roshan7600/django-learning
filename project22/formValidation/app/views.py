from django.shortcuts import render
from app.forms import StudentForm  # Import the form
from app.models import StudentForm as StudentModel  # Import the model with a different name
from django.http import HttpResponse

def student_form(request):
    ESDO = StudentForm()
    d = {'ESDO': ESDO}
    
    if request.method == 'POST':
        SDFO = StudentForm(request.POST)
        if SDFO.is_valid():
            try:
                # Use cleaned_data instead of changed_data
                Sname = SDFO.cleaned_data['Sname']
                Sage = SDFO.cleaned_data['Sage']
                Semail = SDFO.cleaned_data['Semail']
                
                # Create or get the student object using the correct model
                STO, created = StudentModel.objects.get_or_create(
                    Sname=Sname,
                    Sage=Sage,
                    Semail=Semail
                )
                
                if created:
                    return HttpResponse('New Student record is created')
                else:
                    return HttpResponse("Student record already exists")
            except Exception as e:
                return HttpResponse(f'Error: {str(e)}')
        else:
            # Return the form with errors
            d = {'ESDO': SDFO}
            return render(request, 'student_form.html', d)
            
    return render(request, 'student_form.html', d)