import textwrap
import urls

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HomePageView(View):
    def __init__(self):
        return None
    
    linklist = urlpatterns;
    def createlinklist(_linklist):
        linkstring = ""
        for link in linklist:
            linklist += "<a href='./" + str(link) + "'>" + str(link) + "</a>"

    def dispatch(self, *args, **kwargs):
        data = '''
        <HTML>
        <head>
            <Title> Python Site Working </Title>
        </head>
        <body>
            <h1> This is the working section </h1>
        </body>
        </html>
        '''
        return HttpResponse(data)
