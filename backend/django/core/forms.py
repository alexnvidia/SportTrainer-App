from django import forms
from .models import Trainer, Client, Session, Rating, Message
from django.contrib.auth.models import User


# Trainer Form
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['user','bio','specialization', 'phone', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone

# Client Form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user','bio','phone','trainer', 'profile_picture']
    
    def clean_trainer(self):
        trainer = self.cleaned_data.get('trainer')
        if not trainer:
            raise forms.ValidationError("A trainer must be assigned.")
        return trainer
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone

# Session Form
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['trainer', 'client', 'date', 'attended', 'cancelled', 'notes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('attended') and cleaned_data.get('cancelled'):
            raise forms.ValidationError("A session cannot be both attended and cancelled.")
        return cleaned_data

# Rating Form
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['session', 'rating']
    
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

# Message Form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender','receiver', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("Message must be at least 5 characters long.")
        return content


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['bio', 'specialization', 'phone']

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = []  # No necesitamos campos adicionales en este formulario
