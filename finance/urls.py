from django.urls import path, include
from . import views
from .views import Cash, Check, CashDelete, CheckDelete

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('cash/',Cash.as_view(),name='cash'),
    path('check/',Check.as_view(),name='check'),
    path('cash/<int:pk>/delete',CashDelete.as_view(),name='cash-delete'),
    path('check/<int:pk>/delete',CheckDelete.as_view(),name='check-delete'),
    path('cash/del',views.delca,name='del-ca'),
    path('check/del',views.delch,name='del-ch'),
]
