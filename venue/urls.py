from django.urls import path
from . import views
from .views import VenuePostListView, VenueListView, VenueFilterListView

urlpatterns = [
    path('', VenueListView.as_view(), name='venue-home'),
    path('<int:id>/', VenuePostListView.as_view(), name='venue-posts'),
    path('<slug:type>/', VenueFilterListView.as_view(), name='venue-type')
]