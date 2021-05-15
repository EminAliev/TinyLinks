from django.urls import path

from . import views

app_name = 'links'
urlpatterns = [
    path('', views.LinkListView.as_view(), name='index')
]
