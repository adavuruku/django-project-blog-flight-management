from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World')

def say_hello_html(request):
    x = 1
    y = 8
    return render (request, 'hello.html', {'name':'Abdulraheem Sherif A'})