from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'polls.views.index'),
    url(r'^login$', 'polls.views.login'),
    url(r'^register$', 'polls.views.register'),
    url(r'^registeraction$', 'polls.views.registeraction'),
#    url(r'^registererror$', 'polls.views.registererror'),
    url(r'^loginaction$', 'polls.views.loginaction'),
    url(r'^logout$', 'polls.views.logout'),
    url(r'^about$', 'polls.views.about'),
    url(r'^insert$', 'polls.views.insert'),
    # url(r'^delete$', 'polls.views.delete'),
#    url(r'^loginerror$', 'polls.views.loginerror'),
    url(r'^insertaction$', 'polls.views.insertaction'),
    url(r'^view$', 'polls.views.view'),
]
