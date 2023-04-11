

from django.urls import path 
from . import views

urlpatterns = [
    # path('', views.employee, name='index')
    path('student/', views.student, name='student'),
    path('student/create/', views.student_create, name='create'),
    path('student/update-student/<int:roll>', views.update_student, name='update_student'),
     path('student/do-update-student/<int:roll>', views.do_update_student, name='do_update_student'),
    path('student/delete-student/<int:roll>', views.delete_student, name='delete_student'),
]
