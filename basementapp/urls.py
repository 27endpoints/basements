from django.urls import path
from .views import Residents_collection_view, basement_accommodation_view, about_view, Resident_details_view

urlpatterns = [
    path("Residents/", Residents_collection_view, name="Residents_collection_view"),
    path("basements_Dlangezwa/", basement_accommodation_view, name="basement_accommodation_view"),
    path("about_us/", about_view, name="about_view" ),
    path("Resident/<int:Resident_id>/", Resident_details_view, name="Resident_details_view"),
]