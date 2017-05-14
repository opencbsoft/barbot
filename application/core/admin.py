from django.contrib import admin

from core.models import Beverage, Recipient, Cocktail, CocktailContent

class CocktailContentInline(admin.StackedInline):
    model = CocktailContent

class CocktailAdmin(admin.ModelAdmin):
    inlines = [CocktailContentInline, ]


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Beverage)
admin.site.register(Recipient)