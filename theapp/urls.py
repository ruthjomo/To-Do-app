from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #    url(r'^user/(?P<username>\w+)', views.user_profile, name='user_profile'),
    
    
    
]