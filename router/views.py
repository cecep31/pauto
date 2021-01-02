from django.shortcuts import render
from .models import Mrouter

# Create your views here.
def show(request):
    data=Mrouter.objects.all()
    context = {
        "data" : data,
    }

    return render(request,'routershow.html',context)
    pass