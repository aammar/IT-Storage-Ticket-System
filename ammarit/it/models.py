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
  itemID = models.IntegerField(primary_key=True, unique=True)

  itemNumber = models.IntegerField()
  category = models.CharField(max_length=200)
  make = models.CharField(max_length=200)
  model = models.CharField(max_length=200)
  description = models.CharField(max_length=400, blank=True)
  imgURL = models.CharField(max_length=128, blank=True)
  owner = models.ForeignKey(Owner, null=True, blank=True)
  ownership_desc = models.CharField(max_length=1000)
  ownership_time = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return unicode(self.make + " " + self.model)

  def sameAs(self, item):
    return self.itemNumber == item.itemNumber

class ItemRequest(models.Model):
  requester = models.ForeignKey(Owner)
  desc = models.CharField(max_length=1000)
  time = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return unicode(str(self.requester) + " requested items")

class RequestedItem(models.Model):
  request = models.ForeignKey(ItemRequest)
  itemNumber = models.IntegerField()

  def __unicode__(self):
    return unicode(str(self.itemNumber))

  def getitem(self):
    try:
      return Item.objects.filter(itemNumber=self.itemNumber)[0]
    except:
      return None

class Log(models.Model):
  logText = models.CharField(max_length=2000)
  subtext = models.CharField(max_length=10000)
  time = models.DateTimeField(auto_now_add=True)
  type = models.CharField(max_length=64)

  def __unicode__(self):
    return unicode("[" + str(self.time) + "]" + self.logText)
