# Create your views here.
from myapp.models import Myapp
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

from form import SumbitForm 


def index(request):
    all_list = Myapp.objects.all()
    output = ','.join([p.text for p in all_list])
    return HttpResponse(output)

#def text_form(request):
#    return render_to_response('text_form.html')


# def tweets(request):
def textform(request):
    tweets = Myapp.objects.all()
    if request.method == 'POST':
    	form = SumbitForm(request.POST)
	if form.is_valid():
           message = form.cleaned_data['text'] 
	   Myapp(text=message).save()

    else:
	form = SumbitForm()

    return render(request, 'text_form.html', {
        'form': form,
	'tweets': tweets,
    })
