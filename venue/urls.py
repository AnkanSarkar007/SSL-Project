from django.urls import path
from . import views
from .views import VenuePostListView, VenueListView

urlpatterns = [
    path('', VenueListView.as_view(), name='venue-home'),
    path('<int:id>/', VenuePostListView.as_view(), name='venue-posts'),
]