from django.shortcuts import redirect, render, get_object_or_404
from .models import UniqueURL

def base_redirect(request):
    unique_url = UniqueURL.objects.create()
    return redirect('unique_view', unique_id=unique_url.unique_id)

def unique_view(request, unique_id):
    unique_url = get_object_or_404(UniqueURL, unique_id=unique_id)
    base_url = f'{request.scheme}://{request.get_host()}/'
    if unique_url.is_expired:
        return render(request, 'expired.html', {'base_url': base_url})  
    return render(request, 'unique_page.html', {'unique_id': unique_id})