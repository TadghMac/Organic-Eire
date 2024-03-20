from django.contrib import admin
from .models import Links
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Links)
class LinksAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

