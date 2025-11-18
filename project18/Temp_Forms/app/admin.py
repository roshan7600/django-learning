from django.contrib import admin

# Register your models here.
from app.models import *


# CUSTOMIZE THE ADMIN INTERFACE

class customViewAdmin(admin.ModelAdmin):
    list_display=['Topic_name','name','Url','pk']
    list_display_links=['name']
    search_fields=['Topic_name']
    list_filter=['Topic_name','url']
    list_editable=['Url']
    list_per_page=2


admin.site.register(Topic)
admin.site.register(Webpage,customViewAdmin)    
admin.site.register(AccessRecord)

# ADMIN HEADER AND TITLE CUSTOMIZATION
admin.site.site_header="DJANGO FORM ADMIN"
admin.site.site_title="django form goods"
admin.site.index_title="WELCOME TO DJANGO FORM ADMINISTRATION"