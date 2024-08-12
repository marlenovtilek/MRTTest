from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from apps.main.models import AnalysisResult, AnalysisResultImage

# Register your models here.


class AnalysisResultImageInline(admin.TabularInline):
    model = AnalysisResultImage
    extra = 0

class CustomResultAdmin(admin.ModelAdmin):
    inlines = [AnalysisResultImageInline]

    
    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     user = request.user
    #     qs = super().get_queryset(request)
    #     qs = qs.filter(doctor=user)
    #     return qs

admin.site.register(AnalysisResult, CustomResultAdmin)
