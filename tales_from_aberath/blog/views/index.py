from django.shortcuts import render
from ..models import BlogPost

# Create your views here.
def index(request):
    top_five = BlogPost.objects.all().order_by('-pub_date')[:5]
    not_found = 'No posts found.'

    return render(request, 'blog/index.html', { 'posts': top_five, 'not_found': not_found })