__author__ = 'arashaga'
from project.models import Projects
from rfc.models import RFCDocument


def project_info_helper(request, pk):
    projects = Projects.objects.all().order_by('project_name')
    selected_project = Projects.objects.filter(pk=pk)
    proj = []
    rfcs = RFCDocument.objects.filter(rfc_project_id=pk)

    for project in projects:
        if request.user.has_obj_perm('view', project) or request.user.has_obj_perm('delete', project):

            proj.append(project)

        else:
            proj.append('None')
    print pk
    print proj
    # print selected_project
    context = {'uprojects': proj,
               'selectedProj': selected_project[0],
               'rfc_count': rfcs.count(),
               'selectedProjID': pk}
    print context
    return context