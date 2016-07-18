from django.db import models

# Create your models here.

class Employee(models.Model):
	FName = models.CharField(max_length=200)
	LName = models.CharField(max_length=200)
	ID = models.IntegerField(primary_key=True)
	def __unicode__(self):
		return unicode(self.ID)

class Storage(models.Model):
	Item_Number = models.IntegerField(primary_key=True)
	Quantity = models.IntegerField()
	Category = models.CharField(max_length=200)
	Make = models.CharField(max_length=200)
	Model = models.CharField(max_length=200)
	def __unicode__(self):
		return unicode(self.Item_Number)

class Room():





class Item_List(models.Model):
	ID_Tag = models.IntegerField(primary_key=True)
	Item_Number = models.ForeignKey('Storage', on_delete=models.CASCADE)
	def __unicode__(self):
		return unicode(self.ID_Tag)


class Employee_Item(models.Model):
	ID = models.ForeignKey('Employee', on_delete=models.CASCADE)
	ID_Tag = models.ForeignKey('Item_List', on_delete=models.CASCADE)
