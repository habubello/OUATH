from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ecourses.views import blog_list,teacher_list,course_list,blog_detail,teacher_detail,about,course_details
app_name = 'ecourses'

urlpatterns = [

    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('courses/', course_list, name='course_list'),
    path('about/', about, name='about'),
    path('courses/<int:course_id>/', course_details, name='course_details'),

    path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
