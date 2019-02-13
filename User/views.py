from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


# def Home(request):
#     return render(request, 'User/Login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'User/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        # pass_form = PasswordChangeCustomForm(request.user, request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # user = pass_form.save()
            # update_session_auth_hash(request, user)  # Important!
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # pass_form = PasswordChangeCustomForm(request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        # 'pass_form': pass_form
    }
    return render(request, 'User/profile.html', context)
