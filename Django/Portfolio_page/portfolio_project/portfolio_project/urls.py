"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import angry_dice.views
import forum.views
import JavaPic.views
import JavaPic_Jquery.views
from port_main import views as main_views
import port_main.views
import random_quote.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.main),
    url(r'^angry_dice/$', angry_dice.views.main, name='Angry Dice'),
    url(r'^forum/$', forum.views.main),
    url(r'^JavaPic/$', JavaPic.views.javapic_main),
    url(r'^JavaPic/Join/$', JavaPic.views.join),
    url(r'^JavaPic/Gallery/', JavaPic.views.gallery),
    url(r'^JavaPic_Jquery/$', JavaPic_Jquery.views.main),
    url(r'^JavaPic_Jquery/Join$', JavaPic_Jquery.views.join),
    url(r'^JavaPic_Jquery/Gallery/', JavaPic_Jquery.views.gallery),
    url(r'^random_quote/$', random_quote.views.main),
]
