from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse_lazy, reverse

from .forms import AchingForm
from .models import Verse

import random


def aching(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AchingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            verse=random.choice(Verse.objects.all())
            context = {'verse': verse.verse_text,
                       'question': form.cleaned_data['question'],
                       }
            return render(request, 'answer.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AchingForm()

    return render(request, 'aching.html', {'form': form})

def verse_view(request, verse_id=None):
    if verse_id:
        verse = get_object_or_404(Verse, pk=verse_id)
    return render(request, 'verse_view.html', {'verse': verse.verse_text})

