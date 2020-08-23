from django.conf.urls import url
from .views import like_button

app_name="like_button"

urlpatterns=[
  
    url(r'^$',like_button, name='like'),

 ]
