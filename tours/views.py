from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound

from tours.data import title
from tours.data import subtitle
from tours.data import description
from tours.data import tours
from tours.data import departures

import random


def MainView(request):
    random_list = list(range(1, 17, 1))
    random.shuffle(random_list)
    context = {'title': title, 'subtitle': subtitle, 'description': description}
    for i in range(1, 7, 1):
        country_name = 'country_' + str(i)
        name = 'name_' + str(i)
        number = 'n_' + str(i)
        pic = 'picture_' + str(i)
        context[country_name] = tours[random_list[i]]['country']
        context[name] = tours[random_list[i]]['title']
        context[number] = random_list[i]
        context[pic] = tours[random_list[i]]['picture']
    return render(request, "tours/index.html", context=context)


def TourView(request, _id):
    stars = int(tours[_id]['stars']) * '★'
    return render(request, "tours/tour.html", {'title': tours[_id]['title'], 'description': tours[_id]['description'],
                                               'departure': departures[tours[_id]['departure']],
                                               'picture': tours[_id]['picture'],
                                               'price': tours[_id]['price'], 'stars': stars,
                                               'country': tours[_id]['country'], 'nights': tours[_id]['nights']})


def DepartureView(request, departure):
    context = {'departure': departures[departure]}
    counter = 0
    prices = []
    nights = []
    for tour in tours.keys():
        if tours[tour]['departure'] == departure:
            counter = counter + 1
            prices.append(tours[tour]['price'])
            nights.append(tours[tour]['nights'])
    context['counter'] = counter
    context['min_price'] = min(prices)
    context['max_price'] = max(prices)
    context['min_nights'] = min(nights)
    context['max_nights'] = max(nights)
    return render(request, "tours/departure.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
