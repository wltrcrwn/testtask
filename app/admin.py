from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User

from app.models import Customer, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    change_list_template = 'admin/customers/change_list.html'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

admin.site.unregister(User)
admin.site.unregister(Group)