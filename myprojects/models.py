from phone_field import PhoneField
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from ckeditor.fields import RichTextField

# each instance is a project displayed in a new page
class Project(models.Model):
    featured = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    feature_list_visible = models.BooleanField(default=True)
    code_sample_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    project_type = models.CharField(default="Web Application", max_length=50)
    description = RichTextField()
    project_link = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    front_image = models.ImageField(upload_to='proj_frontimages',verbose_name="Thumbnail")
    large_image = models.ImageField(upload_to='proj_frontimages', blank=True)
    technical_details = models.TextField(verbose_name="Technical Details (split by /)", null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == "":
            self.slug = f"{self.title}".replace(' ','').lower()
        super(Project, self).save(*args, **kwargs)

# each instance is a daily update stored under devlopment log
class ProjectUpdate(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    details = models.TextField()
    link = models.URLField(null=True, blank=True)
    first_image = models.ImageField(upload_to='update_images',blank=True, verbose_name="Image 1")
    second_image = models.ImageField(upload_to='update_images', blank=True, verbose_name="Image 2")
    third_image = models.ImageField(upload_to='update_images', blank=True, verbose_name="Image 3")

    #relationship to Project model
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return f"Update for {self.project.title} on {self.date_posted.date()}"

class ProjectFeatureList(models.Model):
    feature_title = models.CharField(max_length=50)
    feature_detail = models.TextField()
    feature_image = models.ImageField(upload_to='feature_images',blank=True)

    # relationship to Project model
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Feature for {self.project.title}"

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

class MyInformation(models.Model):
    name = models.CharField(max_length=20)
    about_page_description = RichTextField()
    phone_number = PhoneField()
    email = models.EmailField()
    current_role = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    tech_stack = models.TextField(verbose_name="Stack (split by /)", null=True)
    resume_link = models.URLField(null=True, blank=True)
    my_photo = models.ImageField(upload_to='profile', blank=True)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return "My Information"

class CodeSample(models.Model):
    sample_name = models.CharField(max_length=50)
    sample_text = models.TextField()
    github_gist_id = models.CharField(max_length=100)
    feature_image = models.ImageField(null=True, upload_to='code sample')
    # relationship to Project model
    project = models.ForeignKey(Project, on_delete=models.CASCADE)