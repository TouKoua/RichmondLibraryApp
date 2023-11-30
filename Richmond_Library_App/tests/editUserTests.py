from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, TestUser
from Richmond_Library_App.models import User 

class EditUserTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.test_user = TestUser.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            user_type='student'
        )

    def test_edit_user(self):
        # Ensure the edit view is accessible
        response = self.client.get(reverse('edit_user', args=[self.test_user.username]))
        self.assertEqual(response.status_code, 200)

        # Edit user data
        updated_email = 'updated@example.com'
        updated_password = 'updatedpassword'
        updated_user_type = 'admin'

        response = self.client.post(
            reverse('edit_user', args=[self.test_user.username]),
            {
                '_email': updated_email,
                '_password': updated_password,
                '_user_type': updated_user_type
            }
        )

        # Check if the user is redirected to the users view after editing
        self.assertRedirects(response, reverse('users'))

        # Refresh the user from the database
        self.test_user.refresh_from_db()

        # Check if the user data is updated
        self.assertEqual(self.test_user.email, updated_email)
        self.assertEqual(self.test_user.password, updated_password)
        self.assertEqual(self.test_user.user_type, updated_user_type)