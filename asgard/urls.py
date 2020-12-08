"""asgard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from asgard_mvc import views as v
from asgard import settings

urlpatterns = [
    path('', v.index, name='index'),
    path('profile/', v.userprofile_view, name='user_profile'),
    path('ar/', v.ar_view, name='ar'),
    path('quiz/', v.quiz_view, name='quiz'),
    path('discussion/', v.discussion_view, name='discussion'),
    re_path(r'^discussion/send_message/$', v.send_message_json, name='send_message_json'),
    re_path(r'^discussion/refresh_message/$', v.get_new_message_json, name='get_new_message_json'),
    path('admin/', admin.site.urls),
    path('accounts/login/', v.login_view, name='login'),
    path('accounts/register/', v.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)