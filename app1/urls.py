from django.urls import path
from app1 import views
urlpatterns=[
    path('register/',views.registerview,name='register'),
    path('details/',views.details,name='details'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
]