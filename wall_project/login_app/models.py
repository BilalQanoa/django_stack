from django.db import models
from datetime import datetime, date
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        
        # First Name Validation
        if len(postData.get('first_name', '')) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        elif not postData.get('first_name', '').isalpha():
            errors['first_name_alpha'] = "First name must contain letters only."
            
        # Last Name Validation
        if len(postData.get('last_name', '')) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."
        elif not postData.get('last_name', '').isalpha():
            errors['last_name_alpha'] = "Last name must contain letters only."
            
        # Email Validation
        email = postData.get('email', '')
        if len(email) == 0:
            errors['email_req'] = "Email is required."
        elif not EMAIL_REGEX.match(email):
            errors['email_format'] = "Invalid email address format."
        elif self.filter(email=email).exists():
            errors['email_unique'] = "Email address is already in use."
            
        # Password Validation
        password = postData.get('password', '')
        confirm_password = postData.get('confirm_password', '')
        if len(password) < 8:
            errors['password_len'] = "Password must be at least 8 characters."
        if password != confirm_password:
            errors['password_match'] = "Passwords do not match."
            
        # Birthday Validation
        birthday_str = postData.get('birthday', '')
        if not birthday_str:
            errors['birthday_req'] = "Birthday is required."
        else:
            try:
                birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
                today = date.today()
                
                # Check if strictly in the past
                if birthday >= today:
                    errors['birthday_past'] = "Birthday must be in the past."
                else:
                    # SENSEI BONUS: COPPA compliance (at least 13 years old)
                    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                    if age < 13:
                        errors['birthday_age'] = "You must be at least 13 years old to register."
            except ValueError:
                errors['birthday_format'] = "Invalid birthday format."
                
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData.get('email', '')) == 0:
            errors['email_req'] = "Email is required."
        if len(postData.get('password', '')) == 0:
            errors['password_req'] = "Password is required."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
