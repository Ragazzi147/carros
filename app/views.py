from app.models import CustomUser
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]
        email = data["email"]

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"})

        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return JsonResponse({"success": "User registered successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": "User logged in successfully"})
        else:
            return JsonResponse({"error": "Invalid credentials"})
    else:
        return JsonResponse({"error": "Invalid request method"})


@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"success": "User logged out successfully"})
