from django.urls import path, include

from rest_framework import routers

from .views import (TeacherView, CommentView, CoursesView, LessonView, EmailMessage, LessonLikeView,
                    LessonCreateLikeView)

router = routers.DefaultRouter()
router.register('teacher', TeacherView)
router.register('comment', CommentView)
router.register('courses', CoursesView)
router.register('lesson', LessonView)


api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(api_urlpatterns)),
    path('email', EmailMessage.as_view()),
    path('api/v1/lesson/<int:pk>/like/', LessonLikeView.as_view()),
    path('api/v1/lesson/like/create/', LessonCreateLikeView.as_view())
]
