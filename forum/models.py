from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


STATUS = ((0, "Posted"), (1, "Approved"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=300, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1500)
    difficulty_hard = models.BooleanField(default=False)
    difficulty_moderate = models.BooleanField(default=False)
    difficulty_easy = models.BooleanField(default=False)
    breed_big = models.BooleanField(default=False)
    breed_mid = models.BooleanField(default=False)
    breed_sml = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
                                User,
                                related_name='blogpost_like',
                                blank=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    about_me = models.TextField(max_length=300, blank=True)
    about_dog = models.TextField(max_length=300, blank=True)
    favorite_location = models.TextField(max_length=100, blank=True)

    # Automatically create user profile upon user registration
    # Code taken from ordinarycoders.com
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
