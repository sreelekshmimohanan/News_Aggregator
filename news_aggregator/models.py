from django.db import models



class regtable(models.Model):
    name=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    role=models.CharField(max_length=20, default='user')

class Reporter(models.Model):
    name=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    experience_years = models.IntegerField(default=0)
    specialization = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=200, blank=True) 
