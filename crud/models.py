from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Job(models.Model):
    title =models.CharField(max_length=20)
    descriptions=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)
    required_skills=models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    min_education=models.CharField(max_length=50)
    min_experience=models.CharField(max_length=50)
    age_requirements=models.CharField(max_length=50)
    gender =models.CharField(max_length=2,default='M')
    closing_date=models.DateField()
    status=models.CharField(max_length=2)
    salary=models.PositiveIntegerField()
    additional_benefits=models.CharField(max_length=50)
    document=models.FileField
   

    def __str__(self):
        return self.title + " " + self.descriptions
		
		
class Jobs(models.Model):
    title =models.CharField(max_length=20)
    descriptions=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)
    required_skills=models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    min_education=models.CharField(max_length=50)
    min_experience=models.CharField(max_length=50)
    age_requirements=models.CharField(max_length=50)
    gender =models.CharField(max_length=2,default='M')
    closing_date=models.DateField()
    status=models.CharField(max_length=2)
    salary=models.PositiveIntegerField()
    additional_benefits=models.CharField(max_length=50)
    document=models.FileField()
   

    def __str__(self):
        return self.title + " " + self.descriptions
		
class Jo(models.Model):
    title =models.CharField(max_length=20)
    descriptions=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)
    required_skills=models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    min_education=models.CharField(max_length=50)
    min_experience=models.CharField(max_length=50)
    age_requirements=models.CharField(max_length=50)
    gender =models.CharField(max_length=2,default='M')
    closing_date=models.DateField()
    status=models.CharField(max_length=2)
    salary=models.PositiveIntegerField()
    additional_benefits=models.CharField(max_length=50)
    document=models.FileField()
   

    def __str__(self):
        return self.title + " " + self.descriptions