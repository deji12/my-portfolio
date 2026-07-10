from django.shortcuts import render, redirect
from .models import Project, Recognition,ContactMessage, Resume
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.urls import reverse

def home(request):

    projects = Project.objects.filter(is_active=True).order_by('order_number')
    recognitions = Recognition.objects.filter(is_active=True)
    resume = Resume.objects.last()

    context = {
        'projects': projects,
        'recognitions': recognitions,
        'resume': resume
    }

    return render(request, 'index.html', context)

def process_contact_message(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_message = ContactMessage.objects.create(
            name = name,
            email = email,
            subject = subject,
            body = message
        )

        message = f'Hello Ayo, you have received a new contact portfolio message. Details below:\n\nName: {name}\nEmail: {email}\nMessage: {message}\nTimestamp: {contact_message.timestamp}'
        
        email_message = EmailMessage(
            'New Contact Message',
            message,
            settings.EMAIL_HOST_USER,
            [settings.ADMIN_RECIPIENT_EMAIL]
        )

        email_message.fail_silently = True
        email_message.send()

        messages.success(request, 'Message sent successfully')
        return redirect(f"{reverse('home')}#contact")