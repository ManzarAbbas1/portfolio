from django.contrib import admin
from .models import PersonalInfo, Education, Skill, Experience, Project, Contact

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contact)