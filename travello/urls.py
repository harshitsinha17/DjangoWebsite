from django.urls import path
from . import views

urlpatterns = [
    path('business',views.index,name='index'),

]