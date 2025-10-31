from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Count
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        university = self.get_object()
        university_courses = UniversityCourse.objects.filter(university=university)

        course_title = request.query_params.get('title', None)
        semester = request.query_params.get('semester', None)

        if course_title:
            university_courses = university_courses.filter(course__title__icontains=course_title)
        if semester:
            university_courses = university_courses.filter(semester__icontains=semester)

        university_courses = university_courses.order_by('duration_weeks')

        serializer = UniversityCourseSerializer(university_courses, many=True)
        return Response(serializer.json())

    @action(detail=True, methods=['get'])
    def course_stats(self, request, pk=None):
        university = self.get_object()
        stats = UniversityCourse.objects.filter(university=university).aggregate(
            total_courses=Count('id'),
            average_duration=Avg('duration_weeks')
        )

        return Response({
            "total_courses": stats['total_courses'],
            "average_duration": round(stats['average_duration'] or 0, 1)
        })


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class UniversityCourseViewSet(viewsets.ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['university', 'course', 'semester']

