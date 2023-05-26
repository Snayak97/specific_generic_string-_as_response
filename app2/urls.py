from django.urls import path
from app2.views import *

app2_name='something'
urlpatterns=[
    path('sky/',sky,name='sky'),
]