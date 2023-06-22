from django.urls import path 

from .views import * 


urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("index/",index,name="index"),
    path("news/",news,name="news"),
    path("newsd/",newsd,name="newsd"),

    
]