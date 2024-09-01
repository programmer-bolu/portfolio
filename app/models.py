from django.db import models

# Create your models here.

class work(models.Model):
    choice = (
        ('frontend', 'frontend'),
        ('backend', 'backend'),
        ('fullstack', 'fullstack'),
    )
    work_name = models.CharField(max_length=60)
    work_type = models.TextField(max_length=255, choices=choice)
    
    
    
class addUserData(models.Model):
    full_name = models.CharField(max_length=60)
    who_you_are_description = models.TextField()
    your_experience_1 = models.CharField(max_length=20)
    your_experience_2 = models.CharField(max_length=20)
    your_experience_3 = models.CharField(max_length=20)
    your_frontend_framework_1 = models.CharField(max_length=20)
    your_frontend_framework_2 = models.CharField(max_length=20)
    your_backend_framework_1 = models.CharField(max_length=20)
    your_backend_framework_2 = models.CharField(max_length=20)
    your_fullstack_framework_1 = models.CharField(max_length=20)
    your_fullstack_framework_2 = models.CharField(max_length=20)
    your_specialty = models.TextField()
    your_previous_work = models.ForeignKey(work, on_delete=models.CASCADE, null=True, blank=True)
    testimony = models.TextField()
    testimony_sharer = models.CharField(max_length=255)
    testimony_rating = models.IntegerField()
    testimony_sharer_position = models.CharField(max_length=255)
    frequently_asked_question_1 = models.TextField()
    frequently_asked_question_answer_1 = models.TextField()
    frequently_asked_question_2 = models.TextField()
    frequently_asked_question_answer_2 = models.TextField()
    frequently_asked_question_3 = models.TextField()
    frequently_asked_question_answer_3 = models.TextField()
    your_address = models.CharField(max_length=255)
    your_contact = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255)
    
