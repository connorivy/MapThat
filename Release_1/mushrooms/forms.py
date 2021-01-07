from django import forms

class MessageForm(forms.Form):
    name = forms.EmailField(label = 'E-mail', max_length = 100)
    subject = forms.CharField(label = 'Subject', max_length = 100)
    message = forms.CharField(label = 'Message', max_length = 256)
