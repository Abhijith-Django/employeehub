from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from information.models import Employee

from information.forms import EmployeeForm

class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,"employee_list.html",{"data":qs})
    
class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"employee_create.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            form_instance.cleaned_data

            return redirect("employee-list")
        
        else:

            return redirect("employee-create")
        
class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,"employee_detail.html",{"data":qs})
    
class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect("employee-list")
    
class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        

    