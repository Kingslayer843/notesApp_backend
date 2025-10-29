from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListCreateView.as_view(), name='note-list-create'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note-detail-no-slash'),
]
