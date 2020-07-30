from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from app.models import Customer
import datetime as DT
from django.http import HttpResponseRedirect


@csrf_exempt
def import_customers(request):
    try:
        file = request.POST.get('file', None)
        with open(file) as f:
            l = f.readlines()
            for q in l[1:]:
                q = q.replace('\n', '').split(',')
                d1 = DT.datetime.strptime(q[2], '%Y/%m/%d').date()
                d2 = DT.datetime.strptime(q[3], '%Y/%m/%d').date()
                Customer.objects.create(first_name=q[0],
                                        last_name=q[1],
                                        date_of_birth=d1,
                                        register_date=d2
                                        )
    finally:
        return redirect(reverse('admin:%s_%s_%s' % ('app', 'customer', 'changelist')))
