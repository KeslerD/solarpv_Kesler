from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Certificate)
admin.site.register(Product)
admin.site.register(TestStandard)
admin.site.register(PerformanceData)
admin.site.register(Service)
admin.site.register(TestSequence)