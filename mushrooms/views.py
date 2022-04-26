from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from extract.models import Document
from extract.forms import DocumentForm
from .EmailSender import email
from .forms import MessageForm

image = ''

def SendEmail(request):
    import os 
    global image
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sub = form.cleaned_data['subject']
        email(address, sub, message, image)
        return HttpResponse('Thanks for using our service')
    else:
        src = request.path[6:] 
        image = os.path.abspath('../Release_1/' + src[10:])
        
        #Get image
        #Get Address
        #email(adress, image)

        msgForm = MessageForm()
        return render(request, 'email.html', {'image':src ,'form':msgForm})
