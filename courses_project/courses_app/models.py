from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData.get('name', '')) <= 5:
            errors['name'] = "Course name should be more than 5 characters."
        if len(postData.get('desc', '')) <= 15:
            errors['desc'] = "Description should be more than 15 characters."
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
