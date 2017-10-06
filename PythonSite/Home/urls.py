from django.conf.urls import url

from Home.views import HomePageView

urlpatterns = [
    url('^Home', HomePageView.as_view(), name='home')
]