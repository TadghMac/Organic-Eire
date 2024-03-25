from django.contrib import admin
from .models import Links
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Links)
class LinksAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

