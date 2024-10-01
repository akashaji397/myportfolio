from django.contrib import admin
from .models import About, Education, RecentWork,Experience,CV

# Register your models here.
admin.site.register(About)
admin.site.register(Education)
admin.site.register(RecentWork)
admin.site.register(Experience)
admin.site.register(CV)