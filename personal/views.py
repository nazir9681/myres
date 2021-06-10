from django.shortcuts import render, HttpResponse

# Create your views here.

def homeView(request):
    context = { }
    return render(request,'personal/home.html',context)

