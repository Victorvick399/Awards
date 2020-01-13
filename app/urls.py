from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name='Home'),
    url(r'^about/',views.about, name='About'),
    path('new/post/',views.new_post,name='new_post'),
    url(r'profile/',views.profile,name='Profile'),
    path(r'single_post/<int:post_id>',views.single_post,name="single_post"),
    path(r'update_post/<int:post_id>',views.update_post,name="update_post"),
    path('profile/<username>',views.other_profiles,name="other_profiles"),
    path('update/profile/',views.update_profile,name='update_profile'),
    url(r'^search/$',views.search,name="search"),
    path('logout',views.logout,name='logout')
]
