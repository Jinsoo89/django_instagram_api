from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post
from post.serializers.post_photo import PostPhotoSerializer

__all__ = (
    'PostSerializer',
    'UserSerializer',
)

"""
author 필드의 값이 pk가 아닌 하나의 Object(dict)로 나타나도록 수정
1. 관련 테스트코드 작성
    post_list, post_create부분
2. 해당 테스트코드가 작동하도록 PostSerializer를 수정 및 UserSerializer 작성
3. 테스트 및 포스트맨 작동 확인

post에 연결된 PostPhoto를 리스트 내부의 Object형태로 리턴
    'author': {<author object>},
    'postphoto_set': [
        {
            'pk': <PostPhoto pk>,
            'photo': <PostPhoto photo field url>,
        },
    ]
1. 관련 테스트코드 작성
    post_list, post_create부분
2. 해당 테스트코드가 작동하도록 PostSerializer를 수정 및 PostPhotoSerializer 작성
3. 테스트 및 포스트맨 작동 확인
"""


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    photo_list = PostPhotoSerializer(many=True, read_only=True, source='postphoto_set')

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo_list',
            'created_date',
        )
        read_only_fields = (
            'created_date',

        )
