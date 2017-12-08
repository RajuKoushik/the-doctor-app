from django.conf.urls import url
from rest_framework.authtoken import views as rest_views
from . import views

urlpatterns = [

    url(r'^login/', rest_views.obtain_auth_token),
    url(r'^signup/?', views.signup),
    url(r'^home/?', views.home, name='home'),
    url(r'^login/', rest_views.obtain_auth_token),

]
