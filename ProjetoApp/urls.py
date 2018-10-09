from django.urls import path
from .views import persons_list, persons_new, persons_update, persons_delete, ola, logoff, home


urlpatterns = [
    path('home/', ola, name='ola'),
    path('list', persons_list, name='persons_list'),
    path('new/', persons_new, name='persons_new'),
    path('update/<int:id>/', persons_update, name='persons_update'),
    path('delete/<int:id>/', persons_delete, name='persons_delete'),
    path('logout/', logoff, name='looff'),
    path('', home, name='home'),
]