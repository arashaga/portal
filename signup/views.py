from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("index.html", locals(), context_instance = RequestContext(request))


def profile(request):

    form = ProfileForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("address.html", locals(), context_instance = RequestContext(request))


@login_required(login_url='/')
def members(request):
    return render_to_response("/members/index.html", locals(), context_instance=RequestContext(request))


def user_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # home(request)
            return HttpResponseRedirect('/')

    return render_to_response("/", locals(), context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')