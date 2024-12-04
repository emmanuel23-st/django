from django import forms  
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="First name",max_length=50)  
    lastname  = forms.CharField(label="Last name", max_length = 100)