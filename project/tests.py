from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

# Create your tests here.
from project.models import Projects
from signup.models import SignUp, ObjectPermission
# from myobjperm.models import ObjectPermission



class ProjectTestCase(TestCase):
    def setUp(self):
        super(ProjectTestCase, self).setUp()
        self.john = SignUp.objects.create(email='john@john.com')
        self.project = Projects.objects.create(project_name='la salle', project_state_id=1, project_start='2013-10-07',
                                               project_finish='2013-10-07',
                                               project_owner_id=1, project_active=1)
        ct = ContentType.objects.get_for_model(self.project)
        print ct
        ObjectPermission.objects.create(user=self.john, can_view=True,
                                        can_change=True, can_delete=False,
                                        content_type=ct, object_id=self.project.id)


    def test_project_permission(self):
        print self.project, self.john
        self.assertFalse(self.john.has_obj_perm('delete', self.project))
        self.assertTrue(self.john.has_obj_perm('view', self.project))
        self.assertTrue(self.john.has_obj_perm('change', self.project))
