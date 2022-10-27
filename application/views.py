from django.shortcuts import render, redirect, reverse
from .models import Notes, Category
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddNoteForm, AddCategoryForm
from django.db.models import Q


@login_required()
def main(request):
    cards = Notes.objects.filter(user=request.user).all()
    categories = Category.objects.filter(user=request.user).all()
    context = {
        'cards': cards,
        'categories': categories
    }

    return render(request, 'cards.html', context=context)


def category_filter(request):
    cards = Notes.objects.filter(category=).all()
    context = {
        'cards': cards
    }

    return render(request, 'cards.html', context=context)

def delete_note(request, id):
    if request.POST:
        Notes.objects.filter(id=id).delete()

    return redirect('main')

def edit_note(request, id):
    if request.POST:
        Notes.objects.filter(id=id).delete()

    return redirect('main')

def search(request):
    query = request.GET.get('query')
    search_results = Notes.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'search.html', {'search_results': search_results, 'query': query})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('main'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})

@login_required()
def add_note(request):

    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id
        form = AddNoteForm(request_data, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = AddNoteForm()

    return render(request, 'note_form.html', context={'form': form})

@login_required()
def add_category(request):

    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id
        form = AddCategoryForm(request_data)

        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = AddCategoryForm()

    return render(request, 'category_form.html', context={'form': form})

