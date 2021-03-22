from django.urls import path
from . import views

app_name='vet'

urlpatterns = [
        path(r'', views.index,name="index"),
        path(r'signup', views.signup,name="signup"),
        path(r'profile/', views.create_user,name="crear_usuario"),
        path(r'profile/see', views.SingleUsuario,name="profile"),
        path(r'profile/(?P<pk>\d+)', views.SingleUsuario),
]
