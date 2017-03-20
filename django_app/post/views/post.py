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
from django.views.generic import DetailView
from django.views.generic import ListView

from post.models import Post

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
)


class PostList(ListView):
    """
    1. 데이터추가
        Postman으로 Post두개 만들고 각각의 Post에 PostPhoto를 3개 추가
    2. post_list.html에서 posts변수를 loop하며 각 post의 postphoto_set.all을 loop
        postphoto_set을 내부에서 loop하며 내부 loop아이템의 photo.url을 이용해 이미지 출력
    """
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    """
    DetailView를 상속받아서 구현되도록
    """
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context


class PostDelete(View):
    pass
