""" Users views"""
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# exceptioons
from django.db.utils import IntegrityError
# models
from django.contrib.auth.models import User
from users.models import Profile


@login_required
def update_profile(request):
    profile = request.user.profile

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user
        })


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Passwords are not the same'})
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'User is already taken'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.last_name = request.POST['email']
        user.save()
        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')
