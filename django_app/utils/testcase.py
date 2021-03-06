from django.contrib.auth import get_user_model

User = get_user_model()


class APITestCaseAuthMixin(object):
    test_username = 'jinsoo'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def create_user_and_login(self, client):
        user = self.create_user()
        self.client.login(
            username=self.test_username,
            password=self.test_password,
        )
        return user
