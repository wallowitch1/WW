from django.urls import path
from . import views  # 현재 앱(main)의 views.py 파일에서 뷰를 import

urlpatterns = [
    path('', views.home, name='home'),
    # 다른 URL 패턴들...
]