from django.shortcuts import render
# 

# Create your views here.

#let's create new model views
def student(request):
    return render(request, "student/index.html")