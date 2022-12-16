from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class book(models.Model):

    status_choices = [
        ('avaliable', 'avaliable'),
        ('rental', 'rental'),
        ('sold', 'sold')
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(
        category, on_delete=models.PROTECT, null=True, blank=True)
    photo_book = models.ImageField(
        upload_to='photos', height_field=None, null=True, blank=True)
    photo_author = models.ImageField(
        upload_to='photos', height_field=None, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    retal_price_day = models.IntegerField(null=True, blank=True)
    retal_period = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    status = models.CharField(
        max_length=200, null=True, blank=True, choices=status_choices)

    def __str__(self):
        return self.title
