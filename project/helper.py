__author__ = 'arashaga'
from project.models import Projects
from rfc.models import RFCDocument


def project_info_helper(request, pk):
    user = request.user
    projects = Projects.objects.all().order_by('project_name')
    selected_project = Projects.objects.filter(pk=pk)
    proj = []
    permissions = {}
    rfcs = RFCDocument.objects.filter(rfc_project_id=pk)

    for project in projects:
        if user.has_obj_perm('view', project) or user.has_obj_perm('delete', project):
            proj.append(project)

        else:
            proj.append('None')

    # print selected_project
    permissions = check_project_permissions(user, pk)
    context = {'uprojects': proj,
               'selectedProj': selected_project[0],
               'rfc_count': rfcs.count(),
               'selectedProjID': pk,
               'permissions': permissions}
    print context
    return context


def check_project_permissions(user, pk):
    selected_project = Projects.objects.get(pk=pk)
    print pk
    print selected_project
    permissions = {}
    permissions['view'] = False
    permissions['delete'] = False
    permissions['change'] = False

    if user.has_obj_perm('view', selected_project):
        permissions['view'] = True

    if user.has_obj_perm('change', selected_project):
        permissions['change'] = True

    if user.has_obj_perm('delete', selected_project):
        permissions['delete'] = True

    return permissions