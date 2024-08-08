from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login, logout

User = get_user_model()


# Create your views here.
@require_http_methods(['GET', 'POST'])
def blog_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                # 登入
                login(request, user)
                # 判斷是否記住我
                if not remember:
                    # 如果沒有點擊記住我 那要設置過期時間為 0 瀏覽器關閉後會過期
                    request.session.set_expiry(0)
                # 如果點擊了 就用默認的兩週時間
                return redirect('/')
            else:
                form.add_error(None, 'email 或密碼錯誤！')
            return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


def blog_logout(request):
    logout(request)
    return redirect('/')

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(email=email, username=username, password=password)
            return redirect(reverse('blog_auth:login'))
        else:
            print(form.errors)
            return render(request, 'register.html', context={"form": form})
