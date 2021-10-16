from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #signup and login
    path('signup/', views.signup),
    path('login/', views.login),

    #access and refresh token
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    #snippets
    path('snippets/', views.SnippetOverView.as_view()),
    path('snippets/create/', views.SnippetCreate.as_view()),
    path('snippets/<int:pk>/', views.SnippetRetrieveUpdateDestroy.as_view()),
]

