from django.urls import path, include, re_path
from django.contrib import admin
from authentication import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('home/', include('election.urls')),
]

urlpatterns += staticfiles_urlpatterns()