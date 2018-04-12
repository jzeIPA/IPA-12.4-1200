from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse
from benutzeraccounts import views

#alle URLs die aufrubar sind, werden hier aufgelistet. Die Views-Funktionen werden angesprochen

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'benutzeraccounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^profil/$', views.profile, name='profile'),
    url(r'^profil/bearbeiten/$', views.edit_profile, name='edit_profile'),

    url(r'^passwort_wechseln/$', views.change_password, name='change_password'),

    url(r'^registrieren/$', views.register, name='register'),
]
