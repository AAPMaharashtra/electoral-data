from django.db import models

# Create your models here.
class LokSabhaSeat(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class AssemblyConstituency(models.Model):
	lok_sabha_seat = models.ForeignKey(LokSabhaSeat)
	name = models.CharField(max_length=100)
	constituency_no = models.CharField('constituency number',max_length=10,primary_key=True)
	def __unicode__(self):
		return self.name + ', ' + self.constituency_no

class PollingStation(models.Model):
	name = models.CharField(max_length=100)
	constituency = models.ForeignKey(AssemblyConstituency)
	def __unicode__(self):
		return self.name

class Society(models.Model):
	society_no 	= models.CharField('society number',max_length=50, primary_key=True)
	part_no = models.CharField('assembly part number',max_length=10,default='')
	address = models.CharField(max_length=200)
	pincode = models.IntegerField(default=0)
	polling_station = models.ForeignKey(PollingStation)
	male_count = models.IntegerField(default=0)
	female_count = models.IntegerField(default=0)
	total_count = models.IntegerField(default=0)
	def __unicode__(self):
		return self.society_no + ', ' + self.address

class Citizen(models.Model):
	society = models.ForeignKey(Society)
	voter_id = models.CharField(max_length=100,default='')
	name = models.CharField(max_length=100)
	parent_name = models.CharField(max_length=100)
	t_flag = models.CharField(max_length=100)
	age = models.IntegerField(default=0)
	SEX_CHOICES = (('male','Male'),('female','Female'))
	sex = models.CharField(max_length=10,choices=SEX_CHOICES,default='male')

	INTEREST_CHOICES = (
		('for','For'),
		('against','Against'),
		('neutral','Neutral'),
	)
	interest = models.CharField(max_length=10,choices=INTEREST_CHOICES,default='neutral')

	PHOTO_CHOICES = (
		('y','Yes'),
		('n','No')
	)
	photo_available = models.CharField(max_length=2,choices=PHOTO_CHOICES,default='n')

	PHOTO_CHOICES = (
		('y','Yes'),
		('n','No')
	)
	photo_available = models.CharField(max_length=2,choices=PHOTO_CHOICES,default='n')
	def __unicode__(self):
		return self.name + ', ' + self.address









