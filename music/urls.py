from django.urls import path
from . import views

app_name = 'song'
urlpatterns = [
    path('', views.showsongs),
    path('<int:song_id>', views.song_detail, name='song_detail'),
    path('edit/<int:song_id>', views.song_edit, name='song_edit'),
    path('edit/action', views.edit_action, name='edit_action')
]
