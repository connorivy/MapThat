from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from extract.models import Document
from extract.forms import DocumentForm

from .GenerateKML import KMLifyer
def list(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(type(request.FILES['docfile']))
            for document in request.FILES.getlist('docfile'):


                newdoc = Document(docfile = document)
                newdoc.save()
                print(newdoc.docfile.path)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': documents, 'form': form})
def clear_all(request):
    Document.objects.all().delete()
    documents = Document.objects.all()
    return HttpResponseRedirect(reverse('list'))
    
def build_kml(request):

    documents = Document.objects.all()
    print(documents)
    km = KMLifyer()
    for document in documents:
        print('./' + document.docfile.name)
        km.extract('./' + document.docfile.name)
    kml_string =  km.gen_kml()

    form = DocumentForm()

    response = HttpResponse( content=kml_string, content_type='plain/text')
    response['Content-Disposition'] = 'attachment; filename="images.kml"'

    return response

