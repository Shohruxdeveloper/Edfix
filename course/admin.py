from django.contrib import admin

from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """ Siz o'qituvchi modeli parametrlarini administrator panelida ko'rsatish orqali boshqarishingiz mumkin """
    list_display = ('id', 'full_name', 'experience', 'level',)
    list_display_links = ('id', 'full_name', 'experience', 'level',)
    list_filter = ('full_name', 'experience', 'level',)
    search_fields = ('full_name', 'experience', 'level',)
    ordering = ('pk',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """ Kurs modeli parametrlarini bu yerda administrator panelida ko‘rsatish orqali boshqarishingiz mumkin """
    list_display = ('id', 'title', 'teacher', 'price',)
    list_display_links = ('id', 'title', 'teacher', 'price',)
    list_filter = ('title', 'teacher', 'price',)
    search_fields = ('title', 'teacher', 'price',)
    ordering = ('pk',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """ Dars modeli parametrlarini bu yerda administrator panelida ko‘rsatish orqali boshqarishingiz mumkin """
    list_display = ('id', 'course', 'title')
    list_display_links = ('id', 'course', 'title')
    list_filter = ('course', 'title')
    search_fields = ('title', 'title')
    ordering = ('pk',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Siz sharh modeli parametrlarini bu yerda administrator panelida ko‘rsatish orqali boshqarishingiz mumkin """
    list_display = ('id', 'author', 'lesson',)
    list_display_links = ('id', 'author', 'lesson',)
    list_filter = ('author', 'lesson', )
    search_fields = ('author', 'lesson',)
    ordering = ('pk',)


@admin.register(LikeLesson)
class LikeLessonAdmin(admin.ModelAdmin):
    """ Siz like modeli parametrlarini administrator panelida ko'rsatish orqali boshqarishingiz mumkin """
    list_display = ('id', 'lesson', 'user', 'like_or_dislike',)
    list_display_links = ('id', 'lesson', 'user', 'like_or_dislike',)
    list_filter = ('lesson', 'user')
    search_fields = ('lesson', 'user')
    ordering = ('pk',)
