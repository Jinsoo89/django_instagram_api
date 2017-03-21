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
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView

from post.forms import PostForm
from post.models.comment import PostComment
from post.models.post import Post, PostPhoto

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
    'PostCreate',
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


class PostCreate(FormView):
    """
    FormView를 상속받아 구현
    attributes
        template_name
        form_class
        success_url
    method
        form_valid(self, form)
            request는 self.request로 접근 가능
            form.cleaned_data는 바로 사용 가능
            redirect는 정의해줄 필요 없음
    """
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = '/post/'

    def form_valid(self, form):
        post = Post.objects.create(author=self.request.user)
        content = form.cleaned_data.get('content').strip()
        if content is not None:
            PostComment.objects.create(
                post=post,
                author=self.request.user,
                content=content,
            )
        photos = self.request.FILES.getlist('photos')
        for photo in photos:
            PostPhoto.objects.create(
                post=post,
                photo=photo,
            )
        return super(PostCreate, self).form_valid(form)

        # form_class = PostForm
        # template_name = 'post/post_create.html'
        #
        # def get(self, request, *args, **kwargs):
        #     form = self.form_class(request.POST)
        #     context = {
        #         'form': form,
        #     }
        #     return render(request, self.template_name, context)
        #
        # def post(self, request, *args, **kwargs):
        #     form = self.form_class(request.POST, request.FILES)
        #     # 해당 request.user를 author로 하는 Post인스턴스 생성
        #     if form.is_valid():
        #         post = Post.objects.create(author=request.user)
        #         # 2. 만약 form.cleaned_data['content']가 빈 값이 아니면 PostComment 인스턴스 생성
        #         content = form.cleaned_data.get('content').strip()
        #         if content is not None:
        #             PostComment.objects.create(
        #                 author=request.user,
        #                 content=content,
        #                 post=post,
        #             )
        #         # 3. request.FILES.getlist('photos')를 loop하며 PostPhoto 인스턴스 생성
        #         photos = request.FILES.getlist('photos')
        #         for photo in photos:
        #             PostPhoto.objects.create(
        #                 post=post,
        #                 photo=photo,
        #             )
        #         # 4. return redirect('post:post-list')
        #         return redirect('post:post-list')
        #     else:
        #         return HttpResponse(form.errors)


class PostDetail(DetailView):
    """
    DetailView를 상속받아서 구현되도록
    """
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:post-list')
