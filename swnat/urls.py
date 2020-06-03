"""swnat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from nurseapp import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^403/', views.error403),
    url(r'^$', auth_views.LoginView.as_view(), name='login'),

    # user auth
    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^home2/$', views.home2, name='home'),
    url(r'^patient_historics/$', views.patient_historics, name='patient_historics'),

    # url(r'^publico/$', views.panel_publico, name='panel_publico'),

    url(r'^patients/$', views.adm_patient, name='patient_list'),
    url(r'^patients/add/$', views.adm_patient_add, name='patient_add'),
    url(r'^patients/edit/$', views.adm_patient_mod, name='patient_edit'),
    url(r'^patients/delete/$', views.adm_patient_del, name='patient_del'),

    url(r'^records/$', views.adm_record, name='record_list'),
    url(r'^records/add/$', views.adm_record_add, name='record_add'),
    url(r'^records/edit/$', views.adm_record_mod, name='record_edit'),
    url(r'^records/delete/$', views.adm_record_del, name='record_del'),

    url(r'^ranges/$', views.adm_range, name='range_list'),
    url(r'^ranges/add/$', views.adm_range_add, name='range_add'),
    url(r'^ranges/edit/$', views.adm_range_mod, name='range_edit'),
    url(r'^ranges/delete/$', views.adm_range_del, name='range_del'),

]
