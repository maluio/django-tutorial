from django.urls import path

from . import views

# https://docs.djangoproject.com/en/3.1/intro/tutorial03/#namespacing-url-names
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # https://docs.djangoproject.com/en/3.1/intro/tutorial03/#removing-hardcoded-urls-in-templates
    path('<int:question_id>/vote/', views.vote, name='vote'),
]