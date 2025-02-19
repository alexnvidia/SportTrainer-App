from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Trainer, Client, Session, Rating, Message
from .forms import TrainerForm, ClientForm, SessionForm, RatingForm, MessageForm, UserRegistrationForm, TrainerRegistrationForm, ClientRegistrationForm
from django.contrib.auth import login



# Trainer Views
class TrainerListView(LoginRequiredMixin, ListView):
    model = Trainer
    template_name = 'core/trainer_list.html'
    context_object_name = 'trainers'

class TrainerCreateView(LoginRequiredMixin, CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'core/trainer_form.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'core/trainer_form.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainer
    template_name = 'core/trainer_confirm_delete.html'
    success_url = reverse_lazy('trainer-list')

# Client Views
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'core/client_list.html'
    context_object_name = 'clients'

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'core/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'core/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'core/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')

# Session Views
class SessionListView(LoginRequiredMixin, ListView):
    model = Session
    template_name = 'core/session_list.html'
    context_object_name = 'sessions'

class SessionCreateView(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm
    template_name = 'core/session_form.html'
    success_url = reverse_lazy('session-list')

class SessionUpdateView(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'core/session_form.html'
    success_url = reverse_lazy('session-list')

class SessionDeleteView(LoginRequiredMixin, DeleteView):
    model = Session
    template_name = 'core/session_confirm_delete.html'
    success_url = reverse_lazy('session-list')

# Rating Views
class RatingListView(LoginRequiredMixin, ListView):
    model = Rating
    template_name = 'core/rating_list.html'
    context_object_name = 'ratings'

class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'core/rating_form.html'
    success_url = reverse_lazy('rating-list')

class RatingUpdateView(LoginRequiredMixin, UpdateView):
    model = Rating
    form_class = RatingForm
    template_name = 'core/rating_form.html'
    success_url = reverse_lazy('rating-list')

class RatingDeleteView(LoginRequiredMixin, DeleteView):
    model = Rating
    template_name = 'core/rating_confirm_delete.html'
    success_url = reverse_lazy('rating-list')

# Message Views
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'core/message_list.html'
    context_object_name = 'messages'

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'core/message_form.html'
    success_url = reverse_lazy('message-list')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'core/message_form.html'
    success_url = reverse_lazy('message-list')

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'core/message_confirm_delete.html'
    success_url = reverse_lazy('message-list')

class DashboardView(View):
    def get(self, request):
        user = request.user
        context = {}

        if hasattr(user, 'trainer'):
            context['trainer'] = user.trainer
            context['clients'] = user.trainer.clients.all()
        elif hasattr(user, 'client'):
            context['client'] = user.client
            context['trainers'] = Trainer.objects.all()

        return render(request, 'core/dashboard.html', context)

def register_trainer(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        trainer_form = TrainerRegistrationForm(request.POST)
        if user_form.is_valid() and trainer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            trainer = trainer_form.save(commit=False)
            trainer.user = user
            trainer.save()
            login(request, user)
            return redirect('trainer-list')  # Cambia esto a la vista que prefieras
    else:
        user_form = UserRegistrationForm()
        trainer_form = TrainerRegistrationForm()
    return render(request, 'core/register_trainer.html', {'user_form': user_form, 'trainer_form': trainer_form})

def register_client(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            client = Client.objects.create(user=user)
            login(request, user)
            return redirect('client-list')  # Cambia esto a la vista que prefieras
    else:
        user_form = UserRegistrationForm()
    return render(request, 'core/register_client.html', {'user_form': user_form})

def home(request):
    return render(request, 'core/home.html')


