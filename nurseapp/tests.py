from django.test import TestCase
from nurseapp.forms import *


# Create your tests here.
class Login(TestCase):
    def test_get(self):
        """Login URL test"""
        # Run.
        response = self.client.get('/login/')
        # Check.
        self.assertEqual(response.status_code, 200, msg='Login URL failed!')


class AddPatient(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'test',
            'email': 'test',
            'password': 'test',
        }
        User.objects.create_superuser(**self.credentials)
        self.client.post('/login/', self.credentials, follow=True)

    def test(self):
        data = {
            'nurse_id': 1,
            'name': 'test',
            'lastname': 'test',
            'cid': 1,
            'gender': 'm',
            'birth': '2000-06-01',
            'save': '1'
        }
        self.client.post('/patients/add/?', data, follow=True)
        # test si se creo
        self.assertTrue(Patient.objects.filter(name='test').exists(),
                        msg='Patient \'test\' was not created')
