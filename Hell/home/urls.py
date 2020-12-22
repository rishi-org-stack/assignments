from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns=[
    path("",views.home,name="home"),
    path("add/<str:fname>/<str:lname>/<str:email>/",views.add,name="add"),
    path("getu/<int:id>/",views.getuser,name="getu"),
    path("addfavs/<int:id>/<str:name>/",views.favs,name="favs"),
    path("dfavs/<int:id>/<str:name>",views.rmfavs,name="getfavs")

]