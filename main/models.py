from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField(upload_to="user_icons", blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "email"  # ☆2 このテーブルのレコードを一意に識別
    REQUIRED_FIELDS = ["username"]  # スーパーユーザ作成時に入力する

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    title = models.CharField("タイトル", max_length=50)
    content = models.TextField("内容")
    image = models.ImageField("画像", upload_to="post_images", blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by{self.posted_by.username}"

    class Meta:
        verbose_name = "ポスト"
        verbose_name_plural = "ポスト"


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_posts"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="favorited_by_users"
    )

    class Meta:
        verbose_name = "いいね"
        verbose_name_plural = "いいね"
