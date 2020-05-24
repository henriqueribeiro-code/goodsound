from django.shortcuts import render, redirect
from .forms import UserModelForm
# Create your views here.


def add(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect()
    else:

        form = UserModelForm()

    context = {
        'form': form
    }
    return render(request, 'users/user.html', context)

