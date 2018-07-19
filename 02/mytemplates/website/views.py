from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class ABoutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
