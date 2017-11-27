from django.conf.urls import url

from . import views
from .views import FilmListView

urlpatterns = [
    #url(r'^$', views.film_list),
    url(r'^$', FilmListView.as_view(), name='film'),
    url(r'(?P<pk>\d+)/$', views.filmdetail, name='film_detail'),

]
