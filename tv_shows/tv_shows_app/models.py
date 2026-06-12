from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData, show_id=None):
        errors = {}
        if len(postData.get('title', '').strip()) < 1:
            errors['title'] = 'Title is required and must not be empty.'
        if len(postData.get('network', '').strip()) < 1:
            errors['network'] = 'Network is required and must not be empty.'
        
        release_date_str = postData.get('release_date', '').strip()
        if len(release_date_str) < 1:
            errors['release_date'] = 'Release Date is required and must not be empty.'
        else:
            try:
                release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
                if release_date >= datetime.today().date():
                    errors['release_date'] = 'Release Date must be strictly in the past.'
            except ValueError:
                errors['release_date'] = 'Invalid date format.'

        description = postData.get('description', '').strip()
        if description and len(description) < 10:
            errors['description'] = 'Description must be at least 10 characters long if provided.'
        
        title = postData.get('title', '').strip()
        if title:
            existing_shows = Show.objects.filter(title=title)
            if show_id:
                existing_shows = existing_shows.exclude(id=show_id)
            if existing_shows.exists():
                errors['title_unique'] = 'A show with this title already exists.'
                
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
