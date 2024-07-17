from rest_framework import serializers
from .models import Teacher, Course, Comment, Lesson, LikeLesson


class TeacherSerializers(serializers.ModelSerializer):
    """ O'qituvchi modeli uchun yozilgan serializer """
    class Meta:
        model = Teacher
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    """" Izohlar modeli uchun yozilgan serializer """
    class Meta:
        model = Comment
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    """ Kurs modeli uchun yozilgan serializer """
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    """ Dars modeli uchun yozilgan serializer """
    class Meta:
        model = Lesson
        fields = '__all__'


class MailSerializers(serializers.Serializer):
    """ Email uchun yozilgan serializer """
    name = serializers.CharField(max_length=250)
    text = serializers.CharField()


class LikeSerializer(serializers.ModelSerializer):
    """Like lar modeli uchun yozilgan serializer"""
    class Meta:
        model = LikeLesson
        fields = '__all__'