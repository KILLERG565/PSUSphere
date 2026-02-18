from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from studentorg.forms import ItemForm
from .models import Item, Organization
from django.views.generic.list import ListView
# Create your views here.

def home(request):
    items = Item.objects.all().order_by('id')  # Fetch all items
    paginator = Paginator(items, 5)  # Show 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect back to home
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

# Class-based view for Organization list
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"