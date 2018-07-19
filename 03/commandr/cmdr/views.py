from django.views.generic import ListView

# Create your views here.

from .models import Cmdr

class HomePageView(ListView):
    model = Cmdr
    template_name = 'home.html'
