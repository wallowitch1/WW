from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    # 요청 메소드가 POST 일 때
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)


        # 로그인 성공시 메인 페이지로 이동
        if user is not None:
            login(request, user)
            print("Login success. {}".format(user.get_username()))
            return redirect('/')
        else:
            print("Login fail")


    return render(request, 'user/login.html')

# 사용자 로그아웃
def user_logout(request):
    logout(request)
    return redirect('user/login.html')

# 사용자 등록(회원가입)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password_check = request.POST.get('password2')
        if password == password_check:
            User.objects.create_user(username=username, password=password)
            return redirect('/user/login')
        
    return render(request, 'user/register.html')
