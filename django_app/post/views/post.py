"""
- class-based view로
    PostList, PostDetail, PostCreate, PostDelete 뷰를 작성
"""
from django.views import View

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
)


class PostList(View):
    pass


class PostDetail(View):
    pass


class PostDelete(View):
    pass