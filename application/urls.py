from django.urls import path
from .views import main, sign_up, about

urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    # path('create_note/', create_note, name='create_note'),
    # path('create_category/', create_category, name='create_category'),
    path('registration/sign_up', sign_up, name='sign_up'),
    ]

