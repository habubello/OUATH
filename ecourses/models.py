from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=255)
    describe = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    field = models.CharField(max_length=255)
    img = models.ImageField(upload_to='teacher_images/', blank=True, null=True)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)  # Рейтинг (0.0 - 5.0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video = models.FileField(upload_to='course_videos/', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name