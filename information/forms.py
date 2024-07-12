from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField(max_length=200)

    department=forms.CharField(max_length=200)

    email=forms.EmailField()

    phone_num=forms.IntegerField()