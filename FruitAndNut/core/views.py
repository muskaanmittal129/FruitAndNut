from django.shortcuts import render
from django.views import generic


class Home(generic.DetailView):
    template_name = 'core/home.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
