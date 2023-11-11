# studentGradesBack/studentgradesapp/urls.py

from django.urls import path
from .views import classnames  # Make sure this matches the view function name

urlpatterns = [
    path('classnames/', classnames, name='classnames'),
]
