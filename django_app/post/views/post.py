"""
- class-based view로
    PostList, PostDetail, PostCreate, PostDelete 뷰를 작성
- 기존 프로젝트의 설정 가져와서 PostList가 작동하도록 구현
    1. settings.py
        STATIC_DIR,, STATICFILES_DIRS 설정
    2. 기존프로젝트의 static폴더 복사
    3. .gitignore에 django_app/static/css/ 추가
    4. 기존 프로젝트의 templates폴더 복사
        TEMPLATE_DIR 변수 설정 TEMPLATE설정의 TEMPLATE_DIRS에 해당 변수 추가
    5. PostList CBV에 get메서드 작성 및 내부 쿼리를 return
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
