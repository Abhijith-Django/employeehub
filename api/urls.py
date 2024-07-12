from django.urls import path

from api import views

urlpatterns = [
    
    path('employees/',views.EmployeeCreateListView.as_view()),
    path('employees/<int:pk>/',views.EmployeeRetreiveUpdateDeleteView.as_view()),

]