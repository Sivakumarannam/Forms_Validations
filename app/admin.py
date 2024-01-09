from django.contrib import admin
from app.models import *
# Register your models here.
class customize_student(admin.ModelAdmin):
    list_display=['Sname','Email']
    list_display_links=['Email']
    list_editable=['Sname']
    list_filter=['Sname','Sdateofbirth','Squalification_10','Squalification_12','Squalification_Degree']
    list_per_page=1



admin.site.register(Student_model,customize_student)
