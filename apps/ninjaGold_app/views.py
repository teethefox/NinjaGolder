from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    return render(request,'index.html')
def process(request):
    try:
        request.session['gold']=0
        request.session['ninja']
        
    except KeyError:
        request.session['gold'] = 0
        request.session['ninja']=0

        
            # request.session['farm']=request.POST['farm']
            # request.session['cave']=request.POST['cave']
            # request.session['house']=request.POST['house']
            # request.session['casino']=request.POST['casino']
    if request.POST.get("farm"):
        request.session['gold'] = request.session['gold'] + random.randint(10,20)
        action= "earned"
        building= "Farm"
        
    elif request.POST.get('cave'):
        request.session['gold'] = request.session['gold'] + random.randint(5,10)
        action="earned"
        building="Cave"
    elif request.POST.get("house"):
        request.session['gold'] = request.session['gold'] + random.randint(2,5)
        action ="earned"
        building="House"
    elif request.POST.get('casino'):
        request.session['random'] = random.randint(0,50) 
        action="lost"
        building="Casino"
        if request.session['random'] < 25:
            request.session['gold'] = request.session['gold'] + request.session['random']
        else:
            request.session['gold'] = request.session['gold'] - request.session['random']
    request.session['ninja'] += request.session['gold']
    timestamp = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    log = {
        'class': action,
        'message': "You {} {} gold from the {} {} ".format(action, request.session['gold'], building, timestamp)
    }
    try:
        activity_log = request.session['logs']
    except KeyError:
        activity_log = []

    request.session['total'] += request.session['gold']
    
    activity_log.append(log)
    request.session['logs'] = activity_log
            
    return redirect('/')

# Create your views here.
