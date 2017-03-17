from rest_framework import serializers

from post.models import Post

__all__ = (
    'PostSerializer',
    'UserSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    """
    author 필드의 값이 pk가 아닌 하나의 Object(dict)로 나타나도록 수정
    1. 관련 테스트코드 작성
        post_list, post_create부분
    2. 해당 테스트코드가 작동하도록 PostSerializer를 수정 및 UserSerializer 작성
    3. 테스트 및 포스트맨 작동 확인
    """

    # user = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
        )
        read_only_fields = (
            'author',
            'created_date',
        )
