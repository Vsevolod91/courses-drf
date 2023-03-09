from rest_framework.routers import DefaultRouter
from courses.views import *
from django.urls import path

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson-create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson-<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson-update-<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson-delete-<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete')
              ] + router.urls

