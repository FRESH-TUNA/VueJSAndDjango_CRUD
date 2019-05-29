from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.middleware import csrf

from .models import *
from .forms import *

def getCsrf(request):
    return JsonResponse({'csrfToken': csrf.get_token(request)})

def readPosts(request):
    posts = list(Post.objects.values())
    return JsonResponse({'posts': posts})

def readPost(request, pk):
    post = model_to_dict(get_object_or_404(Post, pk=pk))
    return JsonResponse({'post': post})

def createPost(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        postForm = PostForm(body)
        postForm.save()
        return JsonResponse({'result': 'success'})

def updatePost(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        body = json.loads(request.body.decode('utf-8'))
        postForm = PostForm(body, instance=post)
        postForm.save()
        return JsonResponse({'result': 'success'})

def deletePost(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return JsonResponse({'result': 'success'})
