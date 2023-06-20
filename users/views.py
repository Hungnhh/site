from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} create sucessfully')
            return redirect('food:index')
        else:
            form = UserCreationForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')

def test(request):
    pass