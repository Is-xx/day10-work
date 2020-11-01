from django.urls import path
from app import views


urlpatterns = [
    path('login/', views.UserLogin.as_view({'post': 'login'})),
    path('info/', views.UserInfo.as_view()),
    path('info/<str:id>', views.UserInfo.as_view()),
]