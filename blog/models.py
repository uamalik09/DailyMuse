from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    text=models.TextField(validators=[MinLengthValidator(30)])
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True)
    excerpt=models.CharField(max_length=100,null=False)


    


    def __str__(self):
        return f'{self.user.username} - {self.title}'
    
@receiver(pre_save, sender=Blog)
def populate_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        instance.slug = base_slug
        counter = 1
        while Blog.objects.filter(slug=instance.slug).exists():
            instance.slug = f'{base_slug}-{counter}'
            counter += 1