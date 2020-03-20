from django.db import models
from slugify import slugify
class Companies(models.Model):
    Company_name=models.CharField(max_length=255)
    about_company=models.TextField()
    job_description=models.TextField()
    role=models.CharField(max_length=255)
    job_requirement=models.TextField()
    mandatory_skills=models.TextField()
    stipend=models.IntegerField()
    Company_url=models.URLField()
    Company_age=models.IntegerField()
    loctaion=models.TextField()
    perks=models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    logo=models.ImageField(upload_to='if/images')

    def __str__(self):
        return self.Company_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Company_name)
        super(Companies, self).save(*args, **kwargs)
