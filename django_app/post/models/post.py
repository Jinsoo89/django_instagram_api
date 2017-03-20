from django.conf import settings
from django.db import models

__all__ = (
    'Post',
    'PostPhoto',
)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pk',)


class PostPhoto(models.Model):
    post = models.ForeignKey(Post)
    photo = models.ImageField(upload_to='post')
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'post'

        # def to_dict(self):
        #     ret = {
        #         'pk': self.pk,
        #         'photo': self.photo.url,
        #     }
        #     return ret
