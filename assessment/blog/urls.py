from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.SignInView.as_view()),
    path("sign_up/", views.SignUpView.as_view()),
    path("post/", views.PostListCreateAPIView.as_view()),
    path("post/<int:pk>/", views.PostDetailAPIView.as_view()),
    path('assign-permissions/', views.AssignPermissions.as_view()),
    path('revoke-permissions/', views.RevokePermissions.as_view()),

   
]
