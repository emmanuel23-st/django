from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



from .models import House,Cars,Products



from django.shortcuts import render 
from .models import House, Cars,Products
 # Create your views here. 
def brian(request):
    home = House.objects.all() 
    height = Cars.objects.all() 
    
    context = {
        'products':Products


    }
    return render (request ,"home.html" , context)


from my_app.forms import StudentForm  
  
def index(request):  
    student = StudentForm()  
    return render(request,"my_forms.html",{'form':student})  

 
    
