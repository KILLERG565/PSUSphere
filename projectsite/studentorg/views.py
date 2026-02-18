from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item
# Create your views here.
def home(request):
    items = Item.objects.all()  # Fetch all items
    paginator = Paginator(items, 5)  # Show 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})
    