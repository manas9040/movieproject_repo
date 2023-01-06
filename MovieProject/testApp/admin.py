from django.contrib import admin
from testApp.models import MovieInfo

# Register your models here.
class MovieInfoAdmin(admin.ModelAdmin):
    list_display=['moviename','releasedate','actor','actress','rating']
admin.site.register(MovieInfo,MovieInfoAdmin)
