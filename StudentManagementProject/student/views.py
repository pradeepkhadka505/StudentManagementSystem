from django.shortcuts import render, redirect
from .models import Student 

# Create your views here.
#let's create new model views
def student(request):
    std = Student.objects.all()
    return render(request, "student/index.html", {'std' : std})

def student_create(request):
    if request.method == 'POST':
        print("Added")

            #retrive all user inputs
        stds_roll = request.POST.get('std_roll')
        stds_name = request.POST.get('std_name')
        stds_address= request.POST.get('std_address')
        stds_phone = request.POST.get('std_phone')
        stds_email = request.POST.get('std_email')

        #create and object for models class

        s = Student()  #objects for models 
        s.roll = stds_roll 
        s.name = stds_name 
        s.address = stds_address
        s.phone = stds_phone
        s.email = stds_email
        s.save()
        return redirect('/student/')
    return render(request, "student/create.html")

def delete_student(request, roll):
    s = Student.objects.get(pk = roll )
    s.delete()
    return redirect('/student/')

def update_student(request, roll):
    std = Student.objects.get(pk = roll )
    return render(request, "student/update.html", {'std': std})

def do_update_student(request, roll):
            #retrive all user inputs
    stds_roll = request.POST.get('std_roll')
    stds_name = request.POST.get('std_name')
    stds_address= request.POST.get('std_address')
    stds_phone = request.POST.get('std_phone')
    stds_email = request.POST.get('std_email')

    std = Student.objects.get(pk = roll )
    std.roll = stds_roll
    std.name = stds_name
    std.address = stds_address
    std.phone = stds_phone
    std.email = stds_email

    std.save()
    return redirect('/student/')

    # return render(request, "student/update.html", {'std': std})