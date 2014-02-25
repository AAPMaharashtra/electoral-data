from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255,default='')
	constituency = models.ForeignKey(AssemblyConstituency)
	processed = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

class Citizen(models.Model):
	polling_station = models.ForeignKey(PollingStation)
	part_no = models.IntegerField(blank=False)
	serial_no = models.IntegerField(blank=False)
	voter_id = models.CharField(max_length=100,default='')
	first_name = models.CharField(max_length=100,default='')
	last_name = models.CharField(max_length=100,default='')
	parent_name = models.CharField(max_length=100)
	house_no = models.CharField(max_length=100,default='')
	age = models.IntegerField(default=0)
	SEX_CHOICES = (('male','Male'),('female','Female'))
	sex = models.CharField(max_length=10,choices=SEX_CHOICES,default='male')

	INTEREST_CHOICES = (
		('aap','AAP'),
		('congress','Congress'),
		('ncp','NCP'),
		('bjp','BJP'),
		('shs','SHS'),
		('mns','MNS'),
		('rpi','RPI'),
		('other','Other'),
	)
	interest = models.CharField(max_length=10,choices=INTEREST_CHOICES,default='other')

	PHOTO_CHOICES = (
		('y','Yes'),
		('n','No')
	)
	processed = models.BooleanField(default=False)

	isMember = models.BooleanField('Member',default=False)
	member_no = models.CharField(max_length=20,default='',blank=True)
	email_address = models.EmailField(blank=True)

	isVolunteer = models.BooleanField('Volunteer',default=False)

	isDonor = models.BooleanField('Donor',default=False)
	voucher_no = models.CharField(max_length=100,default='',blank=True)
	donation_amount = models.IntegerField(default=0)

	markForDeletion = models.BooleanField('Mark for Deletion',default=False)
	markForTransposition = models.BooleanField('Mark for Transposition',default=False)

	phone_no = models.CharField(max_length=20,default='',blank=True)

	def __unicode__(self):
		return self.name + ', ' + self.address

class CitizenInterestForm(ModelForm):
	class Meta:
		model = Citizen
		fields = ['interest', 'processed','isMember','isVolunteer','isDonor','voucher_no','donation_amount','markForTransposition','markForDeletion','phone_no','member_no','email_address']

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	polling_station = models.ForeignKey(PollingStation,blank=True,null=True)
	assembly = models.ForeignKey(AssemblyConstituency,blank=True,null=True)

	def __unicode__(self):
		return 'Test'





