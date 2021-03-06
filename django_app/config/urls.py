"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

# HttpResponse / HttpRequest를 위한 url
from post.urls import views as post_urls
from post.urls import apis as post_apis_urls
from member.urls import apis as member_apis_urls

api_urlpatterns = [
    url(r'^post/', include(post_apis_urls)),
    url(r'^member/', include(member_apis_urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include(post_urls)),
    url(r'^api/', include(api_urlpatterns, namespace='api')),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
