from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.views import View

from tours.data import tours
from tours.data import departures


def MainView(request):
    return render(request, "tours/index.html", {'var': tours[1]['title']})


def TourView(request, _id):
    stars=int(tours[_id]['stars'])*'★'
    return render(request, "tours/tour.html", {'title': tours[_id]['title'], 'description': tours[_id]['description'],
                                               'departure': departures[tours[_id]['departure']], 'picture': tours[_id]['picture'],
                                               'price': tours[_id]['price'], 'stars': stars,
                                               'country': tours[_id]['country'], 'nights': tours[_id]['nights']})


def DepartureView(request, departure):
    return render(request, "tours/departure.html")


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
