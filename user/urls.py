from nturl2path import url2pathname
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign-up')
]
