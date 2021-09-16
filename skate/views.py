# from skate.permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SkateSerializer
from .models import Skate
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework import generics
# from rest_framework import permissions

# Create your views here.
class SkateList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Skate.objects.all()
    serializer_class = SkateSerializer


class SkateDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Skate.objects.all()
    serializer_class = SkateSerializer
