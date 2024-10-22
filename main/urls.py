from django.urls import path

from main import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("index/", views.PostListView.as_view(), name="index"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/detail/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("favorite/", views.post_favorite_register, name="favorite"),
    path(
        "user/change_info", views.UserInfoUpdateView.as_view(), name="user_info_update"
    ),
]
