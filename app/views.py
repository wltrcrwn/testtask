from django.http import JsonResponse
from rest_framework import generics, filters
from app.models import Customer
from app.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime as DT


@api_view(['GET'])
def customers_list(request):
    date = request.GET.get('date',None)
    if date:
        cs = Customer.objects.filter(register_date=DT.datetime.strptime(date, '%Y-%m-%d'))
    else:
        cs = Customer.objects.all()
    serializer = CustomerSerializer(cs, many=True)
    return Response(serializer.data)

