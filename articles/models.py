from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class TimeStampMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	id = models.AutoField(primary_key=True)

# TODO Set up more columns fot Article metadata and Table relationships (user with articles, likes, comments, etc)

# ROLES
Reader   = 'reader'
Writer   = 'writer'
Moderator= 'moderator' 
Uploader = 'data uploader'

ROLES = (
	(Reader, 'reader'),
	(Writer, 'writer'),
	(Moderator, 'moderator'), 
	(Uploader, 'data uploader'),
)

class Users(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	role = models.CharField(choices = ROLES, null=False, default=Reader, max_length=15)
	password = models.CharField(max_length=50)
	profile_picture = models.ImageField(default='user-default.png', null=True, blank=True)

	def __str__(self):
		return self.name


class Article(TimeStampMixin):
	title = models.CharField(null=False, max_length=50, unique=True)
	content = models.TextField(null=False)
	numVisits = models.IntegerField(null=True, auto_created=True)
	tags = models.CharField(null=True, max_length=200)
	author = models.ForeignKey(Users, on_delete=models.CASCADE)
	header_image = models.ImageField(default='default-header.png', null=True, blank=True)

	def __str__(self):
		return self.title

	# class Meta:
	# 	constraints = [
	# 		models.CheckConstraint(
	# 			check=Q(content__length__gte=100),
	# 			name="text_field_name_min_length",
	# 		)
	# 	]