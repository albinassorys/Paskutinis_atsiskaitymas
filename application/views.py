from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Notes, Category
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages


@login_required()
def main(request):

    cards = Notes.objects.filter(user=request.user).all()
    categories = Category.objects.filter(user=request.user).all()
    context = {
        'cards': cards,
        'categories': categories
    }

    return render(request, 'cards.html', context=context)


def about(request):

    return render(request, 'about.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ('Registration successful'))
            return redirect(reverse('main'))
        else:
            messages.warning(request, ('Behave!'))
    else:
        form = SignUpForm()
    messages.info(request, ('Enter required information'))
    return render(request, 'registration/sign_up.html', context={'form': form})


