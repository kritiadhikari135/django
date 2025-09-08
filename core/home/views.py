from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    people = [
        { 'name': 'ram', 'age': 26},
        {'name': 'shyam', 'age': 17},
        {'name': 'z', 'age': 64},
        {'name': 'sandeep', 'age': 18},
    ]
    

    return render(request , "home/index.html", context = {'peoples': people});
