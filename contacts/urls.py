from django.urls import path
from .views import (
    ContactListCreateView,
    ContactRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("contacts/", ContactListCreateView.as_view()),
    path(
        "contacts/<int:contact_id>/",
        ContactRetrieveUpdateDestroyView.as_view()
    ),
]
