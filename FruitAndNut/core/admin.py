from django.contrib import admin
from .models import RecentEvent, RecentEventSlider, FooterAbout, FooterContact, FooterRelatedLinks


admin.site.register(RecentEventSlider)
admin.site.register(RecentEvent)
admin.site.register(FooterRelatedLinks)
admin.site.register(FooterContact)
admin.site.register(FooterAbout)
# admin.site.register()



