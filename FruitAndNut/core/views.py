from django.shortcuts import render
from django.views import generic
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion, Faculty


class Home(generic.DetailView):
    template_name = 'core/home.html'
    context = {}

    def get_footer_about(self):
        self.context["footer_about"] = FooterAbout.objects.all().first()

    def get_footer_contact(self):
        contact_list = [contact.text_data for contact in FooterContact.objects.all()]
        self.context["footer_contact"] = contact_list

    def get_footer_related_links(self):
        self.context["footer_related_links"] = FooterRelatedLinks.objects.order_by('priority')

    def get_recent_event(self):
        self.context["recent_events"] = RecentEvent.objects.filter(active=True)

    def get_landing_porting(self):
        self.context["landing_portion"] = LandingPortion.objects.filter(active=True)

    def get(self, *args, **kwargs):
        self.get_footer_about()
        self.get_footer_contact()
        self.get_footer_related_links()
        self.get_recent_event()
        self.get_landing_porting()
        return render(self.request, self.template_name, self.context)


class FacultyView(generic.ListView):
    template_name = 'core/faculty.htm'
    context ={}

    def get_faculty(self):
        faculty_info = Faculty.objects.all()
        self.context['faculty_info'] = faculty_info

    def get(self, request, *args, **kwargs):
        self.get_faculty()
        return render(self.request,self.template_name,self.context)



class LabView(generic.ListView):
    template_name = 'core/Labs.htm'

    def get(self, *args, **kwargs):
        return render(self.request,self.template_name)
