from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.testingSwager, name='testingswager'),
    path('register_compony/',views.register_compony)
]