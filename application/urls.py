from django.urls import path, include
from .views import main, sign_up, search, add_note, category_filter, add_category, delete_note, edit_note

urlpatterns = [
    path('', main, name='main'),
    path('add_category/', add_category, name='add_category'),
    path('add_note/', add_note, name='add_note'),
    path('delete_note/', delete_note, name='delete_note'),
    path('edit_note/', edit_note, name='edit_note'),
    path('registration/', include('django.contrib.auth.urls')),
    path('account/sign_up', sign_up, name='sign_up'),
    path('search/', search, name='search'),
    path('category_filter/', category_filter, name='category_filter'),
    ]

