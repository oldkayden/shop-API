from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.dispatch import receiver

class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Category)
def category_slug_save(sender, instance, *args, **kwargs):
    print('******************')
    print('SIGNAL IS WORKED!')
    print('******************')
    if not instance.slug:
        instance.slug = slugify(instance.name)





# http://localhost:8000/api/categories/laptops/products/
# http://localhost:8000/api/categories/smatphones/products/

