from django.db import models

# Create your models here.

class Owner(models.Model):
	FName = models.CharField(max_length=200)
	LName = models.CharField(max_length=200)
  ownerType = models.CharField(max_length=200)
	def __unicode__(self):
		return unicode(FName + " " + LName)

class Item(models.Model):
	Item_Number = models.IntegerField(primary_key=True)
	Category = models.CharField(max_length=200)
	Make = models.CharField(max_length=200)
	Model = models.CharField(max_length=200)
	def __unicode__(self):
		return unicode(str(self.Item_Number))

