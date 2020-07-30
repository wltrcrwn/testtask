from django.urls import path, include

from app.csv_parser import import_customers
from app.views import customers_list

urlpatterns = [
    path('customers/', customers_list, name="customers"),
    path('import_customers/', import_customers, name="import_customers"),
]
