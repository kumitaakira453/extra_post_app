from django.contrib import admin

# Register your models here.
from .models import Favorite, Post, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_staff"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "posted_by__username", "posted_at", "updated_at"]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user__username",
        "post__title",
    ]
