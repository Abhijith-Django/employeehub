from django.urls import path
from information.views import EmployeeListView,EmployeeCreateView,EmployeeDetailView,EmployeeDeleteView

urlpatterns = [
    
    path('employees/all/',EmployeeListView.as_view(),name="employee-list"),
    path('employees/add/',EmployeeCreateView.as_view(),name="employee-create"),
    path('employees/<int:pk>/',EmployeeDetailView.as_view(),name="employee-detail"),
    path('employee/<int:pk>/remove',EmployeeDeleteView.as_view(),name="employee-delete")

]