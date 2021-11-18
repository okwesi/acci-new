from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.Home.as_view(), name="home"),
    url("branches", views.Branch.as_view(), name="branches"),
    url("contact", views.contact, name="contact"),
    url("devotions", views.DevotionList.as_view(), name="devotion"),
    url('^(?P<pk>[0-9]+)/(?P<title>.+)/', views.DevotionView.as_view(), name="devotiondetail"),
]  