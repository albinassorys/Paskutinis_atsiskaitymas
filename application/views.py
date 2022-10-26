from django.shortcuts import render
from .models import Notes, Category
from django.contrib.auth.models import User


def main(request):

    cards = Notes.objects.filter(user=request.user).first()
    categories = Category.objects.filter(user=request.user).first()
    context = {
        'cards': cards,
        'categories': categories
    }

    return render(request, 'cards.html', context=context)
