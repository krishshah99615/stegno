from django.urls import path
from .views import home,encode,decode
urlpatterns = [
               path('',view=home,name='home'),
               path('encode',view=encode,name='encode'),
               path('decode',view=decode,name='decode'),
]
