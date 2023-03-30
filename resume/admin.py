from django.contrib import admin
from .models import Skill,Achievement,Project,Contact
# Register your models here.
admin.site.register((Skill,Achievement,Project,Contact))