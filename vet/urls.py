from django.urls import path
from . import views


urlpatterns = [
        path(r'', views.index,name="index"),
        path(r'signup', views.signup,name="signup"),
]
