from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
]
