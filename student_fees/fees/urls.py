from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('update_fees/<int:student_id>/', views.update_fees, name='update_fees'),
]
