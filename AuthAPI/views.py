from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse
import json

def signup(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if body['password1'] == body['password2']:
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            return JsonResponse({'result': 'success'})

def signin(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        user = auth.authenticate(
            request,
            username=body['username'],
            password=body['password1']
        )

        if user is not None:
            auth.login(request, user)
            return JsonResponse({'result': 'success'})
        else:
            return JsonResponse({'result': 'failed'})

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return JsonResponse({'result': 'success'})