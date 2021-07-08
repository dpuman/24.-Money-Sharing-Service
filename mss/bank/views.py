from django.http.response import HttpResponse
from django.shortcuts import render
from . forms import SignUpForm
from . models import Customer, Account, Transection
# Create your views here.


def signup(request):
    form = SignUpForm

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'bank/register.html', context)
