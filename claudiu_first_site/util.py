
### Source: https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/#:~:text=What%20is%20SlugField%20in%20Django,with%20primary%20key%20id%3D%202.
import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
 
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug = slug).exists()
     
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug[:max_length-5], randstr = random_string_generator(size = 4))
             
        return unique_slug_generator(instance, new_slug = new_slug)
    return slug