from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import employeemodelform
from .models import employeemodel

# Create your views here.
def index(request):
    return HttpResponse("Hello")

class employeeclass(View):
    template_name = "employee.html"

    def get(self, request, pk = None):
        form = employeemodelform()
        query = employeemodel.objects.all()
        if pk:
            employeemodel.objects.filter(pk = pk).delete()
            return redirect("employee-class")
        
        context = {"data": query, "form":form}
        return render(request=request, template_name=self.template_name , context=context)
    
    def post(self, request, pk = None):
        if pk:
            employee = employeemodel.objects.get(pk = pk)
            form = employeemodelform(request.POST, instance=employee)
        else:
            form =  employeemodelform(request.POST)
        
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect("employee-class")
        
        query = employeemodel.objects.all()
        context = {"data" : query, "form": form}
        print("form post is :")

        return render(request=request, template_name=self.template_name, context=context)