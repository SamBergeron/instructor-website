from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.forms import ModelForm

from markdown import markdown

from .lists import COUNTRIES, STATES

# DB models.
########################
## POST MODEL
########################
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    author = models.ForeignKey(User, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-created_at", "title"]
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ("blog:post_detail", (), {"slug": self.slug})

        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


########################
## RESORT MODEL
########################        
class Resort(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=4, choices=COUNTRIES)
    state = models.CharField(max_length=3, choices=STATES)
    
    class Meta:
        ordering = ["country", "state", "name"]
        
    def __unicode__(self):
        return self.name

        
########################
## PROFILE MODEL
########################    
class Profile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    username = models.ForeignKey(User, related_name="profile", unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    slug = models.SlugField(max_length=512, blank=True, default='')
    country = models.CharField(max_length=255, choices=COUNTRIES)
    resort = models.ForeignKey(Resort, related_name="user_profile")
    description = models.TextField()
    markdown_description = models.TextField('Body', help_text='Use markdown for publishing')
    contact_info = models.TextField()
    contact_phone = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255, unique=True)
    
    class Meta:
        ordering = ["lastname", "firstname"]
        
    def __unicode__(self):
        return self.firstname + self.lastname
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.firstname + self.lastname + self.resort)
        import markdown
        self.description = markdown.markdown(self.markdown_description)
        super(Profile, self).save(*args, **kwargs)
        
    
    