# studentGradesBack/studentgradesapp/urls.py

from django.urls import path
from .views import classnames, export_csv  # Make sure this matches the view function name

urlpatterns = [
    path('classnames/', classnames, name='classnames'),
    path('export-csv/', export_csv, name='export_csv'),
]
