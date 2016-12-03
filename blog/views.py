from django.shortcuts import render
from django.utils import timezone
from blog import models

def post_list(request):
	posts = models.Post.objects.all() 
	d = {"posts": posts}
	return render(request, 'blog/post_list.html',d) 
	


# Create your views here.
