from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound


def MainView(request):
    return render(request, "tours/index.html")


def TourView(request, id):
    return render(request, "tours/tour.html")


def DepartureView(request, departure):
    return render(request, "tours/departure.html")


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
