from django.shortcuts import render
from .models import Blog, Teacher, Course, Category
from django.shortcuts import render, get_object_or_404

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'ecourses/blog.html', {'blogs': blogs})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'ecourses/teacher.html', {'teachers': teachers})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'ecourses/course.html', {'courses': courses})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'ecourses/teacher_detail.html', {'teacher': teacher})


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'ecourses/course_details.html', {'course': course})
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'ecourses/blog_detail.html', {'blog': blog})


def about(request):
    return render(request, 'ecourses/about.html')

