from django.shortcuts import render, HttpResponse

def home_main(request):
    return HttpResponse("Welcome to blog ")