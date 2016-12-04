from django.db import models

# Create your models here.

class Country(models.Model):
    cid=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.country

class Year(models.Model):
    yid=models.AutoField(primary_key=True)
    year=models.IntegerField()

    def __str__(self):
        return str(self.year)
    
class MaxTemp(models.Model):
    cid=models.ForeignKey(Country,default=None)
    year=models.ForeignKey(Year,default=None)

    jan=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    feb=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    mar=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    apr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    may=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    jun=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    jul=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    aug=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    sep=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    octu=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    nov=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    dec=models.DecimalField(max_digits=4, decimal_places=2,null=True)

    win=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    spr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    sumr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    aut=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    ann=models.DecimalField(max_digits=4, decimal_places=2,null=True)

    def __str__(self):
        return str(self.year)
    
class MinTemp(models.Model):
    cid=models.ForeignKey(Country,default=None)
    year=models.ForeignKey(Year,default=None)

    jan=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    feb=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    mar=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    apr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    may=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    jun=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    jul=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    aug=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    sep=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    octu=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    nov=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    dec=models.DecimalField(max_digits=4, decimal_places=2,null=True)

    win=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    spr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    sumr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    aut=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    ann=models.DecimalField(max_digits=4, decimal_places=2,null=True)

    def __str__(self):
        return str(self.year)
class MeanTemp(models.Model):
    cid=models.ForeignKey(Country,default=None)
    year=models.ForeignKey(Year,default=None)

    jan=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    feb=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    mar=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    apr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    may=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    jun=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    jul=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    aug=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    sep=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    octu=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    nov=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    dec=models.DecimalField(max_digits=4, decimal_places=2,null=True)

    win=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    spr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    sumr=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    aut=models.DecimalField(max_digits=4, decimal_places=2,null=True)
    ann=models.DecimalField(max_digits=4, decimal_places=2,null=True)

    def __str__(self):
        return str(self.year)

class Sunshine(models.Model):
    cid=models.ForeignKey(Country,default=None)
    year=models.ForeignKey(Year,default=None)

    jan=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    feb=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    mar=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    apr=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    may=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    jun=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    jul=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    aug=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sep=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    octu=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    nov=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    dec=models.DecimalField(max_digits=6, decimal_places=2,null=True)

    win=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    spr=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sumr=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    aut=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    ann=models.DecimalField(max_digits=6, decimal_places=2,null=True)

    def __str__(self):
        return str(self.year)

class Rainfall(models.Model):
    cid=models.ForeignKey(Country,default=None)
    year=models.ForeignKey(Year,default=None)

    jan=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    feb=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    mar=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    apr=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    may=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    jun=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    jul=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    aug=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sep=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    octu=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    nov=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    dec=models.DecimalField(max_digits=6, decimal_places=2,null=True)

    win=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    spr=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sumr=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    aut=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    ann=models.DecimalField(max_digits=6, decimal_places=2,null=True)

    def __str__(self):
        return str(self.year)
