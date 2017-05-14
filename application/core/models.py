from django.db import models


class Beverage(models.Model):
    name = models.CharField(max_length=100)
    alcohol = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipient(models.Model):
    position = models.PositiveSmallIntegerField(default=1, unique=True)
    beverage = models.ForeignKey(Beverage)
    total_quantity = models.PositiveSmallIntegerField(default=0, help_text="In mililiters")
    available_quantity = models.PositiveSmallIntegerField(default=0, help_text="In mililiters")
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.position)


class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="cocktails", blank=True)
    created = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class CocktailContent(models.Model):
    cocktail = models.ForeignKey(Cocktail)
    beverage = models.ForeignKey(Beverage)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.beverage.name
