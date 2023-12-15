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

    def get(self, request, pk = None, name = None, address = None, tsearch = None):
        print("data got: PK is ", pk,"name is ", name,"address is ", address, "search: ", tsearch)
        print("Data was sent for pk", pk)
        form = employeemodelform()
        query = employeemodel.objects.all()
        empros = projectmodel.objects.all()
        zipped = [{"emp": emp, "pro": pro} for emp, pro in zip(query, empros)]
        if tsearch:
            query = employeemodel.objects.filter(name__icontains = tsearch)
        

        if pk and name:
            employeemodel.objects.filter(pk = pk).delete()
            return redirect("employee-class")

        if pk and address:
            
            employee = employeemodel.objects.get(pk = pk)
            
            form = employeemodelform( instance=employee)
            print("Employee is ", pk,employee.name, employee.address, employee.occupation)
        
        context = {"form":form, "zipped":zipped, "query": query, "empros": empros}
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

    def get(self, request, tsearch = None, type =  None, s_date = None):
        if tsearch and type == "icontains":
            print("For icontains match")
            query = projectmodel.objects.filter(dev__name__icontains = tsearch)
        elif tsearch and type == "exact":
            print("For exact match")
            query = projectmodel.objects.filter(dev__name__exact = tsearch)
        elif tsearch and type == "iexact":
            print("For iexact match")
            query = projectmodel.objects.filter(dev__name__iexact = tsearch)
        elif tsearch and type == "startswith":
            print("For startswith match")
            query = projectmodel.objects.filter(dev__name__startswith = tsearch)
        elif tsearch and type == "isstartswith":
            print("For isstartswith match")
            query = projectmodel.objects.filter(dev__name__isstartswith = tsearch)
        elif tsearch and type == "endswith":
            print("For endswith match")
            query = projectmodel.objects.filter(dev__name__endswith = tsearch)
        elif tsearch and type == "iendswith":
            print("For isendswith match")
            query = projectmodel.objects.filter(dev__name__iendswith = tsearch)
        elif tsearch and type == "isnull":
            print("For isnull match")
            query = projectmodel.objects.filter(dev__name__isnull = tsearch)
        elif s_date:
            print("For date match")
            query = projectmodel.objects.filter(start_date__date = s_date)
        else:
            query = projectmodel.objects.all()
        form = projectmodelform(request.POST)
        context = {"data": query, "form": form}
        return render(request=request, template_name=self.template_name, context= context)
    

    def post(self, request):
        
        query = projectmodel.objects.all()
        form =  projectmodelform(request.POST)

        if form.is_valid:
            form.save()
        context = {"data": query , "form": form}
        return render(request=request, template_name=self.template_name, context= context)
    
