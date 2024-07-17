from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail


from .serializers import (TeacherSerializers, CommentSerializers, CourseSerializers, LessonSerializers,
                          LikeSerializer, MailSerializers)
from .models import Teacher, Comment, Course, Lesson, LikeLesson
from .permissions import CustomPermission, CoursePermission

from rest_framework import viewsets, filters
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class TeacherView(viewsets.ModelViewSet):
    """ O'qituvchilar uchun yozilgan view """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [CustomPermission]


class CommentView(viewsets.ModelViewSet):
    """ Izohlar uchun yozilgan view """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [CustomPermission]


class CoursesView(viewsets.ModelViewSet):
    """ Kurslar uchun yozilgan view """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [CoursePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class LessonView(viewsets.ModelViewSet):
    """ Dasrlar uchun yozilgan view """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [CoursePermission]


class EmailMessage(APIView):
    """ E-mail yuborish uchun yozilgan view """
    permission_classes = [CoursePermission]

    def post(self, request: Request):
        serializer = MailSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        users_email = []
        for user in users:
            users_email.append(user.email)
        users_email.append('shohruhabdurahmonov800@gmail.com')

        # "Edfix saytida siz uchun yangiliklar!!!",


        send_mail(
            serializer.validated_data.get('name'),
            serializer.validated_data.get('text'),
            settings.EMAIL_HOST_USER,
            users_email,
            fail_silently=False,
        )

        return Response({'success': "True"})


class LessonLikeView(APIView):
    def get(self, request, pk):
        likes = LikeLesson.objects.filter(like_or_dislike=True, lesson_id=pk).count()
        dis_likes = LikeLesson.objects.filter(like_or_dislike=False, lesson_id=pk).count()
        return Response({"likes": likes, "dis_likes": dis_likes})


class LessonCreateLikeView(APIView):

    def post(self, request):
        user_id = request.data.get('user')
        lesson_id = request.data.get('lesson')
        like_or_dislike_value = request.data.get('like_or_dislike')

        existing_like = LikeLesson.objects.filter(user_id=user_id, lesson_id=lesson_id).first()

        if existing_like:
            existing_like.delete()

            if existing_like.like_or_dislike == like_or_dislike_value:
                return Response({"message": "like deleted"})

        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_dislike = serializer.save()
        return Response(LikeSerializer(like_dislike).data)




