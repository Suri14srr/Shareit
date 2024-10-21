import uuid
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

def base_redirect(request):
    unique_id = uuid.uuid4()
    return redirect('unique_view', unique_id=unique_id)

def unique_view(request, unique_id):
    # Render the template from templates/unique_page.html
    return render(request, 'unique_page.html', {'unique_id': unique_id})