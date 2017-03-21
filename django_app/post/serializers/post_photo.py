from rest_framework import serializers

from post.models.post import PostPhoto

__all__ = (
    'PostPhotoSerializer',
)


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = (
            'post',
            'photo',
        )
