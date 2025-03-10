
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from _core.permissions import (
    IsSuperUserOrSafeMethod,
    IsSuperUserOrOwnsAccount
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .models import User


class UserListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrSafeMethod]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrOwnsAccount]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"
