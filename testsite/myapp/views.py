# Create your views here.
from myapp.models import Myapp
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    all_list = Myapp.objects.all()
    output = ','.join([p.text for p in all_list])
    return HttpResponse(output)

def text_form(request):
    return render_to_response('text_form.html')


def form(request):
    if 'q' in request.GET:
        message = request.GET['q']
	Myapp(text=message).save()
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
