from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    """O'qituvchilar uchun yozilgan model"""

    LEVEL_CHOICES = [
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    photo = models.ImageField(upload_to='teachers/photo')
    full_name = models.CharField(max_length=100, verbose_name='Full Name', blank=True)
    experience = models.IntegerField(help_text="Work experience", verbose_name='Work experience')
    level = models.CharField(max_length=6, choices=LEVEL_CHOICES, verbose_name='Level')

    def __str__(self):
        return self.full_name


class Course(models.Model):
    """ Kurslar uchun yozilgan model"""

    title = models.CharField(max_length=255, verbose_name='Course')
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, related_name='teacher_courses', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(verbose_name='price', default=None)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """ Darslar uchun yozilgan model """

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='title', blank=True)
    content = models.TextField()
    video = models.FileField(upload_to='media/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'wmv'])])
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    """ Izoohlar uchun yozilgan model"""

    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE, verbose_name='Lesson comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.lesson.title}'


class LikeLesson(models.Model):
    """ Like lar uchun yozilgan model """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like_or_dislike = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.lesson.title}'


