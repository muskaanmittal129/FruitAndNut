from django.shortcuts import render
from django.views import generic
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion, Faculty,Testimonial,\
    LabSection, ImportantFunctionary, Gallery, Event, EventImages, OrganizationChart, Principal


def get_footer_about():
    context = {}
    context["footer_about"] = FooterAbout.objects.all().first()
    return context


def get_footer_contact():
    context = {}
    contact_list = [contact.text_data for contact in FooterContact.objects.all()]
    context["footer_contact"] = contact_list
    return context


def get_footer_related_links():
    context = {}
    context["footer_related_links"] = FooterRelatedLinks.objects.order_by('priority')
    return context


def get_footer():
    context={}
    context.update(get_footer_about())
    context.update(get_footer_related_links())
    context.update(get_footer_contact())
    return context

class Home(generic.DetailView):
    template_name = 'core/home.html'
    context = {}
    context.update(get_footer())

    def get_recent_event(self):
        self.context["event_info"] = RecentEvent.objects.filter(active=True)

    def get_landing_porting(self):
        self.context["landing_portion"] = LandingPortion.objects.filter(active=True)

    def get(self, *args, **kwargs):
        self.get_recent_event()
        self.get_landing_porting()
        return render(self.request, self.template_name, self.context)


class FacultyView(generic.ListView):
    template_name = 'core/about/faculty.htm'
    context ={}
    context.update(get_footer())

    def get_faculty(self):
        faculty_info = Faculty.objects.all()
        self.context['faculty_info'] = faculty_info

    def get(self, request, *args, **kwargs):
        self.get_faculty()
        return render(self.request,self.template_name,self.context)


class LabView(generic.ListView):
    template_name = 'core/about/Labs.htm'
    context ={}
    context.update(get_footer())

    def get_lab(self):
        lab_info = LabSection.objects.all()
        self.context['lab_info'] = lab_info

    def get(self, *args, **kwargs):
        self.get_lab()
        return render(self.request,self.template_name, self.context)


class GalleryView(generic.ListView):
    template_name = 'core/about/gallery.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request,self.template_name)


class AlumniView(generic.ListView):
    template_name = 'core/testimonial.html'
    context = {}
    context.update(get_footer())

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
    context.update(get_footer())

    def get_imp_functionary(self):
        imp_functionary = ImportantFunctionary.objects.order_by('priority')
        self.context['imp_functionaries'] = imp_functionary

    def get(self, request, *args, **kwargs):
        self.get_imp_functionary()
        return render(self.request,self.template_name,self.context)


class OrganizationChartView(generic.ListView):
    template_name = 'core/about/organization_chart.html'
    context = {}
    context.update(get_footer())

    def get_organization_chart(self):
        try:
            organization_chart = OrganizationChart.objects.all()[0]
        except:
            organization_chart = None
        self.context[' organization_chart'] =  organization_chart

    def get(self, request, *args, **kwargs):
        self.get_organization_chart()
        return render(self.request,self.template_name,self.context)


class PrincipalView(generic.ListView):
    template_name = 'core/about/principal.html'
    context={}
    context.update(get_footer())

    def get_principal(self):
        try:
            principal = Principal.objects.all()[0]
        except:
            principal = None
        self.context['principal'] = principal

    def get(self, request, *args, **kwargs):
        self.get_principal()
        return render(self.request, self.template_name, self.context)


class VisionMissionView(generic.ListView):
    template_name = 'core/about/vision_and_mission.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)
