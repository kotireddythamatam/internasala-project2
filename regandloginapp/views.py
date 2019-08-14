from django.shortcuts import render
from django.http import HttpResponse
from .models import Regmodel
from .forms import Regform,Login
def input(request):
    return render(request, 'input.html')
def reg(request):
    if request.method=="GET":
        a=Regform()
        return render(request, 'reg.html', {'a1':a})
    else:
        b=Regform(request.POST)
        if b.is_valid():
            b.save(commit=True)
            return HttpResponse('regestration is successfull')
        else:
            print(b.errors)
            return HttpResponse('regestration is failed')
def login(request):
    if request.method=="GET":
        c=Login()
        return render(request, 'log.html', {'c1':c})
    else:
        d=Login(request.POST)
        if d.is_valid():
            x=d.cleaned_data['user_name']
            y=d.cleaned_data['password']
            z=Regmodel.objects.filter(user_name=x, password=y)
            if z :
                return HttpResponse('login successfull')
            else:
                return HttpResponse('login failed')
