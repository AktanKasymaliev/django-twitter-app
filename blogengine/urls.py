from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from accounts.views import signingup



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('signup/', signingup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts_auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts_auth/logout.html'), name='logout'),
    path('reset/password/', auth_views.PasswordResetView.as_view(template_name='accounts_auth/password_reset_mail.html',
                                                                email_template_name='accounts_auth/password_reset.html',
                                                                subject_template_name='accounts_auth/password_reset_subject.txt',
                                                                ), name='password_reset'),
    path('reset/password/done/', auth_views.PasswordResetDoneView.as_view(
                                    template_name='accounts_auth/password_reset_done.html'),
                                    name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(
                                    template_name='accounts_auth/password_reset_confirm.html'),
                                    name='password_reset_confirm'),
    # path('reset/<slug:uidb64>/<slug:token>/', sending, name='password_reset_confirm'),
    path('reset/password/complete/', auth_views.PasswordResetCompleteView.as_view(
                                    template_name='accounts_auth/password_reset_complete.html'),
                                    name='password_reset_complete'),
    path('change/password/password/', auth_views.PasswordChangeView.as_view(
                                    template_name='accounts_auth/password_change.html'),
                                    name='password_change'),
    path('change/password/done/', auth_views.PasswordChangeDoneView.as_view(
                                        template_name='accounts_auth/password_change_done.html'),
                                        name='password_change_done'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
