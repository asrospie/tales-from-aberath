from django.shortcuts import render

def about(request):
    return render(request, 'blog/pages/about.html')