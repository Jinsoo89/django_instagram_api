from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase

User = get_user_model()


class PostTest(APILiveServerTestCase):
    test_username = 'jinsoo'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def test_create_post(self):
        # Post.objects.create(
        #     author=user,
        #     photo=
        # )
        pass

    def test_cannot_create_post_not_authenticated(self):
        url = reverse('post-create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTO_403_FORBIDDEN)

    def test_post_list(self):
        pass

    def test_post_update(self):
        pass

    def test_post_retrieve(self):
        pass

    def test_post_destroy(self):
        pass
