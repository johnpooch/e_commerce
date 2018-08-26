from django.test import TestCase
from.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User

# Create your tests here.

# Login Form =====================================================================================

class TestLoginForm(TestCase):
    
    # Valid Log In --------------------------------------------------------------------------------
    
    def test_login_form(self):
        form=UserLoginForm({
            'username': 'superuser',
            'password': 'Pa55w0rd1'
        })
        self.assertTrue(form.is_valid())
    
    def test_cannot_log_in_with_just_username(self):
        form = UserLoginForm({ "username": "username" })
        self.assertFalse(form.is_valid())
        
    def test_cannot_log_in_with_just_password(self):
        form = UserLoginForm({ "password": "password" })
        self.assertFalse(form.is_valid())

    # Missing Values ------------------------------------------------------------------------------

    def test_correct_message_for_missing_username(self):
        form = UserLoginForm({ "username": '' })
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_correct_message_for_missing_password(self):
        form = UserLoginForm({ "password": '' })
        self.assertEqual(form.errors['password'], [u'This field is required.'])
        
# Registration Form ===============================================================================

class TestRegistrationForm(TestCase):
    
    # Valid Registration --------------------------------------------------------------------------
    
    def test_registration_form(self):
        form=UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertTrue(form.is_valid())
        
    # Invalid Registration ------------------------------------------------------------------------
        
    def test_registration_passwords_must_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word2'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords do not match'])
        
    def test_registration_email_must_be_unique(self):
        
        User.objects.create_user(
            username='testuser',
            email='admin@example.com')
        
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email addresses must be unique.'])
    
    def test_cannot_register_with_just_username(self):
        form = UserRegistrationForm({ "username": "username" })
        self.assertFalse(form.is_valid())
        
    def test_cannot_register_with_just_password1(self):
        form = UserRegistrationForm({ "password1": "password" })
        self.assertFalse(form.is_valid())
        
    def test_cannot_use_invalid_email(self):
        form = UserRegistrationForm({ "email": "johnsemail" })
        self.assertFalse(form.is_valid())
        

    # Missing Values ------------------------------------------------------------------------------

    def test_correct_message_for_missing_username(self):
        form = UserRegistrationForm({ "username": '' })
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_correct_message_for_missing_password1(self):
        form = UserRegistrationForm({ "password1": '' })
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
        
    def test_correct_message_for_missing_password2(self):
        form = UserRegistrationForm({ "password2": '' })
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
