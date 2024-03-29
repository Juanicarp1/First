from django.shortcuts import render

# Create your views here.
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Gorda!")


def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Gorda"

    content = "Hello Gorda, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)