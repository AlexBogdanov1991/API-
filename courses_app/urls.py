from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import UniversityViewSet, CourseViewSet, UniversityCourseViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'university-courses', UniversityCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]