from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^success/$', views.success, name="success"),
  url(r'^new/$', views.new, name="new"),
  url(r'^login/$', views.login, name="login"),
  url(r'^create/$', views.create, name="create"),
  url(r'^logout/$', views.logout, name="logout"),

  #CRUD 
  url(r'^add/$', views.add, name="add"), #directs to the add a book page
  url(r'^createbook/$', views.createbook, name="createbook"),#directs to the 'show' book page
  url(r'^showbook/$', views.showbook, name="showbook"), #shows all the books created so far, from previous setup route
  
  url(r'^(?P<id>[0-9]+)/show$', views.show), #matches 10/show
  #  url(r'^add/(?P<id>[0-9]+)/createbook/$', views.createbook, name="createbook"),
]