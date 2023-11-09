# Includes URL patterns

from django.urls import path, include, re_path

from authentication import views
from election import views as eView

# Includes home page to URL
urlpatterns = [
    path('', views.home, name='home'),  # Changed to path for non-regex pattern
]
