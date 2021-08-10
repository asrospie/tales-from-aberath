from django.shortcuts import render
from ..models import BlogPost

# default blog request
def blog(request):
    all_posts = BlogPost.objects.all().order_by('-pub_date')

    tags = []

    for p in all_posts:
        p_tags = p.tags['tags']
        for t in p_tags:
            if t not in tags:
                tags.append(t)

    return render(request, 'blog/pages/blog.html', { 'posts': all_posts, 'tags': tags })

def blog_post(request, permalink):
    post = BlogPost.objects.get(permalink=permalink)

    content = {
        'title': post.title,
        'pub_date': post.pub_date,
        'author': post.author,
        'content': post.content
    }

    return render(request, 'blog/pages/post.html', content) 

def blog_search(request):
    tag = request.GET['q']

    # find blog posts with search tag
    all_posts = BlogPost.objects.all().order_by('-pub_date')

    posts = []
    for p in all_posts:
        if tag in p.tags['tags']:
            posts.append(p) 

    return render(request, 'blog/pages/blog_search.html', { 'tag': tag, 'posts': posts })