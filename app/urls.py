from django.urls import path, include

from app.csv_parser import import_customers
from app.views import customers_list, index_page

urlpatterns = [
    path('', index_page, name="index"),
    path('api/customers/', customers_list, name="customers"),
    path('api/import_customers/', import_customers, name="import_customers"),
]
