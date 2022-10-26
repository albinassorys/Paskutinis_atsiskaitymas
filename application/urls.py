from django.urls import path
from .views import main

    # , create_note, create_category, sign_up

urlpatterns = [
    path('', main, name='main'),
    # path('create_note/', create_note, name='create_note'),
    # path('create_category/', create_note, name='create_note'),
    # path('registration/sign_up', sign_up, name='sign_up'),
    ]

