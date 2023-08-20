from django.contrib import admin

from . import models

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(models.Movie, MovieAdmin)


admin.site.register(models.Ticket)

admin.site.register(models.Place)
admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Review)
