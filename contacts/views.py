from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from _core.permissions import IsSuperUserOrSafeMethod
from .models import Contact
from .serializers import ContactSerializer


class ContactListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrSafeMethod]

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrSafeMethod]

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_url_kwarg = "contact_id"
