

from django.urls import path 
from . import views

urlpatterns = [
    # path('', views.employee, name='index')
    path('student/', views.student, name='student'),
    path('student/create', views.student_create, name='create')
]
