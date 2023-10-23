from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    # ex: /fun_polls/
    path('', views.index, name='index'),
    # ex: /fun_polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /fun_polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /fun_polls/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]