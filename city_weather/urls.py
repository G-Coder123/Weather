from django.urls import path
from . import views
urlpatterns = [

    path("",views.home,name="home"),
    path(r"delete/<int:pk>",views.remove,name="delete")
    #path('r',views.city_change,name="change")
]