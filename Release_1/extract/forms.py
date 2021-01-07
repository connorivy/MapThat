from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Select a file',
        help_text='max. 42 MB',
    )
