from django.urls import path
from .views import employee_list, employee_create, employee_update, employee_delete

urlpatterns = [
    path("", employee_list, name="q9_list"),
    path("create/", employee_create, name="q9_create"),
    path("<int:pk>/edit/", employee_update, name="q9_update"),
    path("<int:pk>/delete/", employee_delete, name="q9_delete"),
]
