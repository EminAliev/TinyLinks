from django.urls import path

from . import views

app_name = 'links'
urlpatterns = [
    path('', views.LinkListView.as_view(), name='index'),
    path('create/', views.CreateLinkView.as_view(), name='create_view'),
    path('<int:link_id>/', views.DetailLinkView.as_view(), name='detail'),
    path('create-link/', views.create_short_link, name='create'),
    path('links/<str:short_link>/', views.short_link_view, name='view'),
    path('delete/<int:link_id>/', views.delete_link, name='delete'),
]
