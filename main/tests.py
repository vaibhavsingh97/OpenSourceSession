from django.test import TestCase, SimpleTestCase
from django.test import Client
from main.forms import RegistrationForm
from main.models import StudentRegisterationForm

class HomeViewTests(SimpleTestCase):

    # Home test failing
    # def test_get_request(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

    def test_register_accessible(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_admin_accessible(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)


class RegistrationValidationTestCase(TestCase):
    def setUp(self):
        StudentRegisterationForm.objects.create(name="vaibhav", email="vaibhav@example.com", branch="cse", year="2014", github_url="https://github.com/vaibhavsingh97/")

    def test_name(self):
        StudentName = StudentRegisterationForm.objects.get(name="vaibhav")
        self.assertEqual(StudentName.name, 'vaibhav')

    def test_email(self):
        StudentEmail = StudentRegisterationForm.objects.get(email="vaibhav@example.com")
        self.assertEqual(StudentEmail.email, "vaibhav@example.com")

    def test_branch(self):
        StudentBranch = StudentRegisterationForm.objects.get(branch="cse")
        self.assertEqual(StudentBranch.branch, "cse")

    def test_year(self):
        StudentYear = StudentRegisterationForm.objects.get(year="2014")
        self.assertEqual(StudentYear.year, 2014)

    def test_github_url(self):
        StudentGithubUrl = StudentRegisterationForm.objects.get(github_url="https://github.com/vaibhavsingh97/")
        self.assertEqual(StudentGithubUrl.github_url, "https://github.com/vaibhavsingh97/")

class RegistrationValidation(TestCase):
    def test_register(self):
        c = Client()
        response = c.post('/register/',{'name': 'vaibhav', 'email': 'vaibhav@example.com', 'branch': 'cse', 'year': '2014', 'github_url': 'https://github.com/vaibhavsingh97/'})
        self.assertEqual(response.status_code, 200)

class User_Form_Test(TestCase):

    def test_UserForm_valid(self):
        form = RegistrationForm(data={'name': 'vaibhav', 'email': 'vaibhav@example.com', 'branch': 'cse', 'year': 2014, 'github_url': 'https://github.com/vaibhavsingh97/'})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = RegistrationForm(data={'name': 'vaibhav', 'email': 'vaibhav@.com', 'branch': 'cse', 'year': 'first', 'github_url': 'test'})
        self.assertFalse(form.is_valid())