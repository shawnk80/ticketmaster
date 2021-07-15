from django.shortcuts import render, redirect, HttpResponse
from .forms import ArtistSearchForm
from .models import ArtistSearch

def home_page(request):
    if request.method == "POST":
        form = ArtistSearchForm(request.POST)
        if form.is_valid():
            print('form is valid')
            artistSearch = form.save(commit=False)
            artistSearch.save()
            return redirect('concert_app:search_results')
    else:
        form = ArtistSearchForm()
    return render(request, 'concert_app/home.html', {'form': form})

def search_results(request):
    return render(request, 'concert_app/search_results.html')
