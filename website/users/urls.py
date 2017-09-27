from django.conf.urls import url, include
from . import views

app_name = 'users'

from .views import (

    message_create,
    post_create,
    decrypttext,
    encrypttext,
    decryptmsg,
    signout,
    delete_m,
    delete_em,
    delete_f,
    guidepage,
    decryptfile,

)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^register/$', views.UserRegFormView.as_view(), name='register'),
    #url(r'^signin/$', views.UserLogFormView.as_view(), name='signin'),
    #url(r'^signout/$', signout, name='signout'),
    url(r'^encrypt/$', encrypttext, name='encrypttext'),
    url(r'^decrypt/$', decrypttext, name='decrypttext'),
    url(r'^upload/$', post_create, name='createpost'),
    url(r'^decryptfile/$', decryptfile, name='decryptfile'),
    url(r'^messages/$', message_create, name='createmsg'),
    url(r'^instructions/$', guidepage, name='guide'),
    url(r'^delete_m/(?P<id>\d+)/$', delete_m),
    url(r'^delete_em/(?P<id>\d+)/$', delete_em),
    url(r'^delete_f/(?P<id>\d+)/$', delete_f),
    #url(r'^(?P<id>\d+)/$', item_info),
    #url(r'^decryptmsg(?P<id>\d+)/$', decryptmsg),

    #include('registration.backends.default.urls')
    #url(r'^textencryption/$', views.textencryption, name='textencryption')



]