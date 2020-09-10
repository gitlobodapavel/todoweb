from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form['username'].value(),
                form['email'].value(),
                form['password'].value()
            )
            user.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {
            'form': form,
        })
