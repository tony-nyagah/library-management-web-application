from accounts.models import CustomUser
from django.test import TestCase


class TestCustomUser(TestCase):
    # Test that a user can be created with all the required fields
    def test_create_user_with_required_fields(self):
        email = "test@example.com"
        password = "password123"
        first_name = "John"
        last_name = "Doe"
        phone_number = "+1234567890"
        role = "BORROWER"

        user = CustomUser.objects.create_user(
            email, password, first_name, last_name, phone_number=phone_number, role=role
        )

        assert user.email == email
        assert user.check_password(password)
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.phone_number == phone_number
        assert user.role == role

    # Test that a superuser can be created with the required fields
    def test_create_superuser_with_required_fields(self):
        email = "test@example.com"
        password = "password"
        first_name = "John"
        last_name = "Doe"
        phone_number = "+1234567890"
        role = "LIBRARIAN"

        user = CustomUser.objects.create_superuser(
            email,
            password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role=role,
        )

        assert user.email == email
        assert user.check_password(password)
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.phone_number == phone_number
        assert user.role == role
        assert user.is_staff
        assert user.is_superuser
        assert user.is_active

    # Test that the user fields are updated correctly
    def test_update_user_fields(self):
        # Create a user
        user = CustomUser.objects.create_user(
            email="test@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
            phone_number="+123456789",
            role="BORROWER",
        )

        # Update the user fields
        user.first_name = "Jane"
        user.last_name = "Smith"
        user.phone_number = "+987654321"
        user.role = "LIBRARIAN"
        user.save()

        # Check that the fields are updated correctly
        assert user.first_name == "Jane"
        assert user.last_name == "Smith"
        assert user.phone_number == "+987654321"
        assert user.role == "LIBRARIAN"

    # Test that a user is successfully deleted from the database
    def test_delete_user(self):
        # Create a user
        user = CustomUser.objects.create_user(
            email="test@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
            phone_number="+123456789",
            role="BORROWER",
        )

        # Delete the user
        user.delete()

        # Check that the user is no longer in the database
        assert not CustomUser.objects.filter(email="test@example.com").exists()

    # Test that a user can be authenticated using their email and password
    def test_authenticate_user_with_email_and_password(self):
        # Create a user
        user = CustomUser.objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="John",
            last_name="Doe",
            phone_number="+123456789",
            role="BORROWER",
        )

        # Authenticate the user
        authenticated_user = CustomUser.objects.authenticate(
            email="test@example.com", password="password123"
        )

        # Check that the authenticated user is the same as the created user
        assert authenticated_user == user
