from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('update_task/<str:pk>/', views.updateTask, name='update_task'),
    url('delete/<str:pk>/', views.deleteTask, name='delete'),
    url(r'^user/profile', views.profile, name='profile'),
    url(r'^update/user/',views.update_profile, name='update_profile'),
    url(r'^user/(?P<username>\w+)', views.user_profile, name='user_profile'),
    # url(r'^new/profile$', views.add_profile, name='add_profile'),
]