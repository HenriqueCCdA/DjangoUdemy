from django.urls import path

from core.views import IndexListView


urlpatterns = [
    path('',IndexListView.as_view(), name='index')
]
