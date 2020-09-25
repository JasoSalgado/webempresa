"""Contact views."""

# Django modules
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        # It will validate if all fields are correct
        if contact_form.is_valid():
            # It has to return the name or a empty chain
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Everything went well
            # Reverse works to redirect without passing raw data
            # We send the mail and redirect.
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['jasgotti98@gmail.com'],
                reply_to=[email]
            )
            
            try:
                email.send()
                # Everything went well
                return redirect(reverse('contact')+'?ok')
            except:
                # Something failed
                return redirect(reverse('contact')+'?fail')                     
        
    return render(request, 'contact/contact.html', {'form':contact_form})
