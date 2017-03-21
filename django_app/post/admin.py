from django.contrib import admin

from post.models.post import Post
from post.models.post import PostPhoto

admin.site.register(Post)
admin.site.register(PostPhoto)
