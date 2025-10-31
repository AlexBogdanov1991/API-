from rest_framework import serializers
from courses.models import University, Course, UniversityCourse

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UniversityCourseSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_description = serializers.CharField(source='course.description', read_only=True)

    class Meta:
        model = UniversityCourse
        fields = ['id', 'university', 'course', 'university_name', 'course_title',
                 'course_description', 'semester', 'duration_weeks']

