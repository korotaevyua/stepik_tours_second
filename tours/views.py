import random

from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render

from tours.data import departures
from tours.data import description
from tours.data import subtitle
from tours.data import title
from tours.data import tours


def main_view(request):
    random_list = list(range(1, 17, 1))
    random.shuffle(random_list)
    context = {'title': title, 'subtitle': subtitle, 'description': description}
    for i in range(1, 7, 1):
        country_name = 'country_' + str(i)
        name = 'name_' + str(i)
        number = 'n_' + str(i)
        pic = 'picture_' + str(i)
        cost = 'cost_' + str(i)
        context[country_name] = tours[random_list[i]]['country']
        context[name] = tours[random_list[i]]['title']
        context[number] = random_list[i]
        context[pic] = tours[random_list[i]]['picture']
        context[cost] = tours[random_list[i]]['price']
    return render(request, "tours/index.html", context=context)


def tour_view(request, _id):
    stars = int(tours[_id]['stars']) * '★'
    return render(request, "tours/tour.html", {'title': tours[_id]['title'], 'description': tours[_id]['description'],
                                               'departure': departures[tours[_id]['departure']],
                                               'picture': tours[_id]['picture'],
                                               'price': tours[_id]['price'], 'stars': stars,
                                               'country': tours[_id]['country'], 'nights': tours[_id]['nights']})


def departure_view(request, departure):
    context = {'departure': departures[departure]}
    prices = []
    nights = []
    needed_tours = []
    paths = []
    for tour_id, tour in tours.items():
        if tour['departure'] == departure:
            prices.append(tour['price'])
            nights.append(tour['nights'])
            needed_tours.append([tour, tour_id])
            paths.append(tour_id)
    context['min_price'] = min(prices)
    context['max_price'] = max(prices)
    context['min_nights'] = min(nights)
    context['max_nights'] = max(nights)
    context['tours'] = needed_tours
    context['paths'] = paths
    return render(request, "tours/departure.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
