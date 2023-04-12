from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
##one for auction listings, one for bids, and one for comments made on auction listings.
## User model

class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


 ## Model for auction listings
class Listing(models.Model):

    title = models.CharField(max_length=64)

    description = models.TextField()

    price = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    img = models.URLField(blank=True, null=True)

    inactive = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.id}. {self.title} Initial price is {self.price}"


## Model one for bids

class Bid (models.Model):
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bids',null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids', null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.bidder.username} - {self.amount}'

##  make_bid = models.IntegerField()
class Soled (models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "buyer", default=None)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "seller", default=None)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = "item", default=None)
    soled_price = models.ForeignKey(Bid, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

def __str__(self):
    return f"{self.id}. {self.buyer} buy {self.listing} for {self.price} ,seller:{self.seller}"



## Model for comments made on auction listings
class Comment(models.Model):
    content = models.CharField(max_length=512)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commenter.username} - {self.content}"
    
class Watchlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = "watchlist", default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Listing {self.listing} in watchlist user: {self.user.username}"
    