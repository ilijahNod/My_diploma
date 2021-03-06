from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path(r'login/', auth_views.LoginView.as_view(), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(r'register/', views.register, name='register'),
    path(r'logout-then-login/', auth_views.logout_then_login,
         name='logout_then_login'),
    path(r'', views.dashboard, name='dashboard'),
    path(r'edit_bio/<int:pk>', views.AuthorUpdateView.as_view(), name='author_edit'),
    path(r'password-change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_form.html'), name='password_change'),
    path(r'password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'), name='password_change_done'),
    path(r'password-reset/', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset.html'), name='password_reset'),
    path(r'password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_change_done.html'), name='password_reset_done'),
    path(r'password-reset/confirm/(<uidb64>[-\w]+)/(<token>[-\w]+)/', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path(r'password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete'),
]
