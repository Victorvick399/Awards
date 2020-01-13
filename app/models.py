from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    '''
    This is the model belonging to the post.
    '''
    title = models.CharField(max_length=20)
    photo = ImageField(blank=True, manual_crop='')
    description = models.TextField()
    link = models.CharField(max_length=1000)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_post(self):
        '''
        Function that saves projects posted.
        '''
        self.save()

    def delete_post(self):
        '''
        Function that that deletes a project.
        '''
        self.delete()

    @classmethod        
    def get_all_posts(cls):
        '''
        Function that gets all posts.
        '''
        posts=cls.objects.order_by('-id')
        return posts

    @classmethod
    def get_single_post(cls,post_id):
        '''
        Function that gets a single post.
        '''
        post=cls.objects.get(id=post_id)
        return post

    @classmethod
    def get_user_posts(cls, user_id):
        '''
        function that gets a user's posts
        '''
        posts=cls.objects.filter(posted_by__id__contains=user_id).order_by('-id')
        return posts

    @classmethod
    def winner_project(cls):
        post=cls.objects.latest()
        return post

    @classmethod
    def search_project(cls,post_name):
        posts=cls.objects.filter(title__icontains=post_name)
        return posts


class Profile(models.Model):
    '''
    This is the user's profile where their details will be.
    '''
    image = ImageField(blank=True, manual_crop='')
    bio = models.TextField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.IntegerField()

    def __str__(self):
        return self.bio
