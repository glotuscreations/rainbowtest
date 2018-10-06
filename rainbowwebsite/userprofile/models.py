from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator




# Create your models here.

class UserProfiles(models.Model):

    LOOKING_CHOICES = (('gay man looking for another gay man', 'gay man looking for another gay man'),
              ('bisexual man looking for men and women', 'bisexual man looking for men and women'),
              ('gay man looking for a lesbian wife', 'gay man looking for a lesbian wife'),
              ('lesbian woman looking for another lesbian woman', 'lesbian woman looking for another lesbian woman'),
              ('bisexual woman looking for both men and women', 'bisexual woman looking for both men and women'),
              ('lesbian woman looking for a gay husband', 'lesbian woman looking for a gay husband'),
              ('trans/intersex looking for females', 'trans/intersex looking for females'),
              ('trans/intersex looking for males', 'trans/intersex looking for males'),
              ('male looking for trans/intersex', 'male looking for trans/intersex'),
              ('female looking for trans/intersex', 'female looking for trans/intersex'),
              ('Looking for anyone for friendship', 'Looking for anyone for friendship'),
              ('Looking to co-parent', 'Looking to co-parent'),
              )

    ETHNIC_CHOICES = (
        ('Indian', 'Indian'),
        ('Pakistani', 'Pakistani'),
        ('Bangladeshi', 'Bangladeshi'),
        ('Sri Lankan', 'Sri Lankan'),
        ('Arab', 'Arab'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Asian', 'Asian'),
        ('other', 'other'))


    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
        ('Intersex', 'Intersex'),
        ('Non-Binary', 'Non-Binary'),
        ('Rather not say', 'Rather not say'))




    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    age= models.IntegerField(null=True, blank=True, validators=[MinValueValidator(18), MaxValueValidator(110)])
    Nationality= models.CharField(max_length=100, null=True, blank=True, verbose_name = 'Ethnicity:', choices = ETHNIC_CHOICES)
    image= models.ImageField(upload_to = 'pic_folder/', null=True, blank=False, verbose_name="your profile photo (required):")
    height= models.IntegerField(blank=True, null=True, verbose_name = "your height in cms:")
    weight= models.IntegerField(blank=True, null=True, verbose_name = 'Your weight in kgs:')
    description= models.TextField(max_length=500, verbose_name = 'Introduce yourself:')
    lookingfor= models.TextField(max_length=500, verbose_name= 'Your ideal soulmate:')
    preference = models.CharField(max_length=300, choices=LOOKING_CHOICES, verbose_name= "Preference:", null=True)
    Country = CountryField()
    City = models.CharField(verbose_name= 'city', max_length=120, null=True, blank = True)
    hobbies= models.CharField(max_length=200, null=True, blank=True)
    profession= models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, default=datetime.now)



    def __str__(self):
        return str(self.user)

    def summary(self):
        return self.description[:150]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfiles, self).save(*args, **kwargs)
