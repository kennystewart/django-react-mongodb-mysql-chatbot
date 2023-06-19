from django.urls import path
from hello import views
urlpatterns = [
    path('', views.home, name='home'),
    path('hello/<name>', views.hello, name="hello")
]