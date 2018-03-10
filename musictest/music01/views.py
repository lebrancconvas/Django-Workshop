from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        """
        <h1>Music BNK48</h1>
        <h2>The Meme Master</h2>
        <a href="#"><button>กลับบ้าน</button></a>

        """
    )
