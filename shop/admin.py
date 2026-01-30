from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "Course Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Course Admin Area"


class CourseAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('category', 'created_at')


class CoursesInLine(admin.TabularInline):
    model = models.Course
    extra = 1
    exclude = ('created_at',)


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['created_at', ], 'classes': ['collapse']}),
    ]
    inlines = [CoursesInLine]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
