from django.shortcuts import render
from ..models import BlogPost

# Create your views here.
def map(request):

    return render(request, 'blog/pages/map.html')