import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    return HttpResponse("hello, lion")

def hello(request, name):
    now = datetime.now(tz=None)
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_objects = re.match('[a-zA-Z]+', name)
    
    if(match_objects):
        clean_name = match_objects.group(0)
    else:
        clean_name = "Friend"
    return HttpResponse("hello, "+ clean_name +", it's " + formatted_now)