from django.shortcuts import render
from django.views import generic
from .models import RecentEvent, RecentEventSlider, FooterAbout, FooterContact, FooterRelatedLinks


class Home(generic.DetailView):
    template_name = 'core/home.html'
    context = {}

    def get_footer_about(self):
        self.context["footer_about"] = FooterAbout.objects.all()

    def get_footer_contact(self):
        self.context["footer_contact"] = FooterContact.objects.all()

    def get_footer_related_links(self):
        self.context["footer_related_links"] = FooterRelatedLinks.objects.all()

    def get(self, *args, **kwargs):
        self.get_footer_about()
        self.get_footer_contact()
        self.get_footer_related_links()
        return render(self.request, self.template_name, self.context)
