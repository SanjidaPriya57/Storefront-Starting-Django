from django.urls import path
from . import views


#urlConfiguration for playground app
urlpatterns = [
    path('hello/', views.say_hello)
]