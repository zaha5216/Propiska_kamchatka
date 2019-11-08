from django.urls import path
from .views import index
from .views import other_page
from .views import gost_page

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other'),
    path('<str:page>/', gost_page, name='gost'),

]
