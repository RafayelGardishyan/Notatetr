from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('', views.index),
    path('register', views.register),
    path('<int:id>/notes', views.logged_user_home),
    path('logout', views.logout),
    path('add', views.add),
    path('note/<int:id>', views.note),
    path('note/edit/<int:id>', views.note_edit),
    path('note/delete/<int:id>', views.note_delete),
]
