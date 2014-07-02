from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rfc.models import RFCDocument
from project.models import Projects


def portal_create_groups():
    if (not Group.objects.filter(name='General Contractor').exists()):
        gc_users = Group(name='General Contractor')
        gc_users.save()

    if (not Group.objects.filter(name='Owner').exists()):
        owner_users = Group(name='Owner')
        owner_users.save()

    if (not Group.objects.filter(name='Architect/Engineer').exists()):
        architect_users = Group(name='Architect/Engineer')
        architect_users.save()

# def portal_create_permissions():
#
#
# rfc_perm = ContentType.objects.get_for_model(RFCDocument)
#
#     if (not Permission.objects.filter(name = 'Can Create RFC').exists()):
#         can_add_rfc = Permission.objects.create(codename='can_add_rfc',
#                                             name = 'Can Create RFC',
#                                             content_type = rfc_perm)
#
#     if (not Permission.objects.filter(name = 'Can Delete RFC').exists()):
#         can_delete_rfc = Permission.objects.create(codename='can_delete_rfc',
#                                             name = 'Can Delete RFC',
#                                             content_type = rfc_perm)
#
#
#     project_perm = ContentType.objects.get_for_model(Projects)
#
#     if (not Permission.objects.filter(name = 'Can Create Project').exists()):
#         can_add_project = Permission.objects.create(codename='can_add_project',
#                                             name = 'Can Create Project',
#                                             content_type = project_perm)
#
#     if (not Permission.objects.filter(name = 'Can Delete Project').exists()):
#         can_delete_project = Permission.objects.create(codename='can_delete_project',
#                                             name = 'Can Delete Project',
#                                             content_type = project_perm)


