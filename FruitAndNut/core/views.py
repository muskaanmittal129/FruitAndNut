from django.shortcuts import render
from django.views import generic
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks


class Home(generic.DetailView):
    template_name = 'core/home.html'
    context = {}

    def get_footer_about(self):
        self.context["footer_about"] = FooterAbout.objects.all()[0]

    def get_footer_contact(self):
        contact_list = [contact.text_data for contact in FooterContact.objects.all()]
        self.context["footer_contact"] = contact_list

    def get_footer_related_links(self):
        self.context["footer_related_links"] = FooterRelatedLinks.objects.all()

    def get_recent_event(self):
        self.context["recent_events"] = RecentEvent.objects.filter(active=True)

    def get(self, *args, **kwargs):
        self.get_footer_about()
        self.get_footer_contact()
        self.get_footer_related_links()
        self.get_recent_event()
        return render(self.request, self.template_name, self.context)
