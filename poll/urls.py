from django.urls import path 
from. import views 

urlpatterns = [
    # ex: /poll/
    path(r'^$', views.index, name='index'),
    
    # ex: /poll/5/
    path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /poll/5/results/
    path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /poll/5/vote/
    path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]