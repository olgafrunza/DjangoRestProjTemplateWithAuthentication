from django.db.models.signals import pre_save
from django.dispatch import receiver 
from .models import Blog
from django.template.defaultfilters import slugify
import uuid

def generate_random_code():
    code = str(uuid.uuid4())[:11].replace("-", "")
    return code


@receiver(pre_save, sender=Blog)
def add_slug(sender, instance, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title + " " + generate_random_code())
        if Blog.objects.filter(slug=slug).exists():
            slug = slugify(instance.title + " " + generate_random_code())
        instance.slug = slug
        