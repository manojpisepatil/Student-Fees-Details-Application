from django.urls import path
from . import views
from .views import student_list
from .views import add_student

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('update_fees/<int:student_id>/', views.update_fees, name='update_fees'),
    path('add/', add_student, name='add_student'),
]
