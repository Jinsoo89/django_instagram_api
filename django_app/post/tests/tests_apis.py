from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase

from post.models import Post

User = get_user_model()


class PostTest(APILiveServerTestCase):
    test_username = 'jinsoo'
    test_password = 'test_password'
    test_created_date = '2017.01.01'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def create_post(self):
        # Post.objects.create(
        #     author=self.create_user(),
        #     created_date=self.test_created_date,
        # )

        url = reverse('post-create')
        data = {
            'author': self.test_username,
            'created_date': self.test_created_date,
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        return response

    def test_create_post(self):
        # Post를 만들 유저를 생성 및 로그인
        user = self.create_user()
        self.client.login(username=self.test_username,
                          password=self.test_password)
        # Post를 생성하는 API주소를 reverse
        url = reverse('post-create')
        # Post를 생성하는 API주소에 POST요청, response를 받아옴
        response = self.create_post(url)
        print(response.status_code)

        # response의 status_code가 201(created)이어야 함
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # 생성 후 Post인스턴스가 총 한개어여함
        self.assertEqual(Post.objects.count(), 1)
        # 생성된 Post인스턴스의 author pk(id)가 테스트시 생성한 User의 pk(id)와 같아야함
        post = Post.objects.first()
        self.assertEqual(post.author.id, user.id)
        # self.assertEqual(response.data.get('author'), self.test_username)
        # self.assertEqual(response.data.get('created_date'),
        #                  self.test_created_date)

    def test_cannot_create_post_not_authenticated(self):
        url = reverse('post-create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.exists(), False)

    def test_post_list(self):
        pass

    def test_post_update(self):
        pass

    def test_post_retrieve(self):
        pass

    def test_post_destroy(self):
        pass
