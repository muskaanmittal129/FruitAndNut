from django.shortcuts import render
from django.views import generic
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion, Faculty,Testimonial,\
    LabSection, ImportantFunctionary, Gallery, Event, EventImages, OrganizationChart


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
        self.context["event_info"] = RecentEvent.objects.filter(active=True)

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
    context ={}

    def get_lab(self):
        lab_info = LabSection.objects.all()
        self.context['lab_info'] = lab_info

    def get(self, *args, **kwargs):
        self.get_lab()
        return render(self.request,self.template_name, self.context)


class GalleryView(generic.ListView):
    template_name = 'core/gallery.html'

    def get(self, request, *args, **kwargs):
        return render(self.request,self.template_name)


class AlumniView(generic.ListView):
    template_name = 'core/testimonial.html'
    context = {}

    def get_testimonial(self):
        testimonial_info = Testimonial.objects.all()
        self.context['testimonial_info'] = testimonial_info

    def get(self, request, *args, **kwargs):
        self.get_testimonial()
        return render(self.request,self.template_name,self.context)


# class RecentEventView(generic.ListView):
#     template_name = 'core/recent_events.html'
#     context ={}
#
#     def get_event(self):
#         event_info = RecentEvent.objects.filter(active=True)
#         self.context['event_info'] = event_info
#
#     def get(self, request, *args, **kwargs):
#         self.get_event()
#         return render(self.request,self.template_name,self.context)

class ImportantFunctionaryView(generic.ListView):
    template_name = 'core/about/important_functionary.html'
    context = {}

    def get_imp_functionary(self):
        imp_functionary = ImportantFunctionary.objects.order_by('priority')
        self.context['imp_functionaries'] = imp_functionary

    def get(self, request, *args, **kwargs):
        self.get_imp_functionary()
        return render(self.request,self.template_name,self.context)


class OrganizationChartView(generic.ListView):
    template_name = 'core/about/organization_chart.html'
    context = {}

    def get_organization_chart(self):
        try:
            organization_chart = OrganizationChart.objects.all()[0]
        except:
            organization_chart = None
        self.context[' organization_chart'] =  organization_chart

    def get(self, request, *args, **kwargs):
        self.get_organization_chart()
        return render(self.request,self.template_name,self.context)
