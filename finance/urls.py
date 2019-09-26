from django.urls import path, include
from . import views
from .views import Cash, Check

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('cash/',Cash.as_view(),name='cash'),
    path('check/',Check.as_view(),name='check'),
]
