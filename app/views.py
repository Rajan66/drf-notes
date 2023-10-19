from django.shortcuts import render
from rest_framework import generics
from .serializers import NoteSerializer
from .models import Note

# Create your views here.


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        if not instance.title:
            instance.title = instance.body
        return instance


class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        if not instance.title:
            instance.title = instance.body
        return instance


class NoteDestroyAPIView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
