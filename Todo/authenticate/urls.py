from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('todo/',views.todo, name='todo'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.signin, name='login'),
]
