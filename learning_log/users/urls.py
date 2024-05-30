from django.urls import path, include

app_name= 'users'

urlpatterns = [
    path('', 'django.contrib.auth.urls'),
]
