from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForm, ProfileForm

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

def members(request):

    return render_to_response("members/index.html", locals(), context_instance = RequestContext(request))