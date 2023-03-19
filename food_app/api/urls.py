from .views import api_search,api_post,api_display,api_display_internal
from django.urls import path 
urlpatterns = [
    path('search/',api_search,name='api_searchs'),
    path('list/',api_post,name='api_post'),
    path('list/display/',api_display,name='api_display'),
    path('list/display_internal/',api_display_internal,name='api_display_internal'),
]