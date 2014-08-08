from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext
from rest_framework.decorators import api_view
from .models import Projects
from .helper import *

# Create your views here.TODO get rid of this later
from rfc.models import RFCDocument


def home(request):
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/')
@api_view(['POST', 'GET'])
def project_info(request, pk):
    if request.method == 'GET':
        # projects = Projects.objects.all().order_by('project_name')
        # selected_project = Projects.objects.filter(pk=pk)
        # proj = []
        # rfcs = RFCDocument.objects.filter(rfc_project_id = pk)
        #
        # for project in projects:
        # if request.user.has_obj_perm('view', project) or request.user.has_obj_perm('delete', project):
        #
        #         proj.append(project)
        #
        #     else:
        #         proj.append('None')
        #
        # print proj
        # #print selected_project
        # context = {'uprojects': proj,
        #            'selectedProj': selected_project[0],
        #            'rfc_count':rfcs.count(),}
        context = project_info_helper(request, pk)
        return render(request, 'members/projects/index.html', context)
    if request.method == 'POST':
        pass


