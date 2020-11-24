from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=50)

    '''def average_rating(self):
         all_ratings = map(lambda x: x.rating, self.review_set.all())
         return np.mean(all_ratings)'''

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.user.name + ' ' + self.wine.name)
