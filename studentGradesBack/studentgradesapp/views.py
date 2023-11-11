from django.shortcuts import render
from django.http import JsonResponse

def classnames(request):
    classes = [f'class{i}' for i in range(1, 11)]
    return JsonResponse({'classes': classes})
