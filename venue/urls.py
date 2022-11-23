from django.urls import path
from . import views
from .views import VenuePostListView, VenueListView, VenueFilterListView, VenueSortListView, VenueSortFilterListView

urlpatterns = [
    path('', VenueListView.as_view(), name='venue-home'),
    path('sort/<slug:sort>', VenueSortListView.as_view(), name='venue-home-sort'),
    path('<int:id>/', VenuePostListView.as_view(), name='venue-posts'),
    path('type/<slug:type>/', VenueFilterListView.as_view(), name='venue-type'),
    path('type/<slug:type>/sort/<slug:sort>', VenueSortFilterListView.as_view(), name='venue-type-sort')
]