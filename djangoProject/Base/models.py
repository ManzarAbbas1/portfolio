from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')
    designation = models.CharField(max_length=100)
    title_line = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.degree} - {self.institution}'

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skill_images/')

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.job_title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(default='https://example.com')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(default='')

    def __str__(self):
        return self.conatct_info



