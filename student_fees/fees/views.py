from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'fees/student_list.html', {'students': students})

def update_fees(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        amount = float(request.POST['amount'])
        student.fees_paid += amount
        student.save()
        return redirect('student_list')
    return render(request, 'fees/update_fees.html', {'student': student})


# from django.shortcuts import render
# from .models import Student  # Assuming you have a Student model

# def student_list(request):
#     students = Student.objects.all()  # Fetch all students from the database
#     return render(request, 'student_list.html', {'students': students})
