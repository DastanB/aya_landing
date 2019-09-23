from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm

def get_application(request):
    if request.method == 'POST':
    
        form = ContactForm(request.POST or None)
        if form.is_valid():
            fio = form.cleaned_data['fio']
            phone_number = form.cleaned_data['phone_number']
            
            from_email = 'aya.edu.kz@gmail.com'
            to_email = ['appazdias8@gmail.com', 'c.tolegen@seznam.cz', 'aya.edu.kz@gmail.com']
            
            send_mail(fio, phone_number, from_email, to_email)
            return HttpResponseRedirect('/thanks')

    form = ContactForm()    
    return render(request, 'thanks.html', {'form': form})