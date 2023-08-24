from . import views
from django.urls import path

urlpatterns = [

    path('',views.sample,name='sample'),
    #path('about/',views.new,name='new')
]