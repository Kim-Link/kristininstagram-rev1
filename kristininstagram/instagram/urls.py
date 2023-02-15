from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL을 만들어줌. router.urls에 리스트 형태로 들어가게됨

urlpatterns =[
    path('public/', views.PublicPostListAPIView.as_view()),
    path('', include(router.urls))
]
