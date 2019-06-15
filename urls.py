from django.conf.urls import url

from . import views

app_name = 'store'

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^about1/', views.about1, name='about1'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.book_list,name='book_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.book_detail,name='book_detail'),
]
