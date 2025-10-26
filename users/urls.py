from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegistrationView, email_verification, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('email-confirm/<str:token>', email_verification, name='email_confirm'),
    path('update_profile/', UserUpdateView.as_view(), name="update_profile"),
]
