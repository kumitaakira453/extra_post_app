from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Exists, OuterRef, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import LoginForm, PostCreateForm, SignUpForm, UserInfoUpdateForm
from .models import Favorite, Post

# Create your views here.


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm  # ログイン用のフォームを指定
    template_name = "main/login.html"  # テンプレートを指定


class LogoutView(auth_views.LogoutView):
    pass


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "main/signup.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class PostListView(generic.ListView):
    model = Post
    template_name = "main/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(favorite_count=Count("favorited_by_users"))
        if self.request.user.is_authenticated:
            favorite_subquery = Favorite.objects.filter(
                post=OuterRef("pk"),  # 現在のPostオブジェクト
                user=self.request.user,
            )
            # annotateにExistsを使って、True/Falseを返す
            queryset = queryset.annotate(is_favorited_by_user=Exists(favorite_subquery))
        serach_key = self.request.GET.get("key")
        if serach_key:
            queryset = queryset.filter(
                Q(title__icontains=serach_key) | Q(content__icontains=serach_key)
            )
        return queryset


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "main/post_create.html"
    success_url = reverse_lazy("index")
    form_class = PostCreateForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.posted_by = self.request.user
        return super().form_valid(form)


class PostDetailView(generic.DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "main/post_detail.html"
    success_url = reverse_lazy("index")


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = "main/post_update.html"
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})


class UserInfoUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "main/change_userinfo.html"
    model = Post
    success_url = reverse_lazy("index")
    form_class = UserInfoUpdateForm

    def get_object(self, queryset=None):
        return self.request.user


def post_favorite_register(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, pk=post_id)
    favorite = Favorite.objects.filter(post=post, user=request.user).first()
    if favorite:
        favorite.delete()
    else:
        Favorite.objects.create(user=request.user, post=post)
    favorite_count = Favorite.objects.filter(post=post).count()
    context = {
        "message": "success",
        "favorite_count": favorite_count,
    }

    return JsonResponse(context)
