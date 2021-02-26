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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
