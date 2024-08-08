from django import forms
from django.contrib.auth.forms import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2,
                               error_messages={'required': '請輸入帳號名稱', 'max_length': '帳號長度需要在 2~20中間',
                                               'min_length': '帳號長度需要在 2~20中間'})
    email = forms.EmailField(error_messages={'required': '請輸入 email', 'invalid': '請輸入一個正確的 email'})
    # 驗證碼之後再做...
    password = forms.CharField(max_length=20, min_length=6)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('email 已經註冊過了！')
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'required': '請輸入 email', 'invalid': '請輸入一個正確的 email'})
    # 驗證碼之後再做...
    password = forms.CharField(max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)