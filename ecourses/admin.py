from django.contrib import admin

from ecourses.models import Course,Teacher,Blog,Category

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Blog)
admin.site.register(Category)

# Register your models here.
