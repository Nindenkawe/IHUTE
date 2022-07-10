from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.register, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path('get_sub_profile/<int:id>', views.get_sub_profile, name='get_sub_profile'),
]