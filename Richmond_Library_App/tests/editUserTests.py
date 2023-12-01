from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Richmond_Library_App.models import User 

class EditUserTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            user_type='student'
        )

    def test_edit_user(self):
        # Ensure the edit view is accessible
        response = self.client.get(reverse('EditUser', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)

        # Edit user data
        updated_email = 'updated@example.com'
        updated_password = 'updatedpassword'
        updated_user_type = 'admin'

        response = self.client.post(
            reverse('EditUser', args=[self.user.username]),
            {
                '_email': updated_email,
                '_password': updated_password,
                '_user_type': updated_user_type
            }
        )

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'users.html')

        # Refresh the user from the database
        self.user.refresh_from_db()

        # Check if the user data is updated
        self.assertEqual(self.user.email, updated_email)
        self.assertEqual(self.user.password, updated_password)
        self.assertEqual(self.user.user_type, updated_user_type)
