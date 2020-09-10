from django.shortcuts import render, redirect
from .forms import TaskCreationForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/auth/login/')
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('profile')
    else:
        form = TaskCreationForm()
        tasks = Task.objects.filter(author=request.user)
        return render(request, 'accounts/profile.html', {
            'user': user,
            'form': form,
            'tasks': tasks,
        })


@login_required(login_url='/auth/login/')
def remove_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.author == request.user:
        task.delete()
        return redirect('profile')
    else:
        return redirect('profile')


@login_required(login_url='/auth/login/')
def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.author == request.user:
        task.is_completed = True
        task.save()
        return redirect('profile')
    else:
        return redirect('profile')