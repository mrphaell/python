from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/create$', views.UserCreate.as_view(), name='users-create'),
    url(r'^users/list$', views.UserList.as_view(), name='users-list'),
    url(r'^users/update$', views.UserUpdate.as_view(), name='users-update'),
    url(r'^users/delete$', views.UserDelet.as_view(), name='users-delete'),
    url(r'^users/$', views.UserAll.as_view(), name='users-delete'),
]