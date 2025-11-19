from django.urls import path
from authentication.views import login, register, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),  # Add this
    path('proxy-image/', proxy_image, name='proxy_image'),
]