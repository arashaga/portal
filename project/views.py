from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext
from rest_framework.decorators import api_view
from .models import Projects

# Create your views here.TODO get rid of this later
def home(request):
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/')
@api_view(['POST', 'GET'])
def project_list(request):
    if request.method == 'GET':
        projects = Projects.objects.all().order_by('project_name')
        context = {'projects': projects}
        return render(request, 'members/projects/index.html', {'projects': projects})
    if request.method == 'POST':
        pass


@login_required(login_url='/')
@api_view(['POST', 'GET'])
def project_list_sidebar(request):
    projects = Projects.objects.all().order_by('project_name')
    # context = {'projects': projects}
    for project in projects:
        if request.user.has_perms('view', project):
            return render(request, 'members/index.html', {'mproject': project})
        elif request.user.has_perms('delete', project):
            return render(request, 'members/index.html', {'mproject': project})
        else:
            return render(request, 'members/index.html', {'mproject': project})