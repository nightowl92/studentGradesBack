from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import csv


def classnames(request):
    classes = [f'class{i}' for i in range(1, 11)]
    return JsonResponse({'classes': classes})

def export_csv(request):
    # Replace this with your database query
    mock_data = [['Column1', 'Column2'], ['Data1', 'Data2'], ['Data3', 'Data4']]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    for row in mock_data:
        writer.writerow(row)

    return response