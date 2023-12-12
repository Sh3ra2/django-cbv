from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("employee", views.employeeclass.as_view(), name="employee-class"),
    path("delete/<int:pk>/", views.employeeclass.as_view(), name="employee-delete"),
    path("update/<int:pk>/", views.employeeclass.as_view(), name="employee-update"),
]