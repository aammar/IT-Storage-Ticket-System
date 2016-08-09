from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
  user = models.ForeignKey(User)
  FName = models.CharField(max_length=200)
  LName = models.CharField(max_length=200)
  ownerType = models.CharField(max_length=200)
  imgURL = models.CharField(max_length=128, blank=True)
  def __unicode__(self):
    return unicode(self.FName + " " + self.LName)

class Item(models.Model):
  itemID = models.IntegerField()
  itemNumber = models.IntegerField(primary_key=True)
  class Meta:
    unique_together = ('itemID', 'itemNumber',)

  category = models.CharField(max_length=200)
  make = models.CharField(max_length=200)
  model = models.CharField(max_length=200)
  description = models.CharField(max_length=400, blank=True)
  imgURL = models.CharField(max_length=128, blank=True)
  owner = models.ForeignKey(Owner, null=True, blank=True)

  def __unicode__(self):
    return unicode(self.make + " " + self.model)

class ItemRequest(models.Model):
  requester = models.ForeignKey(Owner)
  item = models.ForeignKey(Item)

  def __unicode__(self):
    return unicode(str(self.requester) + " requested " + str(self.item))
