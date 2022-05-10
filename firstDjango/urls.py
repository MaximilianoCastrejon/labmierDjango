"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from articles.views import (
                            trending_screen, 
                           articles_display,
                            read_article, profile, 
                            graphsAndData, 
                            favourites, 
                            messages, 
                            settings_page, 
                            user_file_manager,
                            make_article,
                            home_section
                            )

urlpatterns = [
    
    path('', home_section, name='home'),
#ARTICLES URLS

    path('trending', trending_screen, name='trending'),
    path('articles', articles_display, name='article_blocks'),
    path('articles/<int:id>', read_article, name='read_article'),
    path('create', make_article, name='post_article'),
    # AJAX load form
    # path('create/article'),
    # path('create/data'),

#PROFILE URLS

    path('profile', profile, name='user_profile'),
    # path('register'),
    path('settings', settings_page, name='settings'),
    path('files', user_file_manager, name='user_files'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

#DATA

    path('graphs-and-data', graphsAndData, name='data'),
    path('favourites', favourites, name='liked_articles'),
    path('messages', messages, name='messages'),

    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
