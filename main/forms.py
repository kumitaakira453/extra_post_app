from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Post, User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "メールアドレス"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "パスワード"}
        )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 各フィールドにクラスを追加する
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
            }
        )


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["title"].widget.attrs.update({"class": "form-control"})
        # self.fields["content"].widget.attrs.update({"class": "form-control"})
        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "タイトル",
            }
        )
        self.fields["content"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "本文",
            }
        )
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )


class UserInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "icon",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "user名",
            }
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "メールアドレス",
            }
        )
        self.fields["icon"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "アイコン画像",
            }
        )
