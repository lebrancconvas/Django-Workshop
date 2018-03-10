from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        """<h1>Hello Music</h1>
           <h2>Music BNK48 Unofficial Fansite</h2>"""
    )
