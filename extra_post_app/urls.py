"""
URL configuration for extra_post_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# ...
from django.conf import settings
from django.conf.urls.static import static  # 追加
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.core.exceptions import PermissionDenied
from django.http import (
    Http404,
    HttpResponseServerError,
)
from django.urls import include, path

from .error_handlers import (
    custom_bad_request,
    custom_page_not_found,
    custom_permission_denied,
    custom_server_error,
)
from .sitemaps import BlogPostSitemap, StaticViewSitemap

sitemaps = {
    "blog": BlogPostSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = custom_bad_request
handler403 = custom_permission_denied
handler404 = custom_page_not_found
handler500 = custom_server_error


# 各エラーを発生させるためのURLパターン
urlpatterns += [
    path("400/", lambda request: custom_bad_request(request, exception=None)),
    path("403/", lambda request: (_ for _ in ()).throw(PermissionDenied())),
    path("404/", lambda request: (_ for _ in ()).throw(Http404())),
    path(
        "500/",
        lambda request: (_ for _ in ()).throw(
            HttpResponseServerError("Internal Server Error")
        ),
    ),
]
