from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    
    path('worldwide', views.worldwide, name='worldwide'),

    path('resource', TemplateView.as_view(template_name="resources.html"), name='resource'),

]