from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'post':posts})
>>>>>>> 13cf9dfe51ae403ce3933770d0dfaa02f3e02c9c
