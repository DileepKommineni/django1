from django.conf.urls import url,include
from app import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^details/$',views.details),
]