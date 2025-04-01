from decimal import Decimal
from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'fees/student_list.html', {'students': students})

def update_fees(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        amount = float(request.POST['amount'])
        # student.fees_paid += amount
        student.fees_paid += Decimal(amount)
        student.save()
        return redirect('student_list')
    return render(request, 'fees/update_fees.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        total_fees = int(request.POST.get('total_fees'))
        fees_paid = int(request.POST.get('fees_paid'))
        # fees_due = request.POST.get('fees_due')
        
        # Create a new student and save it to the database
        Student.objects.create(
            name=name,
            email=email,
            course=course,
            total_fees=total_fees,
            fees_paid=fees_paid,
            fees_due=fees_due
        )
        
        # Redirect to the student list page after adding the student
        return redirect('student_list')
    
    return render(request, 'fees/add_student.html')
