from django.db import models

# Create your models here.
class Right(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    minage = models.PositiveSmallIntegerField()
    maxage = models.PositiveSmallIntegerField()
    enabled = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    link = models.URLField(blank = True)
    def __str__(self):
        return self.title+" ("+str(self.minage)+"-"+str(self.maxage)+")"


class Entry1(models.Model):
    name1 = models.CharField(max_length=512)
    fname = models.CharField(max_length=512)
    inputage = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name1+" "+self.fname

class Resnum(models.Model):
    num = models.PositiveSmallIntegerField()
