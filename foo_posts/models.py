from django.db import models

# Create your models here.
class FooPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    author = models.ForeignKey(to='user_management.UserProfile', on_delete=models.CASCADE)
    likes = models.ManyToManyField(to='user_management.UserProfile', related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(to='user_management.UserProfile', related_name='post_dislikes', blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def like_post(self, user):
        self.likes.add(user)

    def dislike_post(self, user):
        self.dislikes.add(user)

    def unlike_post(self, user):
        self.likes.remove(user)

    def undislike_post(self, user):
        self.dislikes.remove(user)

    def get_likes_count(self):
        return self.likes.count()

    def get_dislikes_count(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title
