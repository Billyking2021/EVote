# Includes URL patterns
from django.urls import include, re_path, reverse_lazy, path
from django.contrib.auth import views as auth_views
from authentication import views

app_name = 'auth'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^userLogin/$', views.user_login, name='user_login'),
    re_path(r'^instruction/$', views.instruction, name='instruction'),
    re_path(r'^voting/$', views.voting, name='voting'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^candidatevote/$', views.candidatevote, name='candidatevote'),
    re_path(r'^partyvote/$', views.partyvote, name='partyvote'),

    # Password Reset URLs
    re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html',
        email_template_name='authentication/password_reset_email.html',
        success_url=reverse_lazy('auth:password_reset_done'),
    ), name='password_reset'),
    re_path(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html',
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html',
        success_url=reverse_lazy('auth:password_reset_complete')
    ), name='password_reset_confirm'),
    re_path(r'^password-reset-complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html',
    ), name='password_reset_complete'),
]
