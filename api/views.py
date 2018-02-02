from django.shortcuts import render

# Create your views here.
from notatetr.models import User, Note
from rest_framework import viewsets
from .serializers import UserSerializer, NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer