from django.urls import path
from .views import (
    # Trainer Views
    TrainerListView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView,
    # Client Views
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    # Session Views
    SessionListView, SessionCreateView, SessionUpdateView, SessionDeleteView,
    # Rating Views
    RatingListView, RatingCreateView, RatingUpdateView, RatingDeleteView,
    # Message Views
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView,
    # Login Views
    register_trainer, register_client,DashboardView,home
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Home URL
    path('', home, name='home'),
    # Trainer URLs
    path('trainers/', TrainerListView.as_view(), name='trainer-list'),
    path('trainers/create/', TrainerCreateView.as_view(), name='trainer-create'),
    path('trainers/<int:pk>/update/', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainers/<int:pk>/delete/', TrainerDeleteView.as_view(), name='trainer-delete'),

    # Client URLs
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

    # Session URLs
    path('sessions/', SessionListView.as_view(), name='session-list'),
    path('sessions/create/', SessionCreateView.as_view(), name='session-create'),
    path('sessions/<int:pk>/update/', SessionUpdateView.as_view(), name='session-update'),
    path('sessions/<int:pk>/delete/', SessionDeleteView.as_view(), name='session-delete'),

    # Rating URLs
    path('ratings/', RatingListView.as_view(), name='rating-list'),
    path('ratings/create/', RatingCreateView.as_view(), name='rating-create'),
    path('ratings/<int:pk>/update/', RatingUpdateView.as_view(), name='rating-update'),
    path('ratings/<int:pk>/delete/', RatingDeleteView.as_view(), name='rating-delete'),

    # Message URLs
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message-update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),

    # Register URLs
    path('register/trainer/', register_trainer, name='register_trainer'),
    path('register/client/', register_client, name='register_client'),

    #login URLs
    path('login/', LoginView.as_view(template_name='core/auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]