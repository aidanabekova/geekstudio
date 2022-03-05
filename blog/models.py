from django.db import models


class Branch(models.Model):
    adres = models.CharField(max_length=100)

    def __str__(self):
        return self.adres


class Master(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='foto/')
    speciality = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return self.name


STARS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(choices=STARS)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.text


class Procedure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    master = models.ManyToManyField(Master, blank=True)

    def __str__(self):
        return self.name


