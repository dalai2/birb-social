from django.http import HttpResponse

from datetime import datetime
import json


def hello_world(request):
    return HttpResponse("Hello current server time is {now}!".format(
        now=datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    ))


def sort_integers(request):

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4),
                        content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}! welcome to my app'.format(name)
    return HttpResponse(message)
