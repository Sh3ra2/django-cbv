from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("employee", views.employeeclass.as_view(), name="employee-class"),
    path("delete/<int:pk>/<str:name>/", views.employeeclass.as_view(), name="employee-delete"),
    path("update/<int:pk>/<str:address>/", views.employeeclass.as_view(), name="employee-update"),
    path("filter/<str:tsearch>/", views.employeeclass.as_view(), name="employee-filter"),
    path("projects", views.projectclass.as_view(), name="project-class"),
    path("pfilter/<str:tsearch>/<str:type>/", views.projectclass.as_view(), name="project-filter"),
    path("pfilterdate/<slug:s_date>/", views.projectclass.as_view(), name="project-filter"),
]