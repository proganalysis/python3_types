from django.test import TestCase
from core.models import Profile, User


class ProfileTestCase(TestCase):
    """This class defines the test suite for the Person model."""

    def setUp(self):
        """Define the test variables."""
        self.username = "some-test-user"
        self.email = "some@test.user"
        self.password = "passgoeshere123"
        self.user = User(
                username=self.username,
                email=self.email,
                password=self.password
            )


    def test_model_can_create_a_profile(self):
        """Test the Person model can create a profile."""
        old_count = Profile.objects.count()
        self.user.save()

        self.profile = self.profile = Profile(user=self.user)
        self.profile.save()
        new_count = Profile.objects.count()
        self.assertNotEqual(old_count, new_count)
