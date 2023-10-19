from django.urls import path
from .views import NoteListCreateAPIView, NoteUpdateAPIView, NoteDestroyAPIView, NoteDetailAPIView

urlpatterns = [
    path('', NoteListCreateAPIView.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetailAPIView.as_view(), name='delete'),
    path('delete/<int:pk>/', NoteDestroyAPIView.as_view(), name='delete'),
    path('update/<int:pk>/', NoteUpdateAPIView.as_view(), name='update')
]
