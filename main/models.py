from django.db import models

class StudentRegisterationForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    branch = models.CharField(max_length=40)
    year = models.IntegerField()
    github_url = models.URLField()

    def save(self, *args, **kwargs):
        super(StudentRegisterationForm, self).save(*args, **kwargs)