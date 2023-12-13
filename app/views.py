from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import employeemodelform, projectmodelform
from .models import employeemodel, projectmodel

# Create your views here.
def index(request):
    return HttpResponse("Hello")

class employeeclass(View):
    template_name = "employee.html"

    def get(self, request, pk = None, name = None, address = None):
        print("data got: PK is ", pk,"name is ", name,"address is ", address)
        print("Data was sent for pk", pk)
        form = employeemodelform()
        query = employeemodel.objects.all()

        if pk and name:
            employeemodel.objects.filter(pk = pk).delete()
            return redirect("employee-class")

        if pk and address:
            
            employee = employeemodel.objects.get(pk = pk)
            
            form = employeemodelform( instance=employee)
            print("Employee is ", pk,employee.name, employee.address, employee.occupation)
        
        context = {"data": query, "form":form}
        return render(request=request, template_name=self.template_name , context=context)
    
    def post(self, request, pk = None,address = None):

        print("Present in post, pk: ", pk, "address: ", address)
        if pk:
            employee = employeemodel.objects.get(pk = pk)
            
            form = employeemodelform(request.POST, instance=employee)
            print("Employee is ", pk,employee.name, employee.address, employee.occupation)

        else:
            form =  employeemodelform(request.POST)
            print("new form created")
        
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect("employee-class")
        
        query = employeemodel.objects.all()
        context = {"data" : query, "form": form}
        print("Post queries performed")

        return render(request=request, template_name=self.template_name, context=context)
    


class projectclass(View):
    template_name =  "project.html"

    def get(self, request):
        query = projectmodel.objects.all()
        form = projectmodelform(request.POST)
        context = {"data": query, "form": form}
        return render(request=request, template_name=self.template_name, context= context)