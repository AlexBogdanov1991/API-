from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='university_courses')
    semester = models.CharField(max_length=50)
    duration_weeks = models.PositiveIntegerField()

    class Meta:
        unique_together = ['university', 'course', 'semester']

    def __str__(self):
        return f"{self.course.title} at {self.university.name} ({self.semester})"
